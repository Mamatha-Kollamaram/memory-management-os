from PyQt6.QtCore import QObject, pyqtSignal
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class VirtualMemorySystem(QObject):
    page_loaded = pyqtSignal(dict)  # {process_id, page_number, status, location}
    simulation_complete = pyqtSignal(dict)  # {algorithm, hits, faults}
    visualization_ready = pyqtSignal(object)  # Emits a Matplotlib figure object

    def __init__(self):
        super().__init__()
        self.ram_size = 0
        self.page_size = 0
        self.frames = 0
        self.reset_state()

    def reset_state(self):
        self.ram = {}
        self.disk = {}
        self.page_order = deque()
        self.page_faults = 0
        self.page_hits = 0
        self.access_history = []

    def configure(self, ram_size, page_size):
        self.ram_size = ram_size
        self.page_size = page_size
        self.frames = ram_size // page_size
        self.reset_state()

    def load_page(self, process_id, page_number, data, algorithm="FIFO"):
        key = (process_id, page_number)
        result = {"process_id": process_id, "page_number": page_number, "algorithm": algorithm, "status": None, "location": None}

        if key in self.ram:
            self.page_hits += 1
            if algorithm == "LRU":
                self.page_order.remove(key)
                self.page_order.append(key)
            result.update({"status": "hit", "location": "RAM"})
        else:
            self.page_faults += 1
            if len(self.ram) < self.frames:
                self.ram[key] = data
                result["location"] = "RAM"
            else:
                evicted = self.replace_page(algorithm)
                self.disk[evicted] = self.ram.pop(evicted)
                self.ram[key] = data
                result["location"] = "RAM (replaced)"
            self.page_order.append(key)
            result["status"] = "fault"

        self.access_history.append(result)
        self.page_loaded.emit(result)
        return result

    def replace_page(self, algorithm):
        if algorithm == "FIFO":
            return self.page_order.popleft()
        elif algorithm == "LRU":
            return self.page_order.popleft()
        elif algorithm == "Optimal":
            future_access = {key: i for i, key in enumerate(self.page_order)}
            return max(future_access, key=future_access.get)
        return self.page_order.popleft()

    def run_simulation(self, pages, algorithms=["FIFO", "LRU", "Optimal"]):
        results = {}
        for algo in algorithms:
            self.reset_state()
            for process_id, page_number, data in pages:
                self.load_page(process_id, page_number, data, algo)
            results[algo] = {"hits": self.page_hits, "faults": self.page_faults, "access_history": self.access_history.copy()}

        self.simulation_complete.emit(results)
        self.visualization_ready.emit(self.create_visualization(results))
        return results

    def create_visualization(self, results):
        fig, axes = plt.subplots(1, 3, figsize=(12, 4))
        for ax, (algo, data) in zip(axes, results.items()):
            ax.bar(['Hits', 'Faults'], [data['hits'], data['faults']], color=['green', 'red'])
            ax.set_title(f'{algo} Performance')
            ax.set_ylabel('Count')

        plt.tight_layout()
        return fig  # Returning the figure object instead of saving it

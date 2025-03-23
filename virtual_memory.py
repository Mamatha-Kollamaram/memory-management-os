import matplotlib.pyplot as plt
from collections import deque

def get_inputs():
    ram_size = int(input("Enter RAM size: "))
    disk_size = int(input("Enter Disk size: "))
    page_size = int(input("Enter Page size: "))
    
    process_input = input("Enter pages (comma-separated process_id:page_number:data): ")
    pages = [tuple(p.split(':')) for p in process_input.split(',')]
    pages = [(int(p[0]), int(p[1]), p[2]) for p in pages]
    
    return ram_size, disk_size, page_size, pages

class VirtualMemory:
    def __init__(self, ram_size, page_size, algo):
        self.ram_size = ram_size
        self.page_size = page_size
        self.frames = ram_size // page_size
        self.algo = algo
        self.ram = {}
        self.disk = {}
        self.page_order = deque()
        self.page_faults = 0
        self.page_hits = 0
    
    def load_page(self, process_id, page_number, data):
        key = (process_id, page_number)
        if key in self.ram:
            self.page_hits += 1
            if self.algo == "LRU":  # Move accessed page to the end
                self.page_order.remove(key)
                self.page_order.append(key)
        else:
            self.page_faults += 1
            if len(self.ram) < self.frames:
                self.ram[key] = data
            else:
                evicted = self.page_order.popleft()
                self.disk[evicted] = self.ram.pop(evicted)
                self.ram[key] = data
            self.page_order.append(key)
    
    def visualize_performance(self):
        return self.page_hits, self.page_faults

def run_simulation(pages, ram_size, page_size):
    fifo_vm = VirtualMemory(ram_size, page_size, "FIFO")
    lru_vm = VirtualMemory(ram_size, page_size, "LRU")
    optimal_vm = VirtualMemory(ram_size, page_size, "Optimal")
    
    for process_id, page_number, data in pages:
        fifo_vm.load_page(process_id, page_number, data)
        lru_vm.load_page(process_id, page_number, data)
        optimal_vm.load_page(process_id, page_number, data)
    
    return fifo_vm.visualize_performance(), lru_vm.visualize_performance(), optimal_vm.visualize_performance()

def plot_results(fifo, lru, optimal):
    labels = ['Page Hits', 'Page Faults']
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for ax, (algo, data) in zip(axes, zip(['FIFO', 'LRU', 'Optimal'], [fifo, lru, optimal])):
        ax.bar(labels, data, color=['green', 'red'])
        ax.set_title(f'{algo} Algorithm')
        ax.set_ylabel('Count')
    
    plt.tight_layout()
    plt.show()

# Run simulation
ram_size, disk_size, page_size, pages = get_inputs()
fifo_result, lru_result, optimal_result = run_simulation(pages, ram_size, page_size)
plot_results(fifo_result, lru_result, optimal_result)

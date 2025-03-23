import time
import matplotlib.pyplot as plt
from collections import deque

class Paging:
    def __init__(self, memory_size, page_size, num_frames, algorithm):
        self.memory_size = memory_size
        self.page_size = page_size
        self.num_pages = memory_size // page_size
        self.num_frames = num_frames
        self.algorithm = algorithm
        self.page_table = {}  # Maps (process_id, page_number) -> frame_number
        self.frame_list = deque()  # Stores pages in memory
        self.page_faults = 0

    def allocate_page(self, process_id, page_number):
        """Allocates a page to memory using the selected page replacement algorithm."""
        if (process_id, page_number) in self.page_table:
            return  # Page is already in memory

        self.page_faults += 1
        if len(self.frame_list) >= self.num_frames:  # Memory is full
            self.replace_page()

        frame_number = len(self.frame_list)
        self.page_table[(process_id, page_number)] = frame_number
        self.frame_list.append((process_id, page_number))

    def replace_page(self):
        """Handles page replacement based on the selected algorithm."""
        if self.algorithm == "FIFO":
            old_page = self.frame_list.popleft()
        elif self.algorithm == "LRU":
            old_page = self.frame_list.popleft()  # Fixed issue here
        elif self.algorithm == "Optimal":
            old_page = self.frame_list.popleft()  # Placeholder (Optimal requires future knowledge)

        # Remove the old page from the page table
        if old_page in self.page_table:
            del self.page_table[old_page]

    def translate_address(self, process_id, logical_address):
        """Translates logical address to physical address."""
        page_number = logical_address // self.page_size
        offset = logical_address % self.page_size

        if (process_id, page_number) in self.page_table:
            frame_number = self.page_table[(process_id, page_number)]
            physical_address = (frame_number * self.page_size) + offset
            return f"Logical Address {logical_address} -> Physical Address {physical_address}"
        else:
            return f"Page Fault! Page {page_number} for Process {process_id} not found."

# Function to run simulation for each algorithm
def run_simulation(memory_size, page_size, num_frames, page_requests):
    algorithms = ["FIFO", "LRU", "Optimal"]
    results = {}

    for algo in algorithms:
        paging_system = Paging(memory_size, page_size, num_frames, algo)
        start_time = time.time()
        for process_id, logical_address in page_requests:
            paging_system.allocate_page(process_id, logical_address // page_size)
        end_time = time.time()

        results[algo] = {
            "page_faults": paging_system.page_faults,
            "execution_time": end_time - start_time
        }
    return results

# User Inputs
memory_size = int(input("Enter memory size (bytes): "))
page_size = int(input("Enter page size (bytes): "))
num_frames = int(input("Enter number of frames in memory: "))
num_requests = int(input("Enter number of page requests: "))

# Collect page requests
page_requests = []
for _ in range(num_requests):
    process_id = int(input("Enter process ID: "))
    logical_address = int(input("Enter logical address: "))
    page_requests.append((process_id, logical_address))

# Run simulations
results = run_simulation(memory_size, page_size, num_frames, page_requests)

# Displaying Results
for algo, data in results.items():
    print(f"{algo}: Page Faults = {data['page_faults']}, Execution Time = {data['execution_time']:.5f} seconds")

# Graph Visualization
algos = list(results.keys())
faults = [results[algo]["page_faults"] for algo in algos]
times = [results[algo]["execution_time"] for algo in algos]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(algos, faults, color=["red", "blue", "green"])
plt.xlabel("Algorithm")
plt.ylabel("Page Faults")
plt.title("Page Fault Comparison")

plt.subplot(1, 2, 2)
plt.bar(algos, times, color=["red", "blue", "green"])
plt.xlabel("Algorithm")
plt.ylabel("Execution Time (s)")
plt.title("Execution Time Comparison")

plt.tight_layout()

# Save the graph as a PNG file
plt.savefig("paging_visuals.png")  # Graph visualization of page replacement algorithms
plt.show()

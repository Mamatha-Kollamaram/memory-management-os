import time

class PagingSystem:
    def __init__(self, memory_size, page_size, num_frames):
        self.memory_size = memory_size
        self.page_size = page_size
        self.num_frames = num_frames
        self.frames = [-1] * num_frames  # Empty frames
        self.page_table = {}  # Stores mappings for each process
        self.page_requests = []

    def add_page_request(self, process_id, logical_address):
        """Adds a page request for translation."""
        page_number = logical_address // self.page_size
        if process_id not in self.page_table:
            self.page_table[process_id] = []
        self.page_requests.append((process_id, page_number))

    def simulate_algorithm(self, algorithm):
        """Runs FIFO, LRU, or Optimal page replacement algorithm."""
        if algorithm == "FIFO":
            return self.fifo()
        elif algorithm == "LRU":
            return self.lru()
        elif algorithm == "Optimal":
            return self.optimal()

    def optimal(self):
        """Simulates Optimal page replacement."""
        page_faults = 0
        start_time = time.perf_counter()

        for i, (process_id, page) in enumerate(self.page_requests):
            if process_id not in self.page_table:
                self.page_table[process_id] = []

            if page not in self.page_table[process_id]:
                page_faults += 1
                if len(self.page_table[process_id]) < self.num_frames:
                    self.page_table[process_id].append(page)
                else:
                    future_use = {}
                    for j in range(i + 1, len(self.page_requests)):
                        future_process, future_page = self.page_requests[j]
                        if future_process == process_id and future_page in self.page_table[process_id]:
                            future_use[future_page] = j

                    removed_page = min(self.page_table[process_id], key=lambda p: future_use.get(p, float("inf")))
                    self.page_table[process_id].remove(removed_page)
                    self.page_table[process_id].append(page)

        exec_time = time.perf_counter() - start_time
        return page_faults, exec_time

    def fifo(self):
        """Simulates FIFO page replacement."""
        queue = []
        page_faults = 0
        start_time = time.perf_counter()

        for process_id, page in self.page_requests:
            if process_id not in self.page_table:
                self.page_table[process_id] = []

            if page not in self.page_table[process_id]:
                page_faults += 1
                if len(queue) < self.num_frames:
                    queue.append(page)
                else:
                    removed_page = queue.pop(0)
                    if removed_page in self.page_table[process_id]:  
                        self.page_table[process_id].remove(removed_page)
                    queue.append(page)
                self.page_table[process_id].append(page)

        exec_time = time.perf_counter() - start_time
        return page_faults, exec_time

    def lru(self):
        """Simulates LRU page replacement."""
        page_stack = []
        page_faults = 0
        start_time = time.perf_counter()

        for process_id, page in self.page_requests:
            if process_id not in self.page_table:
                self.page_table[process_id] = []

            if page not in self.page_table[process_id]:
                page_faults += 1
                if len(page_stack) < self.num_frames:
                    page_stack.append(page)
                else:
                    removed_page = page_stack.pop(0)
                    if removed_page in self.page_table[process_id]:  
                        self.page_table[process_id].remove(removed_page)
                    page_stack.append(page)
                self.page_table[process_id].append(page)
            else:
                if page in page_stack:
                    page_stack.remove(page)
                page_stack.append(page)

        exec_time = time.perf_counter() - start_time
        return page_faults, exec_time

class Paging:
    def __init__(self, memory_size, page_size):
        self.memory_size = memory_size
        self.page_size = page_size
        self.num_pages = memory_size // page_size
        self.page_table = {}

    def allocate_page(self, process_id, page_number, frame_number):
        self.page_table[(process_id, page_number)] = frame_number

    def translate_address(self, process_id, logical_address):
        page_number = logical_address // self.page_size
        offset = logical_address % self.page_size

        if (process_id, page_number) in self.page_table:
            frame_number = self.page_table[(process_id, page_number)]
            physical_address = (frame_number * self.page_size) + offset
            return physical_address
        else:
            return "Page not found in memory!"

# Example Usage
paging_system = Paging(memory_size=1024, page_size=256)
paging_system.allocate_page(1, 0, 3)  # Assign process 1, page 0 to frame 3
print(paging_system.translate_address(1, 100))  # Example logical address translation


class Paging:
    def __init__(self, memory_size, page_size):
        """
        Initializes the paging system.
        :param memory_size: Total size of memory.
        :param page_size: Size of each page.
        """
        self.memory_size = memory_size
        self.page_size = page_size
        self.num_pages = memory_size // page_size
        self.page_table = {}  # Dictionary storing {(process_id, page_number): frame_number}

    def allocate_page(self, process_id, page_number, frame_number):
        """
        Assigns a page to a frame in memory.
        :param process_id: The process ID.
        :param page_number: The logical page number.
        :param frame_number: The physical frame number.
        """
        self.page_table[(process_id, page_number)] = frame_number

    def translate_address(self, process_id, logical_address):
        """
        Translates a logical address to a physical address.
        :param process_id: The process ID.
        :param logical_address: The logical address to translate.
        :return: The physical address or a page fault message.
        """
        page_number = logical_address // self.page_size
        offset = logical_address % self.page_size

        if (process_id, page_number) in self.page_table:
            frame_number = self.page_table[(process_id, page_number)]
            physical_address = (frame_number * self.page_size) + offset
            return f"Logical Address {logical_address} -> Physical Address {physical_address} (Frame {frame_number}, Offset {offset})"
        else:
            return f"Page Fault! Page {page_number} for Process {process_id} not found in memory."

# Example Usage
paging_system = Paging(memory_size=1024, page_size=256)

# Allocating pages manually
paging_system.allocate_page(1, 0, 3)  # Process 1, Page 0 -> Frame 3
paging_system.allocate_page(1, 1, 2)  # Process 1, Page 1 -> Frame 2
paging_system.allocate_page(2, 0, 1)  # Process 2, Page 0 -> Frame 1

# Translating logical addresses
print(paging_system.translate_address(1, 100))  # Expected: Physical Address in Frame 3
print(paging_system.translate_address(1, 260))  # Expected: Physical Address in Frame 2
print(paging_system.translate_address(2, 50))   # Expected: Physical Address in Frame 1
print(paging_system.translate_address(3, 100))  # Expected: Page Fault (Process 3 does not exist)


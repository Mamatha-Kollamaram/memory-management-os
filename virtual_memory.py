class VirtualMemory:
    def __init__(self, ram_size, disk_size, page_size):
        self.ram_size = ram_size
        self.disk_size = disk_size
        self.page_size = page_size
        self.ram = {}
        self.disk = {}

    def load_page(self, process_id, page_number, data):
        if len(self.ram) < self.ram_size // self.page_size:
            self.ram[(process_id, page_number)] = data
        else:
            evicted = next(iter(self.ram))
            self.disk[evicted] = self.ram.pop(evicted)  # Move to disk
            self.ram[(process_id, page_number)] = data

    def access_page(self, process_id, page_number):
        if (process_id, page_number) in self.ram:
            return f"Page {page_number} of Process {process_id} is in RAM."
        elif (process_id, page_number) in self.disk:
            return f"Page {page_number} of Process {process_id} is in Disk (Page Fault Occurred)."
        else:
            return f"Page Fault! Page {page_number} of Process {process_id} not found."

# Example Usage
vm = VirtualMemory(ram_size=1024, disk_size=2048, page_size=256)
vm.load_page(1, 0, "Data for Page 0")
vm.load_page(1, 1, "Data for Page 1")
print(vm.access_page(1, 0))  # Should be in RAM
print(vm.access_page(1, 2))  # Page Fault

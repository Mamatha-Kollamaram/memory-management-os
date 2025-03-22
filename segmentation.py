class Segment:
    def __init__(self, segment_id, base, limit):
        self.segment_id = segment_id  # Unique ID for the segment
        self.base = base  # Starting address in physical memory
        self.limit = limit  # Size of the segment

class Segmentation:
    def __init__(self):
        self.segment_table = {}  # Stores segment information for each process

    def allocate_segment(self, process_id, segment_id, base, limit):
        if process_id not in self.segment_table:
            self.segment_table[process_id] = []
        self.segment_table[process_id].append(Segment(segment_id, base, limit))

    def translate_address(self, process_id, segment_id, offset):
        if process_id in self.segment_table:
            for segment in self.segment_table[process_id]:
                if segment.segment_id == segment_id:
                    if 0 <= offset < segment.limit:
                        return f"Physical Address: {segment.base + offset}"
                    else:
                        return "Segment Fault! Offset out of bounds."
        return "Segment Fault! Segment not found."

# Example Usage
segmentation_system = Segmentation()
segmentation_system.allocate_segment(1, 0, 100, 300)  # Process 1, Segment 0 (Base: 100, Limit: 300)
segmentation_system.allocate_segment(1, 1, 500, 200)  # Process 1, Segment 1 (Base: 500, Limit: 200)

print(segmentation_system.translate_address(1, 0, 50))  # Should return Physical Address 150
print(segmentation_system.translate_address(1, 1, 180)) # Should return Physical Address 680
print(segmentation_system.translate_address(1, 1, 250)) # Should return Segment Fault
print(segmentation_system.translate_address(2, 0, 10))  # Should return Segment Fault (Process 2 doesn't exist)

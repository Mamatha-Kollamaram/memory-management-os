import matplotlib.pyplot as plt

class Segment:
    def __init__(self, segment_id, base, limit):
        self.segment_id = segment_id  # Unique ID for the segment
        self.base = base  # Starting address in physical memory
        self.limit = limit  # Size of the segment

class Segmentation:
    def __init__(self):
        self.segment_table = {}  # Stores segment information for each process
        self.translation_results = {"success": 0, "fault": 0}  # Track translation success/failures

    def allocate_segment(self, process_id, segment_id, base, limit):
        if process_id not in self.segment_table:
            self.segment_table[process_id] = []
        self.segment_table[process_id].append(Segment(segment_id, base, limit))

    def translate_address(self, process_id, segment_id, offset):
        if process_id in self.segment_table:
            for segment in self.segment_table[process_id]:
                if segment.segment_id == segment_id:
                    if 0 <= offset < segment.limit:
                        self.translation_results["success"] += 1
                        return f"Physical Address: {segment.base + offset}"
                    else:
                        self.translation_results["fault"] += 1
                        return "Segment Fault! Offset out of bounds."
        self.translation_results["fault"] += 1
        return "Segment Fault! Segment not found."

    def visualize_memory(self):
        fig, ax = plt.subplots()
        y = 0
        for process_id, segments in self.segment_table.items():
            for segment in segments:
                ax.barh(y, segment.limit, left=segment.base, color='blue', edgecolor='black')
                ax.text(segment.base + segment.limit / 2, y, f'P{process_id}-S{segment.segment_id}', ha='center', va='center', color='white', fontsize=10)
                y += 1
        ax.set_xlabel("Memory Address")
        ax.set_ylabel("Segments")
        ax.set_title("Memory Allocation (Segmentation)")
        plt.show()

    def visualize_translation_results(self):
        labels = ["Successful Translations", "Segment Faults"]
        values = [self.translation_results["success"], self.translation_results["fault"]]
        colors = ["green", "red"]
        plt.figure()
        plt.bar(labels, values, color=colors)
        plt.xlabel("Translation Outcome")
        plt.ylabel("Count")
        plt.title("Address Translation Success vs. Faults")
        plt.show()

# Example Usage
segmentation_system = Segmentation()

# Bulk Input for Segmentation
segment_input = input("Enter segments (format: process_id segment_id base limit, ...): ")
segments = segment_input.split(", ")
for seg in segments:
    process_id, segment_id, base, limit = map(int, seg.split())
    segmentation_system.allocate_segment(process_id, segment_id, base, limit)

# Bulk Input for Address Translations
translation_input = input("Enter translations (format: process_id segment_id offset, ...): ")
translations = translation_input.split(", ")
for trans in translations:
    process_id, segment_id, offset = map(int, trans.split())
    print(segmentation_system.translate_address(process_id, segment_id, offset))

# Visualizing memory allocation
segmentation_system.visualize_memory()

# Visualizing translation results
segmentation_system.visualize_translation_results()

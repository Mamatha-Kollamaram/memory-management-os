from PyQt6.QtCore import QObject, pyqtSignal
import matplotlib.pyplot as plt

class Segment:
    def __init__(self, segment_id, base, limit):
        self.segment_id = segment_id
        self.base = base
        self.limit = limit

class SegmentationSystem(QObject):
    # PyQt6 Signals for GUI communication
    translation_complete = pyqtSignal(dict)
    allocation_complete = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.segment_table = {}  # Now handles multiple processes
        self.translation_results = {"success": 0, "fault": 0}

    def allocate_segment(self, process_id, segment_id, base, limit):
        """Allocates segments for multiple processes."""
        if process_id not in self.segment_table:
            self.segment_table[process_id] = []
        
        self.segment_table[process_id].append(Segment(segment_id, base, limit))
        
        # Emit allocation result
        self.allocation_complete.emit({
            "process_id": process_id,
            "segment_id": segment_id,
            "base": base,
            "limit": limit,
            "status": "Allocated"
        })

    def translate_address(self, process_id, segment_id, offset):
        """Translates addresses for multiple processes."""
        result = {
            "process_id": process_id,
            "segment_id": segment_id,
            "offset": offset,
            "status": None,
            "physical_address": None
        }

        if process_id in self.segment_table:
            for segment in self.segment_table[process_id]:
                if segment.segment_id == segment_id:
                    if 0 <= offset < segment.limit:
                        physical_address = segment.base + offset
                        self.translation_results["success"] += 1
                        result.update({
                            "status": "success",
                            "physical_address": physical_address,
                            "message": f"Physical Address: {physical_address}"
                        })
                        self.translation_complete.emit(result)
                        return result
                    else:
                        self.translation_results["fault"] += 1
                        result.update({
                            "status": "fault",
                            "message": "Segment Fault! Offset out of bounds."
                        })
                        self.translation_complete.emit(result)
                        return result

        self.translation_results["fault"] += 1
        result.update({
            "status": "fault",
            "message": "Segment Fault! Segment not found."
        })
        self.translation_complete.emit(result)
        return result

    def bulk_allocate(self, segment_data):
        """Handles bulk allocation for multiple processes."""
        for seg in segment_data:
            process_id, segment_id, base, limit = seg
            self.allocate_segment(process_id, segment_id, base, limit)

    def bulk_translate(self, translation_data):
        """Handles bulk translation for multiple processes."""
        results = []
        for trans in translation_data:
            process_id, segment_id, offset = trans
            results.append(self.translate_address(process_id, segment_id, offset))
        return results

    def create_visualization(self):
        """Generates and directly displays visualization."""
        fig, axs = plt.subplots(1, 2, figsize=(12, 6))

        # Memory Allocation Visualization
        y = 0
        for process_id, segments in self.segment_table.items():
            for segment in segments:
                axs[0].barh(y, segment.limit, left=segment.base, color='blue', edgecolor='black')
                axs[0].text(segment.base + segment.limit / 2, y, 
                           f'P{process_id}-S{segment.segment_id}', 
                           ha='center', va='center', color='white', fontsize=10)
                y += 1
        axs[0].set_xlabel("Memory Address")
        axs[0].set_ylabel("Segments")
        axs[0].set_title("Memory Allocation (Segmentation)")

        # Translation Results Visualization
        labels = ["Successful Translations", "Segment Faults"]
        values = [self.translation_results["success"], self.translation_results["fault"]]
        colors = ["green", "red"]
        axs[1].bar(labels, values, color=colors)
        axs[1].set_xlabel("Translation Outcome")
        axs[1].set_ylabel("Count")
        axs[1].set_title("Address Translation Results")

        plt.tight_layout()
        plt.show()  # Directly display graph instead of saving

    def get_segment_table(self):
        """Returns segment table data for GUI display."""
        return {
            process_id: [
                {"id": seg.segment_id, "base": seg.base, "limit": seg.limit}
                for seg in segments
            ]
            for process_id, segments in self.segment_table.items()
        }

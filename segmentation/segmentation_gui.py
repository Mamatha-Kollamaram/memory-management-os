import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit
from PyQt6.QtGui import QFont

from .segmentation import SegmentationSystem

class SegmentationGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.system = SegmentationSystem()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Segmentation System")
        self.setGeometry(200, 200, 600, 500)
        self.setStyleSheet("background-color: #E6E6FA;")  # Lavender background

        # Layout
        layout = QVBoxLayout()

        # Styling
        label_style = "font-size: 14px; font-weight: bold; color: black;"  
        input_style = (
            "padding: 5px; font-size: 14px; border: 1px solid #D8BFD8; "
            "border-radius: 5px; background-color: white;"
        )
        btn_style = (
            "background-color: #D8BFD8; color: black; font-size: 14px; "
            "padding: 5px; border-radius: 5px;"
        )
        output_style = (
            "background-color: white; padding: 10px; border: 1px solid #D8BFD8; "
            "border-radius: 5px; font-size: 14px;"
        )

        # Memory Allocation Section
        self.process_id_input = QLineEdit(self)
        self.process_id_input.setStyleSheet(input_style)
        self.segment_id_input = QLineEdit(self)
        self.segment_id_input.setStyleSheet(input_style)
        self.base_input = QLineEdit(self)
        self.base_input.setStyleSheet(input_style)
        self.limit_input = QLineEdit(self)
        self.limit_input.setStyleSheet(input_style)
        self.allocate_btn = QPushButton("Allocate Segment", self)
        self.allocate_btn.setStyleSheet(btn_style)
        self.allocate_btn.clicked.connect(self.allocate_segment)

        layout.addWidget(self.create_label("Process ID:"))
        layout.addWidget(self.process_id_input)
        layout.addWidget(self.create_label("Segment ID:"))
        layout.addWidget(self.segment_id_input)
        layout.addWidget(self.create_label("Base Address:"))
        layout.addWidget(self.base_input)
        layout.addWidget(self.create_label("Limit:"))
        layout.addWidget(self.limit_input)
        layout.addWidget(self.allocate_btn)

        # Address Translation Section
        self.translation_process_id = QLineEdit(self)
        self.translation_process_id.setStyleSheet(input_style)
        self.translation_segment_id = QLineEdit(self)
        self.translation_segment_id.setStyleSheet(input_style)
        self.offset_input = QLineEdit(self)
        self.offset_input.setStyleSheet(input_style)
        self.translate_btn = QPushButton("Translate Address", self)
        self.translate_btn.setStyleSheet(btn_style)
        self.translate_btn.clicked.connect(self.translate_address)

        layout.addWidget(self.create_label("Translation - Process ID:"))
        layout.addWidget(self.translation_process_id)
        layout.addWidget(self.create_label("Segment ID:"))
        layout.addWidget(self.translation_segment_id)
        layout.addWidget(self.create_label("Offset:"))
        layout.addWidget(self.offset_input)
        layout.addWidget(self.translate_btn)

        # Output Display
        self.output = QTextEdit(self)
        self.output.setReadOnly(True)
        self.output.setStyleSheet(output_style)
        layout.addWidget(self.output)

        # Visualization Button
        self.visualize_btn = QPushButton("Generate Visualization", self)
        self.visualize_btn.setStyleSheet(btn_style)
        self.visualize_btn.clicked.connect(self.generate_visualization)
        layout.addWidget(self.visualize_btn)

        self.setLayout(layout)

    def create_label(self, text):
        label = QLabel(text, self)
        label.setStyleSheet("font-size: 14px; font-weight: bold; color: black;")  
        return label

    def allocate_segment(self):
        process_id = self.process_id_input.text()
        segment_id = self.segment_id_input.text()
        base = int(self.base_input.text())
        limit = int(self.limit_input.text())

        self.system.allocate_segment(process_id, segment_id, base, limit)
        self.output.append(f"Allocated Segment {segment_id} to Process {process_id}")

    def translate_address(self):
        process_id = self.translation_process_id.text()
        segment_id = self.translation_segment_id.text()
        offset = int(self.offset_input.text())

        result = self.system.translate_address(process_id, segment_id, offset)
        self.output.append(result["message"])

    def generate_visualization(self):
        image_path = self.system.create_visualization()
        self.output.append(f"Visualization saved as {image_path}")

# Running the App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SegmentationGUI()
    window.show()
    sys.exit(app.exec())

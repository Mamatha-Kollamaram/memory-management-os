import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, 
                            QLabel, QFrame, QScrollArea)
from PyQt6.QtGui import QFont, QPalette, QColor, QLinearGradient, QBrush, QPixmap
from PyQt6.QtCore import Qt, QPointF

from paging.paging_gui import PagingGUI
from segmentation.segmentation_gui import SegmentationGUI
from virtual_memory.virtual_memory_gui import VirtualMemoryGUI

class MainGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        self.setWindowTitle("Memory Management Simulator")
        self.setGeometry(200, 200, 600, 600)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Header
        header = QLabel("Welcome to Memory Management Simulator!")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_font = QFont("Arial", 40, QFont.Weight.Bold)
        header.setFont(header_font)
        header.setStyleSheet("color: #FBE4D6;")
        layout.addWidget(header)

        # Decorative line
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line)

        # Subheading
        subheading = QLabel("Memory Management Techniques in Operating System")
        subheading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subheading_font = QFont("Arial", 22, QFont.Weight.Bold)
        subheading.setFont(subheading_font)
        subheading.setStyleSheet("color: #FBE4D6;")
        layout.addWidget(subheading)

        # Image below the subheading
        image_label = QLabel(self)
        pixmap = QPixmap("memory_image.webp")  # Ensure this image exists in the project directory
        image_label.setPixmap(pixmap.scaled(400,400, Qt.AspectRatioMode.KeepAspectRatio))
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)

        # Explanation Texts
        self.add_explanation(layout, "What is Paging?", "Paging is a memory management scheme that eliminates the need for contiguous allocation of physical memory.")
        
        self.paging_button = QPushButton("Paging Simulator")
        self.paging_button.setStyleSheet(self.get_button_style())
        self.paging_button.clicked.connect(self.open_paging_gui)
        layout.addWidget(self.paging_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.add_explanation(layout, "What is Segmentation?", "Segmentation divides memory into variable-sized segments representing logical groupings.")
        
        self.segmentation_button = QPushButton("Segmentation Simulator")
        self.segmentation_button.setStyleSheet(self.get_button_style())
        self.segmentation_button.clicked.connect(self.open_segmentation_gui)
        layout.addWidget(self.segmentation_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.add_explanation(layout, "What is Virtual Memory?", "Virtual memory allows programs to use more memory than physically available by swapping data.")
        
        self.virtual_memory_button = QPushButton("Virtual Memory Simulator")
        self.virtual_memory_button.setStyleSheet(self.get_button_style())
        self.virtual_memory_button.clicked.connect(self.open_virtual_memory_gui)
        layout.addWidget(self.virtual_memory_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Footer
        footer = QLabel("© 2025 Memory Management Simulator")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_font = QFont("Arial", 8)
        footer.setFont(footer_font)
        footer.setStyleSheet("color: #4D55CC;")
        layout.addWidget(footer)

        scroll_area.setWidget(container)
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def add_explanation(self, layout, title, content):
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont("Arial", 22, QFont.Weight.Bold)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: #211C84;")
        layout.addWidget(title_label)

        content_label = QLabel(content)
        content_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        content_label.setWordWrap(True)
        content_font = QFont("Arial", 20)
        content_label.setFont(content_font)
        layout.addWidget(content_label)

    def apply_styles(self):
        self.setAutoFillBackground(True)
        palette = self.palette()
        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 600))
        gradient.setColorAt(0.0, QColor("#211C84"))
        gradient.setColorAt(0.5, QColor("#4D55CC"))
        gradient.setColorAt(1.0, QColor("#7A73D1"))
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

    def get_button_style(self):
        return """
            QPushButton {
                background-color: #B5A8D5;
                color: #211C84;
                border: none;
                padding: 12px 24px;
                text-align: center;
                font-size: 14px;
                margin: 4px 2px;
                border-radius: 8px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #7A73D1;
            }
            QPushButton:pressed {
                background-color: #4D55CC;
            }
        """

    def open_paging_gui(self):
        self.paging_window = PagingGUI()
        self.paging_window.show()

    def open_segmentation_gui(self):
        self.segmentation_window = SegmentationGUI()
        self.segmentation_window.show()

    def open_virtual_memory_gui(self):
        self.virtual_memory_window = VirtualMemoryGUI()
        self.virtual_memory_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = QFont("Arial", 10)
    app.setFont(font)
    window = MainGUI()
    window.show()
    sys.exit(app.exec())
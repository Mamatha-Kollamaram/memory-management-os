import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, 
                            QLabel, QFrame, QScrollArea, QHBoxLayout)
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize

# Import the actual GUI implementations from relevant modules
from paging.paging_gui import PagingGUI
from segmentation.segmentation_gui import SegmentationGUI
from virtual_memory.virtual_memory_gui import VirtualMemoryGUI

class MainGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Memory Management Simulator")
        self.setGeometry(200, 200, 600, 600)
        
        self.setWindowIcon(QIcon("icons/app_icon.png"))

        self.background_label = QLabel(self)
        pixmap = QPixmap("memory_image.webp")
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        header = QLabel("Welcome to Memory Management Simulator!")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setFont(QFont("Arial", 30, QFont.Weight.Bold))
        header.setStyleSheet("color: #2D1B69;")
        layout.addWidget(header)

        subheading = QLabel("Memory Management Techniques in Operating Systems")
        subheading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subheading.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        subheading.setStyleSheet("color: #2D1B69;")  
        layout.addWidget(subheading)

        self.add_explanation(layout, "What is Paging?", "Paging is a memory management scheme that eliminates the need for contiguous allocation of physical memory.", "icons/paging.png")
        self.paging_button = self.create_button("Paging Simulator", self.open_paging_gui, "icons/play.png")
        layout.addWidget(self.paging_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.add_explanation(layout, "What is Segmentation?", "Segmentation divides memory into variable-sized segments representing logical groupings.", "icons/segmentation.png")
        self.segmentation_button = self.create_button("Segmentation Simulator", self.open_segmentation_gui, "icons/play.png")
        layout.addWidget(self.segmentation_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.add_explanation(layout, "What is Virtual Memory?", "Virtual memory allows programs to use more memory than physically available by swapping data.", "icons/virtual_memory.png")
        self.virtual_memory_button = self.create_button("Virtual Memory Simulator", self.open_virtual_memory_gui, "icons/play.png")
        layout.addWidget(self.virtual_memory_button, alignment=Qt.AlignmentFlag.AlignCenter)

        footer = QLabel("© 2025 Memory Management Simulator")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setFont(QFont("Arial", 10))
        footer.setStyleSheet("color: #2D1B69;")  
        layout.addWidget(footer)

        scroll_area.setWidget(container)
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def add_explanation(self, layout, title, content, icon_path=None):
        h_layout = QHBoxLayout()
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h_layout.setSpacing(10)
        
        if icon_path:
            icon_label = QLabel()
            pixmap = QPixmap(icon_path)
            icon_label.setPixmap(pixmap.scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio))
            h_layout.addWidget(icon_label)
        
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #2D1B69;")  
        h_layout.addWidget(title_label)
        
        layout.addLayout(h_layout)

        content_label = QLabel(content)
        content_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        content_label.setWordWrap(True)
        content_label.setFont(QFont("Arial", 16))
        content_label.setStyleSheet("color: #2D1B69;")  
        layout.addWidget(content_label)

    def create_button(self, text, function, icon_path=None):
        button = QPushButton(text)
        if icon_path:
            button.setIcon(QIcon(icon_path))
            button.setIconSize(QSize(16, 16))
        
        button.setStyleSheet("""
            QPushButton {
                background-color: #B5A8D5;
                color: #211C84;
                border: none;
                padding: 12px 24px;
                font-size: 14px;
                border-radius: 8px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #7A73D1;
            }
            QPushButton:pressed {
                background-color: #4D55CC;
            }
        """)
        button.clicked.connect(function)
        return button

    def open_paging_gui(self):
        self.paging_window = PagingGUI()
        self.paging_window.show()

    def open_segmentation_gui(self):
        self.segmentation_window = SegmentationGUI()
        self.segmentation_window.show()

    def open_virtual_memory_gui(self):
        self.virtual_memory_window = VirtualMemoryGUI()
        self.virtual_memory_window.show()

    def resizeEvent(self, event):
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Arial", 10))
    window = MainGUI()
    window.show()
    sys.exit(app.exec())

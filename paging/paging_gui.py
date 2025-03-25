from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit
from PyQt6.QtGui import QPalette, QColor
import matplotlib.pyplot as plt
from .paging import PagingSystem

class PagingGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paging Memory Management")
        self.setGeometry(100, 100, 500, 600)

        # Set background color
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#E6E6FA"))  # Lavender
        self.setPalette(palette)

        self.layout = QVBoxLayout()

        self.memory_size_label = QLabel("<b>Enter memory size (bytes):</b>")
        self.memory_size_input = QLineEdit()
        self.layout.addWidget(self.memory_size_label)
        self.layout.addWidget(self.memory_size_input)

        self.page_size_label = QLabel("<b>Enter page size (bytes):</b>")
        self.page_size_input = QLineEdit()
        self.layout.addWidget(self.page_size_label)
        self.layout.addWidget(self.page_size_input)

        self.num_frames_label = QLabel("<b>Enter number of frames:</b>")
        self.num_frames_input = QLineEdit()
        self.layout.addWidget(self.num_frames_label)
        self.layout.addWidget(self.num_frames_input)

        self.request_label = QLabel("<b>Enter page requests (process_id logical_address):</b>")
        self.request_input = QTextEdit()
        self.layout.addWidget(self.request_label)
        self.layout.addWidget(self.request_input)

        # Apply Thistle color to the button
        self.run_button = QPushButton("Run Paging Simulation")
        self.run_button.setStyleSheet("background-color: #D8BFD8; color: black;")  # Thistle color
        self.run_button.clicked.connect(self.run_paging)
        self.layout.addWidget(self.run_button)

        self.output_label = QLabel("")
        self.layout.addWidget(self.output_label)

        self.setLayout(self.layout)

    def run_paging(self):
        try:
            memory_size = int(self.memory_size_input.text())
            page_size = int(self.page_size_input.text())
            num_frames = int(self.num_frames_input.text())

            page_requests_text = self.request_input.toPlainText().strip()
            page_requests = []

            if page_requests_text:
                for line in page_requests_text.split("\n"):
                    parts = line.strip().split()
                    if len(parts) == 2:
                        process_id, logical_address = int(parts[0]), int(parts[1])
                        page_requests.append((process_id, logical_address // page_size))

            paging_system = PagingSystem(memory_size, page_size, num_frames)
            paging_system.page_requests = page_requests  

            results = {
                "FIFO": paging_system.simulate_algorithm("FIFO"),
                "LRU": paging_system.simulate_algorithm("LRU"),
                "Optimal": paging_system.simulate_algorithm("Optimal"),
            }

            self.display_results(results)

        except ValueError:
            self.output_label.setText("Invalid input! Please enter numbers correctly.")

    def display_results(self, results):
        algorithms = list(results.keys())
        page_faults = [results[algo][0] for algo in algorithms]
        exec_times = [results[algo][1] for algo in algorithms]

        fig, ax1 = plt.subplots()

        ax1.bar(algorithms, page_faults, color='c', alpha=0.7, label='Page Faults')
        ax1.set_xlabel("Paging Algorithms", fontsize=14)
        ax1.set_ylabel("Page Faults", color='c', fontsize=14)
        ax1.tick_params(axis='y', labelcolor='c')

        ax2 = ax1.twinx()
        ax2.plot(algorithms, exec_times, color='r', marker='o', linestyle='-', linewidth=2, label='Execution Time')
        ax2.set_ylabel("Execution Time (seconds)", color='r', fontsize=14)
        ax2.tick_params(axis='y', labelcolor='r')

        plt.title("Page Faults & Execution Time Comparison", fontsize=16)
        plt.grid(True)
        plt.show()

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from .virtual_memory import VirtualMemorySystem

class VirtualMemoryGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.vm_system = VirtualMemorySystem()
        self.vm_system.simulation_complete.connect(self.display_results)
        self.vm_system.visualization_ready.connect(self.show_visualization)

    def init_ui(self):
        self.setWindowTitle("Virtual Memory Simulator")
        self.setGeometry(200, 200, 600, 550)

        layout = QVBoxLayout()
        self.setStyleSheet("background-color: #E6E6FA;")  # Lavender background

        self.ram_input = QLineEdit(self)
        self.ram_input.setPlaceholderText("Enter RAM Size (KB)")
        layout.addWidget(QLabel("RAM Size:"))
        layout.addWidget(self.ram_input)

        self.disk_input = QLineEdit(self)
        self.disk_input.setPlaceholderText("Enter Disk Size (KB)")
        layout.addWidget(QLabel("Disk Size:"))
        layout.addWidget(self.disk_input)

        self.page_size_input = QLineEdit(self)
        self.page_size_input.setPlaceholderText("Enter Page Size (KB)")
        layout.addWidget(QLabel("Page Size:"))
        layout.addWidget(self.page_size_input)

        self.pages_input = QTextEdit(self)
        self.pages_input.setPlaceholderText("Enter Pages (format: process_id:page_number:data, ...)")
        layout.addWidget(QLabel("Pages:"))
        layout.addWidget(self.pages_input)

        self.run_button = QPushButton("Run Simulation")
        self.run_button.setStyleSheet("background-color: #D8BFD8; color: black;")  # Thistle button
        self.run_button.clicked.connect(self.run_simulation)
        layout.addWidget(self.run_button)

        self.result_label = QLabel("Results:")
        layout.addWidget(self.result_label)

        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.canvas = None  # Placeholder for the Matplotlib canvas
        self.setLayout(layout)

    def run_simulation(self):
        ram_size = int(self.ram_input.text())
        disk_size = int(self.disk_input.text())
        page_size = int(self.page_size_input.text())

        self.vm_system.configure(ram_size, disk_size, page_size)

        pages = []
        raw_input = self.pages_input.toPlainText().split(",")
        for entry in raw_input:
            parts = entry.strip().split(":")
            if len(parts) == 3:
                pages.append((int(parts[0]), int(parts[1]), parts[2]))

        results = self.vm_system.run_simulation(pages)
        self.display_results(results)

    def display_results(self, results):
        output = ""
        for algo, data in results.items():
            output += f"{algo}: Page Hits = {data['hits']}, Page Faults = {data['faults']}\n"
        self.result_text.setText(output)

    def show_visualization(self, fig):
        if self.canvas is not None:
            self.layout().removeWidget(self.canvas)
            self.canvas.deleteLater()
        self.canvas = FigureCanvas(fig)
        self.layout().addWidget(self.canvas)
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication([])
    window = VirtualMemoryGUI()
    window.show()
    app.exec()

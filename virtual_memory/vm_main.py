import sys
from PyQt6.QtWidgets import QApplication
from virtual_memory_gui import VirtualMemoryGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VirtualMemoryGUI()
    window.show()
    sys.exit(app.exec())

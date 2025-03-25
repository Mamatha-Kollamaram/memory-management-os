from segmentation_gui import SegmentationGUI
import sys
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SegmentationGUI()
    window.show()
    sys.exit(app.exec())

from PyQt6.QtWidgets import QApplication
import sys
from paging_gui import PagingGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PagingGUI()
    window.show()
    sys.exit(app.exec())

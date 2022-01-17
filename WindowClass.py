from PyQt6.QtWidgets import QApplication, QWidget
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Port Scanner")
        self.setFixedWidth(400)
        self.setFixedHeight(400)



app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
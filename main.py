from PySide6.QtWidgets import QApplication, QWidget
import sys

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("voidtube")
        self.resize(900,600)


if __name__=="__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec())
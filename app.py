import threading
from PyQt6 import QtCore, QtGui, QtWidgets
import socket
from PyQt6.QtCore import QThread, QObject, pyqtSignal


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Python Port Scanner")
        MainWindow.resize(500, 565)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("border-radius: 10px;\n"
                                        "background-color: green;\n"
                                        "color: white;")
        self.start_button.setObjectName("start_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.start_button)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_addres = QtWidgets.QLineEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_addres.sizePolicy().hasHeightForWidth())
        self.input_addres.setSizePolicy(sizePolicy)
        self.input_addres.setMinimumSize(QtCore.QSize(0, 40))
        self.input_addres.setFont(font)
        self.input_addres.setStyleSheet("border-radius: 10px;")
        self.input_addres.setObjectName("input_addres")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.splitter)
        self.output_addres = QtWidgets.QListWidget(self.centralwidget)
        self.output_addres.setFont(font)
        self.output_addres.setStyleSheet("border-radius: 10px")
        self.output_addres.setObjectName("output_addres")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.output_addres)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.start_button.clicked.connect(self.start_scan)

    def get_adress(self):
        return self.input_addres.text().strip()

    def start_scan(self):
        if not self.get_adress():
            return

        self.output_addres.clear()
        self.worker = WorkingThread(self)
        self.start_button.setEnabled(False)
        self.start_button.setText("Calculating")
        self.start_button.setStyleSheet("QPushButton { background-color: gray; border-radius: 10px; }")
        self.worker.start()

        def format_button():
            self.start_button.setEnabled(True)
            self.start_button.setText("START")
            self.start_button.setStyleSheet("QPushButton { background-color: green; border-radius: 10px; }")

        self.worker.finished.connect(format_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Port Scanner"))
        self.start_button.setText(_translate("MainWindow", "START"))
        self.label.setText(_translate("MainWindow", "Adress ip"))


class WorkingThread(QThread):
    def __init__(self, ui_Form: Ui_MainWindow):
        super().__init__()
        self.app = ui_Form
        self.ip = socket.gethostbyname(self.app.get_adress())

    def port_scan(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        try:
            con = sock.connect((self.ip, port))
            self.app.output_addres.addItem(f'Port {port} is open')
        except:
            pass

    def run(self):
        for x in range(1, 65535):
            t = threading.Thread(target=self.port_scan, kwargs={'port': x})
            t.start()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

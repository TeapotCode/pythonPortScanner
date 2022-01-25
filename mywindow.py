import threading
from PyQt6 import QtCore, QtGui, QtWidgets
import socket
from PyQt6.QtCore import QThread, QObject, pyqtSignal


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(864, 422)
        Form.setStyleSheet("QWidget {\n"
                           "border-radius: 10px;\n"
                           "}\n"
                           "QPushButton {\n"
                           "background-color: green;\n"
                           "color: white;\n"
                           "border-radius: 10px;\n"
                           "}\n"
                           "QListWidget {\n"
                           "border-radius: 10px;\n"
                           "}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.port_list_left = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.port_list_left.setFont(font)
        self.port_list_left.setStyleSheet("")
        self.port_list_left.setObjectName("port_list_left")
        self.gridLayout.addWidget(self.port_list_left, 2, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(9, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(36)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.port_list_right = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.port_list_right.setFont(font)
        self.port_list_right.setObjectName("port_list_right")
        self.gridLayout.addWidget(self.port_list_right, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 13)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.adress_ip = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adress_ip.sizePolicy().hasHeightForWidth())
        self.adress_ip.setSizePolicy(sizePolicy)
        self.adress_ip.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        self.adress_ip.setFont(font)
        self.adress_ip.setStyleSheet("")
        self.adress_ip.setPlaceholderText("")
        self.adress_ip.setClearButtonEnabled(True)
        self.adress_ip.setObjectName("adress_ip")
        self.verticalLayout_2.addWidget(self.adress_ip)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.ports = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ports.sizePolicy().hasHeightForWidth())
        self.ports.setSizePolicy(sizePolicy)
        self.ports.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        self.ports.setFont(font)
        self.ports.setClearButtonEnabled(True)
        self.ports.setObjectName("ports")
        self.verticalLayout.addWidget(self.ports)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.start_scan)

    def start_scan(self):
        self.worker = WorkingThread(self)
        self.pushButton.setEnabled(False)
        self.pushButton.setText("Calculating")
        self.pushButton.setStyleSheet("QPushButton { background-color: gray }")
        self.worker.start()

        def format_button():
            self.pushButton.setEnabled(True)
            self.pushButton.setText("START")

            self.pushButton.setStyleSheet("QPushButton { background-color: green }")

        self.worker.finished.connect(format_button)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "START"))
        self.label_3.setText(_translate("Form", "Adress ip"))
        self.label_2.setText(_translate("Form", "Ports"))

    def get_adress(self):
        return self.adress_ip.text().strip()


class WorkingThread(QThread):
    def __init__(self, ui_Form: Ui_Form):
        super().__init__()
        self.app = ui_Form

    def port_scan(self, port):
        target = self.app.get_adress()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            con = s.connect((target, port))
            self.app.port_list_left.addItem("Port {} is open".format(port))
        except:
            pass

    def run(self):
        for x in range(1, 65535):
            t = threading.Thread(target=self.port_scan, kwargs={'port': x})
            t.start()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

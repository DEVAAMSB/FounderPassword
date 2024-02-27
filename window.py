from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
from main import password_maker


class Ui_password(object):
    def setupUi(self, password):
        password.setObjectName("password")
        password.resize(430, 280)
        password.setMinimumSize(QtCore.QSize(430, 280))
        password.setMaximumSize(QtCore.QSize(430, 280))
        password.setStyleSheet("#passwordmaker_btn:hover{\n"
"opacity:50%\n"
"}")
        self.centralwidget = QtWidgets.QWidget(password)
        self.centralwidget.setObjectName("centralwidget")
        self.upper = QtWidgets.QCheckBox(self.centralwidget)
        self.upper.setGeometry(QtCore.QRect(30, 30, 111, 31))
        self.upper.setChecked(True)
        self.upper.setObjectName("upper")
        self.lower = QtWidgets.QCheckBox(self.centralwidget)
        self.lower.setGeometry(QtCore.QRect(150, 30, 111, 31))
        self.lower.setChecked(True)
        self.lower.setObjectName("lower")
        self.number = QtWidgets.QCheckBox(self.centralwidget)
        self.number.setGeometry(QtCore.QRect(260, 30, 71, 31))
        self.number.setChecked(True)
        self.number.setObjectName("number")
        self.symbol = QtWidgets.QCheckBox(self.centralwidget)
        self.symbol.setGeometry(QtCore.QRect(340, 30, 71, 31))
        self.symbol.setChecked(True)
        self.symbol.setObjectName("symbol")
        self.length_label = QtWidgets.QLabel(self.centralwidget)
        self.length_label.setGeometry(QtCore.QRect(30, 70, 41, 31))
        self.length_label.setObjectName("length_label")
        self.password_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineedit.setGeometry(QtCore.QRect(30, 130, 311, 31))
        self.password_lineedit.setObjectName("password_lineedit")
        self.copy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.copy_btn.setGeometry(QtCore.QRect(340, 130, 61, 31))
        self.copy_btn.clicked.connect(self.save_text_to_clipboard)
        self.copy_btn.setObjectName("copy_btn")
        self.passwordmaker_btn = QtWidgets.QPushButton(self.centralwidget)
        self.passwordmaker_btn.setGeometry(QtCore.QRect(30, 170, 371, 41))
        self.passwordmaker_btn.setObjectName("passwordmaker_btn")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 120, 391, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(80, 70, 51, 31))
        self.spinBox.setMaximum(86)
        self.spinBox.setProperty("value", 20)
        self.spinBox.setObjectName("spinBox")
        self.groupBox.raise_()
        self.upper.raise_()
        self.lower.raise_()
        self.number.raise_()
        self.symbol.raise_()
        self.length_label.raise_()
        self.password_lineedit.raise_()
        self.copy_btn.raise_()
        self.passwordmaker_btn.raise_()
        self.spinBox.raise_()
        password.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(password)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName("menubar")
        password.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(password)
        self.statusbar.setObjectName("statusbar")
        password.setStatusBar(self.statusbar)

        self.retranslateUi(password)
        QtCore.QMetaObject.connectSlotsByName(password)

        self.passwordmaker_btn.clicked.connect(self.make_password)


    def make_password(self):
        password = password_maker(self.upper.isChecked(), self.lower.isChecked(), self.number.isChecked(), self.symbol.isChecked(), int(self.spinBox.value()))
        self.password_lineedit.setText(password)

    def save_text_to_clipboard(self):
        text = self.password_lineedit.text()
        QApplication.clipboard().setText(text)

    def retranslateUi(self, password):
        _translate = QtCore.QCoreApplication.translate
        password.setWindowTitle(_translate("password", "Founder Password"))
        self.upper.setText(_translate("password", "uppercase letters"))
        self.lower.setText(_translate("password", "lowercase letters"))
        self.number.setText(_translate("password", "numbers"))
        self.symbol.setText(_translate("password", "symbols"))
        self.length_label.setText(_translate("password", "length"))
        self.copy_btn.setText(_translate("password", "copy"))
        self.passwordmaker_btn.setText(_translate("password", "make new passwore"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    password = QtWidgets.QMainWindow()
    ui = Ui_password()
    ui.setupUi(password)
    password.show()
    sys.exit(app.exec_())

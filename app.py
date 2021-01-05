from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
from project1_frontend import Namecard

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.title = "NameCard Management"
        self.date = datetime.now().strftime("%B %d, %Y")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")#主窗口
        MainWindow.resize(445, 315)
        font = QtGui.QFont()
        font.setFamily("consolas")
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)#标签1：NameCard Management
        self.label_1.setGeometry(QtCore.QRect(12, 9, 450, 108))
        font = QtGui.QFont()
        font.setFamily("consolas")
        font.setPointSize(28)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)#标签2：时间戳
        self.label_2.setGeometry(QtCore.QRect(20, 251, 100, 30))
        font = QtGui.QFont()
        font.setFamily("consolas")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)#标签3：用户名
        self.label_3.setGeometry(QtCore.QRect(150, 140, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)#标签4：密码
        self.label_4.setGeometry(QtCore.QRect(150, 170, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)#输入框1
        self.lineEdit.setGeometry(QtCore.QRect(260, 139, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setClearButtonEnabled(True)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)#输入框2
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 169, 151, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)#按钮：登录
        self.pushButton.setGeometry(QtCore.QRect(230, 240, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.init_root)##让图形界面与相关操作互动

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)#pushButton_2：Quit按钮
        self.pushButton_2.setGeometry(QtCore.QRect(320, 240, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.quit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.title))
        self.label_1.setText(_translate("MainWindow", "NameCard Management"))
        self.label_2.setText(_translate("MainWindow", self.date))
        self.label_3.setText(_translate("MainWindow", "Username:"))
        self.label_4.setText(_translate("MainWindow", "Password:"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))

    def quit(self):
        sys.exit(app.exec_())

    def init_root(self):
        user = self.lineEdit.text()
        pas = self.lineEdit_2.text()
        if(user=='limyu' and pas=='pas'):
            MainWindow.destroy()
            root=Tk()
            application=Namecard(root)#PASS IT TO OUR CLASS WHITH ITS PROPERTIES IN CLASS
            root.mainloop()#RUN UNTIL CLOSING THE WINDOW MANUALLY
        else:
            print("ERROR")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        
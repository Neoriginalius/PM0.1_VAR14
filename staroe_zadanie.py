import random
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainTheme = QtWidgets.QTextEdit(self.centralwidget)
        self.mainTheme.setGeometry(QtCore.QRect(0, 0, 411, 61))
        self.mainTheme.setStyleSheet("background-color: rgb(159, 169, 226);\n"
"background-color: rgb(151, 180, 247);")
        self.mainTheme.setReadOnly(True)
        self.mainTheme.setObjectName("mainTheme")
        self.secondTheme = QtWidgets.QTextEdit(self.centralwidget)
        self.secondTheme.setGeometry(QtCore.QRect(-10, 60, 421, 351))
        self.secondTheme.setStyleSheet("background-color: rgb(159, 169, 226);\n"
"background-color: rgb(199, 211, 240);\n"
"")
        self.secondTheme.setReadOnly(True)
        self.secondTheme.setObjectName("secondTheme")

        self.textVedi = QtWidgets.QTextEdit(self.centralwidget)
        self.textVedi.setEnabled(True)
        self.textVedi.setGeometry(QtCore.QRect(20, 80, 251, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.textVedi.setFont(font)
        self.textVedi.setStyleSheet("background-color: rgb(199, 211, 240);\n"
"")
        self.textVedi.setLineWidth(1)
        self.textVedi.setReadOnly(True)
        self.textVedi.setObjectName("textVedi")

        self.textRezult = QtWidgets.QTextEdit(self.centralwidget)
        self.textRezult.setGeometry(QtCore.QRect(20, 120, 241, 31))
        self.textRezult.setStyleSheet("background-color: rgb(199, 211, 240);")
        self.textRezult.setReadOnly(True)
        self.textRezult.setObjectName("textRezult")



        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.enterS())
        self.pushButton1.setGeometry(QtCore.QRect(30, 330, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("background-color: rgb(0, 85, 255);\n" "color: rgb(255, 255, 255);")
        self.pushButton1.setObjectName("pushButton1")




        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 330, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        self.lineVvedi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineVvedi.setGeometry(QtCore.QRect(280, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineVvedi.setFont(font)
        self.lineVvedi.setText("")
        self.lineVvedi.setObjectName("lineVvedi")

        self.lineVvedi_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineVvedi_2.setGeometry(QtCore.QRect(270, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineVvedi_2.setFont(font)
        self.lineVvedi_2.setText("")
        self.lineVvedi_2.setObjectName("lineVvedi_2")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 160, 221, 151))
        self.textEdit.setObjectName("textEdit")


        self.textRezult_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textRezult_2.setGeometry(QtCore.QRect(20, 160, 131, 31))
        self.textRezult_2.setStyleSheet("background-color: rgb(199, 211, 240);")
        self.textRezult_2.setReadOnly(True)
        self.textRezult_2.setObjectName("textRezult_2")



        self.secondTheme.raise_()
        self.mainTheme.raise_()
        self.textVedi.raise_()
        self.textRezult.raise_()
        self.lineVvedi.raise_()
        self.pushButton1.raise_()
        self.pushButton.raise_()
        self.lineVvedi_2.raise_()
        self.textRezult_2.raise_()
        self.textEdit.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.lineVvedi.clear)
        self.pushButton.clicked.connect(self.lineVvedi_2.clear)
        self.pushButton.clicked.connect(self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор граней кубиков"))
        self.mainTheme.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#16a31d;\">Генератор граней кубиков</span></p></body></html>"))
        self.secondTheme.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textVedi.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0c40ff;\">Введите кол-во кубиков:</span></p></body></html>"))
        self.textRezult.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0c40ff;\">Введите кол-во граней:</span></p></body></html>"))
        self.pushButton1.setText(_translate("MainWindow", "Выполнить"))
        self.pushButton.setText(_translate("MainWindow", "Очистить поля"))
        self.textRezult_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0c40ff;\">Результат:</span></p></body></html>"))



    def enterS(self):
        try:
            itog = ''
            schet = ''
            schitaet = 0
            kubiki_max = int(self.lineVvedi.text())
            max_grani = int(self.lineVvedi_2.text())
            for i in range(1, kubiki_max + 1):
                grani = random.randint(1, max_grani)
                itog += (str(i) + "-й кубик: " + str(grani)+"\n")
                schitaet += grani
                schet = "Сумма гарней: " + str(schitaet)
                self.textEdit.setText(itog + str(schet))
        except Exception:
            self.textEdit.setText("Ошибка, необходимо ввести цифровые значения!")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('scp.jpg'))

    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('scp.jpg'))
    MainWindow.setFixedSize(410, 451)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

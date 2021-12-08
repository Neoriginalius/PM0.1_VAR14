import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.head = QtWidgets.QTextEdit(self.centralwidget)
        self.head.setGeometry(QtCore.QRect(0, 0, 411, 61))
        self.head.setStyleSheet("background-color: rgb(159, 169, 226);\n"
"background-color: rgb(151, 180, 247);")
        self.head.setReadOnly(True)
        self.head.setObjectName("head")
        self.secondTheme = QtWidgets.QTextEdit(self.centralwidget)
        self.secondTheme.setGeometry(QtCore.QRect(-10, 60, 421, 351))
        self.secondTheme.setStyleSheet("background-color: rgb(159, 169, 226);\n"
"background-color: rgb(199, 211, 240);\n"
"")
        self.secondTheme.setReadOnly(True)
        self.secondTheme.setObjectName("secondTheme")

        self.entercount_text = QtWidgets.QTextEdit(self.centralwidget)
        self.entercount_text.setEnabled(True)
        self.entercount_text.setGeometry(QtCore.QRect(20, 80, 251, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.entercount_text.setFont(font)
        self.entercount_text.setStyleSheet("background-color: rgb(199, 211, 240);\n" "")
        self.entercount_text.setLineWidth(1)
        self.entercount_text.setReadOnly(True)
        self.entercount_text.setObjectName("entercount_text")

        self.entercount_textgrani = QtWidgets.QTextEdit(self.centralwidget)
        self.entercount_textgrani.setGeometry(QtCore.QRect(20, 120, 241, 31))
        self.entercount_textgrani.setStyleSheet("background-color: rgb(199, 211, 240);")
        self.entercount_textgrani.setReadOnly(True)
        self.entercount_textgrani.setObjectName("entercount_textgrani")

        self.btn_do = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.enterS())
        self.btn_do.setGeometry(QtCore.QRect(30, 330, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_do.setFont(font)
        self.btn_do.setStyleSheet("background-color: rgb(0, 85, 255);\n" "color: rgb(255, 255, 255);")
        self.btn_do.setObjectName("btn_do")

        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(240, 330, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(0, 85, 255);\n" "color: rgb(255, 255, 255);")
        self.btn_clear.setObjectName("btn_clear")

        self.entry_fieldkub = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_fieldkub.setGeometry(QtCore.QRect(280, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.entry_fieldkub.setFont(font)
        self.entry_fieldkub.setText("")
        self.entry_fieldkub.setObjectName("entry_fieldkub")

        self.entry_fieldgran = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_fieldgran.setGeometry(QtCore.QRect(270, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.entry_fieldgran.setFont(font)
        self.entry_fieldgran.setText("")
        self.entry_fieldgran.setObjectName("entry_fieldgran")

        self.resp_output = QtWidgets.QTextEdit(self.centralwidget)
        self.resp_output.setGeometry(QtCore.QRect(160, 160, 221, 151))
        self.resp_output.setObjectName("resp_output")


        self.rezult_textline = QtWidgets.QTextEdit(self.centralwidget)
        self.rezult_textline.setGeometry(QtCore.QRect(20, 160, 131, 31))
        self.rezult_textline.setStyleSheet("background-color: rgb(199, 211, 240);")
        self.rezult_textline.setReadOnly(True)
        self.rezult_textline.setObjectName("rezult_text")



        self.secondTheme.raise_()
        self.head.raise_()
        self.entercount_text.raise_()
        self.entercount_textgrani.raise_()
        self.entry_fieldkub.raise_()
        self.btn_do.raise_()
        self.btn_clear.raise_()
        self.entry_fieldgran.raise_()
        self.rezult_textline.raise_()
        self.resp_output.raise_()

        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        self.btn_clear.clicked.connect(self.entry_fieldkub.clear)
        self.btn_clear.clicked.connect(self.entry_fieldgran.clear)
        self.btn_clear.clicked.connect(self.resp_output.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор граней кубиков"))
        self.head.setHtml(_translate("MainWindow",
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#16a31d;\">Генератор граней кубиков</span></p></body></html>"))
        self.secondTheme.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.entercount_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0c40ff;\">Введите кол-во кубиков:</span></p></body></html>"))
        self.entercount_textgrani.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0c40ff;\">Введите кол-во граней:</span></p></body></html>"))
        self.btn_do.setText(_translate("MainWindow", "Выполнить"))
        self.btn_clear.setText(_translate("MainWindow", "Очистить поля"))
        self.rezult_textline.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0c40ff;\">Результат:</span></p></body></html>"))

    def enterS(self):
        try:
            output = ''
            count = ''
            count_all = 0
            kubiki_max = int(self.entry_fieldkub.text())
            grani_max = int(self.entry_fieldgran.text())
            for i in range(1, kubiki_max + 1):
                grani = random.randint(1, grani_max)
                output += (str(i) + "-й кубик: " + str(grani)+"\n")
                count_all += grani
                count = "Сумма гарней: " + str(count_all)
            self.resp_output.setText(output + str(count))
        except Exception:
            self.resp_output.setText("Ошибка, необходимо ввести цифровые значения!")


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


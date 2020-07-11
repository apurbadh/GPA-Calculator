

from PyQt5 import QtCore, QtGui, QtWidgets

def gpaSub(marks, typ):
    try:
        marks = int(marks)
        gpaal = [0.8, 0.8, 1.2,1.6,2.0,2.4,2.8,3.2,3.6,4,4]
        if typ == 0:
            marks = (marks/75)*100
        elif typ == 1:
            marks = marks * 2
        ind = int(marks//10)
        answer = gpaal[ind]
        return answer
    except:
        return 0

class Ui_MainWindow(object):

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(334, 419)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gpac.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 64, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 64, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 64, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 64, 19))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 200, 64, 19))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 240, 64, 19))
        self.label_7.setObjectName("label_7")
        self.answerLab = QtWidgets.QLabel(self.centralwidget)
        self.answerLab.setGeometry(QtCore.QRect(120, 320, 100, 25))
        self.answerLab.setObjectName("answerLab")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 0, 113, 29))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 40, 113, 29))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 80, 113, 29))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 120, 113, 29))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 160, 113, 29))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(70, 200, 113, 29))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 240, 113, 29))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(110, 280, 113, 29))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 340, 91, 27))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 280, 91, 29))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.buttonClick)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def buttonClick(self):
        _translate = QtCore.QCoreApplication.translate
        mat = self.lineEdit.text()
        opt = self.lineEdit_2.text()
        sci = self.lineEdit_3.text()
        eng = self.lineEdit_4.text()
        nep = self.lineEdit_5.text()
        soc = self.lineEdit_6.text()
        eph = self.lineEdit_7.text()
        sel = self.comboBox.currentText()
        com = self.lineEdit_8.text()
        submarksList = [mat, opt, sci, eng, nep, soc, eph, com]
        allGPA = []
        wri = "Invalid Value"
        for i in range(len(submarksList)):
            if i <= 1:
                typ = 2
            elif i == 7 and sel == "Computer":
                typ = 1
            else:
                typ = 0
            answer = gpaSub(submarksList[i], typ)
            if answer == 0:
                break
            allGPA.append(answer)
        else:
            gpa = round(sum(allGPA)/8,2)
            wri = gpa
        self.answerLab.setText(_translate("MainWindow", f"{wri}"))

            
            
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GPA Converter"))
        self.label.setText(_translate("MainWindow", "Maths:"))
        self.label_2.setText(_translate("MainWindow", "Opt.Maths :"))
        self.label_3.setText(_translate("MainWindow", "Science :"))
        self.label_4.setText(_translate("MainWindow", "English :"))
        self.label_5.setText(_translate("MainWindow", "Nepali :"))
        self.label_6.setText(_translate("MainWindow", "Social :"))
        self.label_7.setText(_translate("MainWindow", "EPH :"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Computer"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Computer"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Account"))
    




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


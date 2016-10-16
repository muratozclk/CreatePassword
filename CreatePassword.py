# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys,random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class WindowDesigner(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self,Form):
        Form.setObjectName("Dialog")
        Form.resize(441, 84)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 20, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(20, 20, 41, 31))
        self.spinBox.setObjectName("spinBox")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(160, 20, 271, 31))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.CreatePassword)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create Password"))
        self.pushButton.setText(_translate("Dialog", "Sifre Al"))

    #Şifre ürettik
    def Random(self,sayi):
        büyükHarf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Y','Z','W','Q','X']
        kücükHarf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','y','z','w','q','x']
        sayılar = ['0','1','2','3','4','5','6','7','8','9']
        karakterler = ['?','@','!','#','%','+','-','*']
        password = []

        #Burdayız
        if(sayi == 6):
            password[0:0] = random.sample(büyükHarf,2)
            password[1:1] = random.sample(kücükHarf, 2)
            password[2:2] = random.sample(sayılar, 1)
            password[3:3] = random.sample(karakterler, 1)
            password = random.sample(password,6)
            passwordStr = ''.join(password)
            return passwordStr
        elif(sayi == 7):
            password[0:0] = random.sample(büyükHarf, 2)
            password[1:1] = random.sample(kücükHarf, 2)
            password[2:2] = random.sample(sayılar, 2)
            password[3:3] = random.sample(karakterler, 1)
            password = random.sample(password, 7)
            passwordStr = ''.join(password)
            return passwordStr
        elif(sayi == 8):
            password[0:0] = random.sample(büyükHarf, 2)
            password[1:1] = random.sample(kücükHarf, 2)
            password[2:2] = random.sample(sayılar, 2)
            password[3:3] = random.sample(karakterler, 2)
            password = random.sample(password, 8)
            passwordStr = ''.join(password)
            return passwordStr
        elif(sayi == 9):
            password[0:0] = random.sample(büyükHarf, 3)
            password[1:1] = random.sample(kücükHarf, 2)
            password[2:2] = random.sample(sayılar, 2)
            password[3:3] = random.sample(karakterler, 2)
            password = random.sample(password, 9)
            passwordStr = ''.join(password)
            return passwordStr
        elif(sayi == 10):
            password[0:0] = random.sample(büyükHarf, 3)
            password[1:1] = random.sample(kücükHarf, 3)
            password[2:2] = random.sample(sayılar, 2)
            password[3:3] = random.sample(karakterler, 2)
            password = random.sample(password, 10)
            passwordStr = ''.join(password)
            return passwordStr
        elif(sayi == 11):
            password[0:0] = random.sample(büyükHarf, 3)
            password[1:1] = random.sample(kücükHarf, 3)
            password[2:2] = random.sample(sayılar, 3)
            password[3:3] = random.sample(karakterler, 2)
            password = random.sample(password, 11)
            passwordStr = ''.join(password)
            return passwordStr
        elif(sayi == 12):
            password[0:0] = random.sample(büyükHarf, 3)
            password[1:1] = random.sample(kücükHarf, 3)
            password[2:2] = random.sample(sayılar, 3)
            password[3:3] = random.sample(karakterler, 3)
            password = random.sample(password, 12)
            passwordStr = ''.join(password)
            return passwordStr



    #Spinbox dan şifre boyutunu aldık
    def Range(self):
        spinRange = int(self.spinBox.value())
        return spinRange

    def CreatePassword(self):
        if(self.Range() <= 5):
            self.textEdit.setText("Daha uzun bir şifre uzunluğu seçiniz.")
        elif(self.Range() >= 13):
            self.textEdit.setText("Daha kısa bir şifre uzunluğu seçiniz.")
        elif(self.Range() == 6):
            self.textEdit.setText(self.Random(6))
        elif (self.Range() == 7):
            self.textEdit.setText(self.Random(7))
        elif (self.Range() == 8):
            self.textEdit.setText(self.Random(8))
        elif (self.Range() == 9):
            self.textEdit.setText(self.Random(9))
        elif (self.Range() == 10):
            self.textEdit.setText(self.Random(10))
        elif (self.Range() == 11):
            self.textEdit.setText(self.Random(11))
        elif (self.Range() == 12):
            self.textEdit.setText(self.Random(12))



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = WindowDesigner()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

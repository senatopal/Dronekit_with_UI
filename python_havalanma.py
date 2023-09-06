# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'havalanma.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_havalanma(object):
    def setupUi(self, havalanma):
        havalanma.setObjectName("havalanma")
        havalanma.resize(352, 474)
        havalanma.setStyleSheet("#centralwidget{\n"
"background-color: rgb(0, 0, 0);}")
        self.centralwidget = QtWidgets.QWidget(havalanma)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 110, 251, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 190, 121, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 290, 111, 25))
        self.pushButton.setObjectName("pushButton")
        havalanma.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(havalanma)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 22))
        self.menubar.setObjectName("menubar")
        havalanma.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(havalanma)
        self.statusbar.setObjectName("statusbar")
        havalanma.setStatusBar(self.statusbar)

        self.retranslateUi(havalanma)
        QtCore.QMetaObject.connectSlotsByName(havalanma)

    def retranslateUi(self, havalanma):
        _translate = QtCore.QCoreApplication.translate
        havalanma.setWindowTitle(_translate("havalanma", "MainWindow"))
        self.label.setText(_translate("havalanma", "Havalanma için yükseklik giriniz: "))
        self.pushButton.setText(_translate("havalanma", "Uygula"))

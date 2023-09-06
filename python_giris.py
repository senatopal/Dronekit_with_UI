# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(367, 522)
        MainWindow.setStyleSheet("#centralwidget{\n"
"background-color: rgb(0, 0, 0);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonKonum = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonKonum.setGeometry(QtCore.QRect(10, 310, 151, 41))
        self.pushButtonKonum.setObjectName("pushButtonKonum")
        self.pushButton_konumgit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_konumgit.setGeometry(QtCore.QRect(190, 310, 151, 41))
        self.pushButton_konumgit.setObjectName("pushButton_konumgit")
        self.pushButton_havalan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_havalan.setGeometry(QtCore.QRect(10, 250, 151, 41))
        self.pushButton_havalan.setObjectName("pushButton_havalan")
        self.pushButton_inis = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inis.setGeometry(QtCore.QRect(190, 250, 151, 41))
        self.pushButton_inis.setStyleSheet("")
        self.pushButton_inis.setObjectName("pushButton_inis")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 79, 271, 61))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 380, 171, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonKonum.setText(_translate("MainWindow", "Drone Konum Ver"))
        self.pushButton_konumgit.setText(_translate("MainWindow", "Drone Konuma Git"))
        self.pushButton_havalan.setText(_translate("MainWindow", "Drone Havalanma"))
        self.pushButton_inis.setText(_translate("MainWindow", "Drone İniş"))
        self.label.setText(_translate("MainWindow", "                  Bir Fonksiyon Seçiniz"))
        self.pushButton.setText(_translate("MainWindow", "Başlangıç Noktasına Git"))

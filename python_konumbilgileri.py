# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'konumbilgileri.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_konumbilgi(object):
    def setupUi(self, konumbilgi):
        konumbilgi.setObjectName("konumbilgi")
        konumbilgi.resize(333, 596)
        konumbilgi.setStyleSheet("#centralwidget{\n"
"background-color: rgb(0, 0, 0);}")
        self.centralwidget = QtWidgets.QWidget(konumbilgi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 90, 271, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.lineEdit_x = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x.setGeometry(QtCore.QRect(0, 140, 221, 25))
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 220, 271, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.lineEdit_y = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_y.setGeometry(QtCore.QRect(0, 270, 231, 25))
        self.lineEdit_y.setObjectName("lineEdit_y")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 370, 271, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setObjectName("label_3")
        self.lineEdit_z = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_z.setGeometry(QtCore.QRect(0, 420, 241, 25))
        self.lineEdit_z.setObjectName("lineEdit_z")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 480, 89, 25))
        self.pushButton.setObjectName("pushButton")
        konumbilgi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(konumbilgi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 22))
        self.menubar.setObjectName("menubar")
        konumbilgi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(konumbilgi)
        self.statusbar.setObjectName("statusbar")
        konumbilgi.setStatusBar(self.statusbar)

        self.retranslateUi(konumbilgi)
        QtCore.QMetaObject.connectSlotsByName(konumbilgi)

    def retranslateUi(self, konumbilgi):
        _translate = QtCore.QCoreApplication.translate
        konumbilgi.setWindowTitle(_translate("konumbilgi", "MainWindow"))
        self.label.setText(_translate("konumbilgi", "X ekseni konum bilgisini giriniz"))
        self.label_2.setText(_translate("konumbilgi", "Y ekseni konum bilgisini giriniz"))
        self.label_3.setText(_translate("konumbilgi", "Yükseklik bilgisini giriniz"))
        self.pushButton.setText(_translate("konumbilgi", "Uygula"))

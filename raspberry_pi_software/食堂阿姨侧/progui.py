# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 480)
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(QtCore.QRect(0, 0, 800, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bg.sizePolicy().hasHeightForWidth())
        self.bg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(24)
        self.bg.setFont(font)
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.exit = QtWidgets.QLabel(Dialog)
        self.exit.setGeometry(QtCore.QRect(580, 0, 221, 51))
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.l1 = QtWidgets.QLabel(Dialog)
        self.l1.setGeometry(QtCore.QRect(62, 367, 366, 81))
        self.l1.setText("")
        self.l1.setObjectName("l1")
        self.food = QtWidgets.QLabel(Dialog)
        self.food.setGeometry(QtCore.QRect(20, 290, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.food.setFont(font)
        self.food.setText("")
        self.food.setAlignment(QtCore.Qt.AlignCenter)
        self.food.setObjectName("food")
        self.jk1 = QtWidgets.QLabel(Dialog)
        self.jk1.setGeometry(QtCore.QRect(30, 160, 91, 81))
        self.jk1.setText("")
        self.jk1.setObjectName("jk1")
        self.l2 = QtWidgets.QLabel(Dialog)
        self.l2.setGeometry(QtCore.QRect(445, 180, 351, 291))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.l2.setFont(font)
        self.l2.setText("")
        self.l2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.l2.setObjectName("l2")
        self.jk2 = QtWidgets.QLabel(Dialog)
        self.jk2.setGeometry(QtCore.QRect(130, 160, 91, 81))
        self.jk2.setText("")
        self.jk2.setObjectName("jk2")
        self.jk3 = QtWidgets.QLabel(Dialog)
        self.jk3.setGeometry(QtCore.QRect(230, 160, 91, 81))
        self.jk3.setText("")
        self.jk3.setObjectName("jk3")
        self.jk4 = QtWidgets.QLabel(Dialog)
        self.jk4.setGeometry(QtCore.QRect(330, 160, 91, 81))
        self.jk4.setText("")
        self.jk4.setObjectName("jk4")
        self.foodbg = QtWidgets.QLabel(Dialog)
        self.foodbg.setGeometry(QtCore.QRect(20, 290, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.foodbg.setFont(font)
        self.foodbg.setText("")
        self.foodbg.setAlignment(QtCore.Qt.AlignCenter)
        self.foodbg.setObjectName("foodbg")
        self.bg.raise_()
        self.foodbg.raise_()
        self.exit.raise_()
        self.l1.raise_()
        self.food.raise_()
        self.jk1.raise_()
        self.l2.raise_()
        self.jk2.raise_()
        self.jk3.raise_()
        self.jk4.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

import img_rc

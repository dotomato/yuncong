# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
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
        self.result = QtWidgets.QLabel(Dialog)
        self.result.setGeometry(QtCore.QRect(370, 90, 431, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(24)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(400, 140, 407, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l1 = QtWidgets.QLabel(self.layoutWidget)
        self.l1.setText("")
        self.l1.setObjectName("l1")
        self.verticalLayout.addWidget(self.l1)
        self.l2 = QtWidgets.QLabel(self.layoutWidget)
        self.l2.setText("")
        self.l2.setObjectName("l2")
        self.verticalLayout.addWidget(self.l2)
        self.l3 = QtWidgets.QLabel(self.layoutWidget)
        self.l3.setText("")
        self.l3.setObjectName("l3")
        self.verticalLayout.addWidget(self.l3)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(560, 440, 241, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.exit = QtWidgets.QLabel(Dialog)
        self.exit.setGeometry(QtCore.QRect(580, 0, 221, 51))
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.l4 = QtWidgets.QLabel(Dialog)
        self.l4.setGeometry(QtCore.QRect(400, 400, 405, 56))
        self.l4.setText("")
        self.l4.setObjectName("l4")
        self.l5 = QtWidgets.QLabel(Dialog)
        self.l5.setGeometry(QtCore.QRect(400, 375, 405, 81))
        self.l5.setText("")
        self.l5.setObjectName("l5")
        self.lyy1 = QtWidgets.QLabel(Dialog)
        self.lyy1.setGeometry(QtCore.QRect(400, 100, 405, 71))
        self.lyy1.setText("")
        self.lyy1.setObjectName("lyy1")
        self.lyy2 = QtWidgets.QLabel(Dialog)
        self.lyy2.setGeometry(QtCore.QRect(400, 230, 405, 71))
        self.lyy2.setText("")
        self.lyy2.setObjectName("lyy2")
        self.bg.raise_()
        self.layoutWidget.raise_()
        self.result.raise_()
        self.label.raise_()
        self.exit.raise_()
        self.l4.raise_()
        self.l5.raise_()
        self.lyy1.raise_()
        self.lyy2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

import img_rc

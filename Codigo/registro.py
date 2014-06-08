# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registro.ui'
#
# Created: Sun Jun  8 12:53:07 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_registro(object):
    def setupUi(self, registro):
        registro.setObjectName("registro")
        registro.resize(373, 269)
        self.verticalLayoutWidget = QtGui.QWidget(registro)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 311, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txt_pass = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txt_pass.setObjectName("txt_pass")
        self.gridLayout.addWidget(self.txt_pass, 1, 1, 1, 1)
        self.txt_nombre = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txt_nombre.setToolTip("")
        self.txt_nombre.setObjectName("txt_nombre")
        self.gridLayout.addWidget(self.txt_nombre, 0, 1, 1, 1)
        self.label_nombre = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_nombre.setObjectName("label_nombre")
        self.gridLayout.addWidget(self.label_nombre, 0, 0, 1, 1)
        self.label_pass = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_pass.setObjectName("label_pass")
        self.gridLayout.addWidget(self.label_pass, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.btn_login = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout.addWidget(self.btn_login)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.boton_signin = QtGui.QPushButton(self.verticalLayoutWidget)
        self.boton_signin.setObjectName("boton_signin")
        self.verticalLayout.addWidget(self.boton_signin)
        spacerItem1 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(registro)
        QtCore.QMetaObject.connectSlotsByName(registro)

    def retranslateUi(self, registro):
        registro.setWindowTitle(QtGui.QApplication.translate("registro", "Registro", None, QtGui.QApplication.UnicodeUTF8))
        self.label_nombre.setText(QtGui.QApplication.translate("registro", "Nombre de Usuario :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pass.setText(QtGui.QApplication.translate("registro", "Contraseña :", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_login.setText(QtGui.QApplication.translate("registro", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_signin.setText(QtGui.QApplication.translate("registro", "Registrar una nueva cuenta", None, QtGui.QApplication.UnicodeUTF8))


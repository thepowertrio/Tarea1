# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created: Thu Jun  5 15:03:01 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Ventana(object):
    def setupUi(self, Ventana):
        Ventana.setObjectName("Ventana")
        Ventana.resize(556, 427)
        self.verticalLayoutWidget = QtGui.QWidget(Ventana)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 541, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_producto = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txt_producto.setText("")
        self.txt_producto.setObjectName("txt_producto")
        self.horizontalLayout.addWidget(self.txt_producto)
        self.label_marcas = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_marcas.setObjectName("label_marcas")
        self.horizontalLayout.addWidget(self.label_marcas)
        self.cbx_marcas = QtGui.QComboBox(self.verticalLayoutWidget)
        self.cbx_marcas.setObjectName("cbx_marcas")
        self.cbx_marcas.addItem("")
        self.cbx_marcas.addItem("")
        self.cbx_marcas.addItem("")
        self.cbx_marcas.addItem("")
        self.cbx_marcas.addItem("")
        self.cbx_marcas.addItem("")
        self.horizontalLayout.addWidget(self.cbx_marcas)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tvw_producto = QtGui.QTableView(self.verticalLayoutWidget)
        self.tvw_producto.setObjectName("tvw_producto")
        self.verticalLayout.addWidget(self.tvw_producto)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Ventana)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(220, 10, 326, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_nuevo = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_nuevo.setObjectName("btn_nuevo")
        self.horizontalLayout_2.addWidget(self.btn_nuevo)
        self.btn_editar = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_editar.setObjectName("btn_editar")
        self.horizontalLayout_2.addWidget(self.btn_editar)
        self.btn_eliminar = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout_2.addWidget(self.btn_eliminar)

        self.retranslateUi(Ventana)
        QtCore.QMetaObject.connectSlotsByName(Ventana)

    def retranslateUi(self, Ventana):
        Ventana.setWindowTitle(QtGui.QApplication.translate("Ventana", "Inventario de productos", None, QtGui.QApplication.UnicodeUTF8))
        self.txt_producto.setPlaceholderText(QtGui.QApplication.translate("Ventana", "¿Qué producto está buscando?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_marcas.setText(QtGui.QApplication.translate("Ventana", "Selecciona una marca :", None, QtGui.QApplication.UnicodeUTF8))
        #self.cbx_marcas.setCurrentText(QtGui.QApplication.translate("Ventana", "Todas", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_marcas.setItemText(0, QtGui.QApplication.translate("Ventana", "Todas", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_marcas.setItemText(1, QtGui.QApplication.translate("Ventana", "Apple", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_marcas.setItemText(2, QtGui.QApplication.translate("Ventana", "Microsoft", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_marcas.setItemText(3, QtGui.QApplication.translate("Ventana", "NIke", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_marcas.setItemText(4, QtGui.QApplication.translate("Ventana", "Reebok", None, QtGui.QApplication.UnicodeUTF8))
        self.cbx_marcas.setItemText(5, QtGui.QApplication.translate("Ventana", "Samsung", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_nuevo.setText(QtGui.QApplication.translate("Ventana", "Nuevo producto", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("Ventana", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("Ventana", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))


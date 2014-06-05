#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from ventana_principal import Ui_Ventana
import manejo_bd

class Display(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui =  Ui_Ventana()
        self.ui.setupUi(self)
        self.cargar_datos()

    def cargar_datos(self):
        productos = manejo_bd.obtener_tabla_productos()

        self.model = QtGui.QStandardItemModel(len(productos), 10)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"ID"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Codigo"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Atributos"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Descripcion"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Imagen"))
        self.model.setHorizontalHeaderItem(6, QtGui.QStandardItem(u"Color"))
        self.model.setHorizontalHeaderItem(7, QtGui.QStandardItem(u"Precio Bruto"))
        self.model.setHorizontalHeaderItem(8, QtGui.QStandardItem(u"Precio Neto"))
        self.model.setHorizontalHeaderItem(9, QtGui.QStandardItem(u"fk_id_marca"))

        r = 0
        for row in productos:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['id_producto'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['codigo'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['atributos'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['descripcion'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['Imagen'])
            index = self.model.index(r, 6, QtCore.QModelIndex())
            self.model.setData(index, row['color'])
            index = self.model.index(r, 7, QtCore.QModelIndex())
            self.model.setData(index, row['precio_bruto'])
            index = self.model.index(r, 8, QtCore.QModelIndex())
            self.model.setData(index, row['precio_neto'])
            index = self.model.index(r, 9, QtCore.QModelIndex())
            self.model.setData(index, row['fk_id_marca'])
            r = r+1
        self.ui.tableView.setModel(self.model)

        self.ui.tableView.setColumnWidth(0, 100)
        self.ui.tableView.setColumnWidth(1, 210)
        self.ui.tableView.setColumnWidth(2, 210)
        self.ui.tableView.setColumnWidth(3, 220)
        self.ui.tableView.setColumnWidth(4, 220)
        self.ui.tableView.setColumnWidth(5, 220)
        self.ui.tableView.setColumnWidth(6, 220)
        self.ui.tableView.setColumnWidth(7, 220)
        self.ui.tableView.setColumnWidth(8, 220)
        self.ui.tableView.setColumnWidth(9, 220)

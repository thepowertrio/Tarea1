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

        #self.model = QtGui.QStandardItemModel(len(productos), 10)
        self.model = QtGui.QStandardItemModel(len(productos)-1, 9)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"ID"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Codigo"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Atributos"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Descripcion"))
        #self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Imagen"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Color"))
        self.model.setHorizontalHeaderItem(6, QtGui.QStandardItem(u"Precio Bruto"))
        self.model.setHorizontalHeaderItem(7, QtGui.QStandardItem(u"Precio Neto"))
        self.model.setHorizontalHeaderItem(8, QtGui.QStandardItem(u"Marca"))

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
            #index = self.model.index(r, 5, QtCore.QModelIndex())
            #self.model.setData(index, row['Imagen'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['color'])
            index = self.model.index(r, 6, QtCore.QModelIndex())
            self.model.setData(index, row['precio_bruto'])
            index = self.model.index(r, 7, QtCore.QModelIndex())
            self.model.setData(index, row['precio_neto'])
            index = self.model.index(r, 8, QtCore.QModelIndex())
            #self.model.setData(index, row['fk_id_marca'])
            if(row['fk_id_marca'] == 1):
                self.model.setData(index, 'Nike')
            if(row['fk_id_marca'] == 2):
                self.model.setData(index, 'Apple')
            if(row['fk_id_marca'] == 3):
                self.model.setData(index, 'Samsung')
            if(row['fk_id_marca'] == 4):
                self.model.setData(index, 'Reebok')
            if(row['fk_id_marca'] == 5):
                self.model.setData(index, 'Microsoft')
            r = r+1
        self.ui.tvw_producto.setModel(self.model)

        self.ui.tvw_producto.setColumnWidth(0, 50)
        self.ui.tvw_producto.setColumnWidth(1, 65)
        self.ui.tvw_producto.setColumnWidth(2, 200)
        self.ui.tvw_producto.setColumnWidth(3, 150)
        self.ui.tvw_producto.setColumnWidth(4, 150)
        self.ui.tvw_producto.setColumnWidth(5, 100)
        self.ui.tvw_producto.setColumnWidth(6, 100)
        self.ui.tvw_producto.setColumnWidth(7, 100)
        self.ui.tvw_producto.setColumnWidth(8, 100)
        #self.ui.tvw_producto.setColumnWidth(9, 220)

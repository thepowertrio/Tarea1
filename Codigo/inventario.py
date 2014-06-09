#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from ventana_principal import Ui_Ventana
import manejo_bd
import form_producto

class Display(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui =  Ui_Ventana()
        self.ui.setupUi(self)
        self.iniciar_botones()
        #self.cargar_datos()
        self.cargar_datos("")

    def cargar_datos(self, text):
        #productos = manejo_bd.obtener_tabla_productos()

        #if (self.ui.cbx_marcas.currentIndex()==0):
        #    productos = manejo_bd.obtener_tabla_productos()
        #else:
        #    productos = manejo_bd.obtener_productos_marca(self.ui.cbx_marcas.currentIndex())

        if (self.ui.cbx_marcas.currentIndex()==0):
            if(text == ""):
                print "no hay texto productos"
                productos = manejo_bd.obtener_tabla_productos()
            else:
                print "hay texto productos"
                productos = manejo_bd.buscar_producto(text)
        else:
            if(text == ""):
                print "no hay texto marca"
                productos = manejo_bd.obtener_productos_marca(self.ui.cbx_marcas.currentIndex())
            else:
                print "hay texto marca"
                productos = manejo_bd.buscar_productos_marca(self.ui.cbx_marcas.currentIndex(),text)

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

    def eliminar_producto(self):
        model = self.ui.tvw_producto.model()
        index = self.ui.tvw_producto.currentIndex()
        if index.row() == -1: #No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            nombre = model.index(index.row(), 2, QtCore.QModelIndex()).data()
            if (manejo_bd.eliminar_producto(nombre)):
                #self.cargar_datos()
                msgBox = QtGui.QMessageBox()
                msgBox.setText("EL registro fue eliminado.")
                msgBox.exec_()
                self.cargar_datos()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
                return False

    def editar_producto(self):
        model = self.ui.tvw_producto.model()
        index = self.ui.tvw_producto.currentIndex()
        if index.row() == -1: #No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            nombre = model.index(index.row(), 2, QtCore.QModelIndex()).data()
            formulario = form_producto.Display(self)
            formulario.editar(nombre)
            formulario.exec_()
            self.cargar_datos("")

    def agregar_producto(self):
        formulario = form_producto.Display(self)
        formulario.exec_()
        self.cargar_datos("")

    def iniciar_botones(self):
        self.ui.btn_eliminar.clicked.connect(self.eliminar_producto)
        self.ui.btn_editar.clicked.connect(self.editar_producto)
        self.ui.cbx_marcas.activated[int].connect(self.cargar_datos)
        self.ui.txt_producto.textChanged[str].connect(self.cargar_datos)
        self.ui.btn_nuevo.clicked.connect(self.agregar_producto)
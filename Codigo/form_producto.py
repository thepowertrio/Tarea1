#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from nuevo_producto import Ui_Dialog
import manejo_bd

class Display(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Dialog()
        self.editado = False
        self.id_producto = ""
        self.imagen = ""
        self.ui.setupUi(self)
        self.iniciar_botones()

    def iniciar_botones(self):
        #self.ui.btn_img.clicked.connect(self.cambiar_imagen)
        self.ui.btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_cancg.clicked.connect(self.cancelar)

    def cancelar(self):
        self.reject()

    def guardar(self):
        if(self.editado):
            manejo_bd.editar_producto(unicode(self.ui.txt_codigo.text()),
                                        unicode(self.ui.txt_nom_prod.text()),
                                        unicode(self.ui.txt_atrib.text()),
                                        unicode(self.ui.txt_desc.text()),
                                        self.imagen,
                                        unicode(self.ui.txt_color.text()),
                                        unicode(self.ui.txt_pb.text()),
                                        unicode(self.ui.txt_pn.text()),
                                        unicode(self.ui.cbx_marca.currentIndex()+1),
                                        unicode(self.id_producto))
        else:
            manejo_bd.agregar_producto(unicode(self.ui.txt_codigo.text()),
                                        unicode(self.ui.txt_nom_prod.text()),
                                        unicode(self.ui.txt_atrib.text()),
                                        unicode(self.ui.txt_desc.text()),
                                        self.imagen,
                                        unicode(self.ui.txt_color.text()),
                                        unicode(self.ui.txt_pb.text()),
                                        unicode(self.ui.txt_pn.text()),
                                        unicode(self.ui.cbx_marca.currentIndex()+1),
                                        self.id_producto)
        self.reject()

    def editar(self, nombre):
        self.editado = True

        datos = manejo_bd.datos_producto(nombre)
        datos = datos[0]

        codigo = unicode(datos[1])
        nombre = unicode(datos[2])
        atrib = unicode(datos[3])
        desc = unicode(datos[4])
        color = unicode(datos[6])
        pb = unicode(datos[7])
        pn = unicode(datos[8])
        self.imagen = datos[5]
        self.id_producto = datos[0]

        self.ui.txt_codigo.setText(codigo)
        self.ui.txt_nom_prod.setText(nombre)
        self.ui.txt_atrib.setText(atrib)
        self.ui.txt_desc.setText(desc)
        self.ui.txt_color.setText(color)
        self.ui.txt_pb.setText(pb)
        self.ui.txt_pn.setText(pn)
        index = datos[9]
        self.ui.cbx_marca.setCurrentIndex(index-1)
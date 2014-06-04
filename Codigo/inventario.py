#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from ventana_principal import Ui_Ventana

class Display(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui =  Ui_Ventana()
        self.ui.setupUi(self)
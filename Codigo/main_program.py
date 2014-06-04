#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import inventario
from PySide import QtGui, QtCore

class Main(QtGui.QMainWindow):
	
	def __init__(self, parent = None):
		super(Main, self).__init__()
		mainwin = inventario.Display(self)
		mainwin.show()

def run():
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()




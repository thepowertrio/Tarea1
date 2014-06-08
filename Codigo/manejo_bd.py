#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from array import *

def conectar():
    #conecta base de datos
    con = sqlite3.connect('bd_principal.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_tabla_productos():
    #devuelve la tabla productos completa
    con = conectar()
    c = con.cursor()
    try:
        query = """SELECT * FROM productos"""
        resultado = c.execute(query)
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    prod = resultado.fetchall()
    con.close()
    return prod

def eliminar_producto(nom):
    #elimina un elemento de la tabla productos
    exito = False
    con = conectar()
    c = con.cursor()
    query = """DELETE FROM productos WHERE nombre = ?"""
    try:
        resultado = c.execute(query,[nom])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def buscar_producto(arg):
    #devuelve la tabla productos completa con el nombre arg.
    con = conectar()
    c = con.cursor()
    try:
        query = """SELECT * FROM procuctos WHERE nombre LIKE ?"""
        resultado = c.execute(query,["%"+arg+"%"])
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    prod = resultado.fetchall()
    con.close()
    return prod

def agregar_producto(cod,nom,atrib,desc,img,color,pb,pn,marca):
    #Agrega una fila en la tabla productos con los valores entregados.
    con = conectar()
    c = con.cursor()
    try:
        query = """INSERT INTO productos(codigo,
            nombre,atributos,descripcion,imagen,color,precio_bruto,
            precio_neto,fk_id_marca) VALUES (?,?,?,?,?,?,?,?,?)"""
        resultado = c.execute(query,[cod,nom,atrib,desc,img,color,pb,pn,marca])
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    index = c.fetchone()
    con.commit()
    con.close()
    return index

def editar_producto(cod,nom,atrib,desc,img,color,pb,pn,marca,id_prod):
    #Edita una fila en la tabla productos con los valores entregados.
    con = conectar()
    c = con.cursor()
    try:
        query = """UPDATE productos SET codigo = ?, nombre = ?, atributos = ?,
            descripcion = ?, imagen = ?, color = ?, precio_bruto = ?,
            precio_neto = ? WHERE id_producto = ?"""
        resultado = c.execute(query,[cod,nom,atrib,desc,img,color,pb,pn,marca,id_prod])
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    index = c.fetchone()
    con.commit()
    con.close()
    return True
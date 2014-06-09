#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from array import *

def conectar():
    """conecta base de datos"""
    con = sqlite3.connect('bd_principal.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_tabla_productos():
    """devuelve la tabla productos completa"""
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
    """elimina un elemento de la tabla productos"""
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

def buscar_producto(nom):
    """devuelve la tabla productos completa con el nombre nom."""
    con = conectar()
    c = con.cursor()
    try:
        query = """SELECT * FROM productos WHERE nombre LIKE ?"""
        resultado = c.execute(query,["%"+nom+"%"])
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    prod = resultado.fetchall()
    con.close()
    return prod

def agregar_producto(cod,nom,atrib,desc,img,color,pb,pn,marca):
    """Agrega una fila en la tabla productos con los valores entregados."""
    con = conectar()
    c = con.cursor()
    try:
        query = """INSERT INTO productos(codigo,
            nombre,atributos,descripcion,imagen,color,precio_bruto,
            precio_neto,fk_id_marca) VALUES (?,?,?,?,?,?,?,?,?)"""
        resultado = c.execute(query,[cod,nom,atrib,desc,img,color,pb,pn,marca])
        print "se agrego un producto"
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    index = c.fetchone()
    con.commit()
    con.close()
    return index

def editar_producto(cod,nom,atrib,desc,img,color,pb,pn,marca,id_prod):
    """Edita una fila en la tabla productos con los valores entregados."""
    con = conectar()
    c = con.cursor()
    try:
        query = """UPDATE productos SET codigo = ?, nombre = ?, atributos = ?,
            descripcion = ?, imagen = ?, color = ?, precio_bruto = ?,
            precio_neto = ?, fk_id_marca = ? WHERE id_producto = ?"""
        resultado = c.execute(query,[cod,nom,atrib,desc,img,color,pb,pn,marca,id_prod])
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    index = c.fetchone()
    con.commit()
    con.close()
    return True

def obtener_productos_marca(marca):
    """devuelve la tabla productos según la marca ingresada"""
    con = conectar()
    c = con.cursor()
    try:
        query = """SELECT * FROM productos WHERE fk_id_marca = ?"""
        resultado = c.execute(query,[marca])
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    prod = resultado.fetchall()
    con.close()
    return prod

def buscar_productos_marca(marca, nom):
    """devuelve la tabla productos según la marca ingresada con el nombre nom"""
    con = conectar()
    c = con.cursor()
    try:
        query = """SELECT * FROM productos WHERE fk_id_marca = ? AND nombre LIKE ?"""
        nombre = "%"+nom+"%"
        resultado = c.execute(query,[marca,nombre])
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    prod = resultado.fetchall()
    con.close()
    return prod

def datos_producto(name):
    """Obtiene la fila de nombre "name" en la tabla productos."""
    con = conectar()
    c = con.cursor()
    try:
        query = """SELECT * FROM productos WHERE nombre=?"""
        resultado = c.execute(query,[name])
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    prod = resultado.fetchall()
    con.close()
    return prod
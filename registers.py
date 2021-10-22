from flask import Flask, render_template, request, url_for, flash, redirect, Request
import yagmail
import utils
import os
import random
import sqlite3
from sqlite3 import Error
from datetime import date

# En tu programa que utiliza el paquete package
#from settings import create_connection
from settings import config
from settings.config import create_connection
from forms import formRegister


from markupsafe import escape #Cambia lo ingresado en el formulario a texto
import hashlib #Criptografia
from werkzeug.security import generate_password_hash 
from werkzeug.security import check_password_hash

class register():

    def __init__(self,usuario, correo,hashclave,is_active,created_at,id_type):
        self.usuario=usuario
        self.correo=correo
        self.hashclave=hashclave
        self.is_active=is_active
        self.created_at=created_at
        self.id_type=id_type

    def get_usuario(self):
        return self.usuario
    def get_correo(self):
        return self.correo
    def get_hashclave(self):
        return self.hashclave
    def get_is_active(self):
        return self.is_active
    def get_created_at(self):
        return self.created_at
    def get_id_type(self):
        return self.id_type       

def sql_insert_user(usuario, correo,hashclave,is_active,created_at,id_type):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                cur = con.cursor()                                
                cur.execute("INSERT INTO user (username,email, password,is_active, created_at,id_type) VALUES(?,?,?,?,?,?) ", (usuario, correo,hashclave,is_active,created_at,id_type))
                con.commit
            except Error:
                con.rollback()

def sql_get_user(usuario):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()                                
                cur.execute("SELECT username FROM user WHERE username = ?", [usuario])
                row = cur.fetchone()
                if row is None:
                    flash("Usuario no se encuentra en la BD.")
                    return False
                else:
                    return True    
            except Error:
                print(Error)

def sql_get_email(correo):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()                                
                cur.execute("SELECT email FROM user WHERE email = ?", [correo])
                row = cur.fetchone()
                if row is None:
                    flash("El correo no se encuentra en la BD.")
                    return False
                else:
                    return True    
            except Error:
                print(Error)  

def sql_get_user_info(usuario):

        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()                                
                cur.execute("SELECT * FROM user WHERE username = ?", [usuario])
                row = cur.fetchone()
                if row is None:
                    flash("El usuario no se encuentra en la BD.")
                    return row
                else:
                    return row    
            except Error:
                print(Error)      


def sql_update_user_profile(usuario,nombre, apellido, correo,hashclave,bd,genero, como):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                cur = con.cursor()                                
                #cur.execute("INSERT INTO user (name, lastname,email, password,bd, gender,likes) VALUES(?,?,?,?,?,?,?) ", (nombre, apellido, correo,hashclave,bd,genero,como))
                #cur.execute("UPDATE Estudiantes SET nombre=?, ciclo=?, sexo=?, estado=? WHERE documento=?", [nombre, ciclo, sexo, estado, documento])
                cur.execute("UPDATE user SET name=?, lastname=?, email=?, password=?, bd=?, gender=?, likes=? WHERE username=?", [nombre, apellido, correo, hashclave, bd, genero, como, usuario])
                con.commit
                if con.total_changes > 0:
                    flash("Usuario editado con Exito")  
                else:
                    flash("Error en el proceso de edición")                  
            except Error:
                con.rollback()            



   
def sql_get_email_profile(usuario,correo):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()                                
                cur.execute("SELECT email FROM user WHERE email = ? and username <> ? ", [correo, usuario])
                row = cur.fetchone()
                if row is None:
                    #flash("El correo se puede actualizar en la BD.")
                    return True
                else:
                    flash("El correo ya esta asociado a otro usuario en la BD.")
                    return False   
            except Error:
                print(Error)              
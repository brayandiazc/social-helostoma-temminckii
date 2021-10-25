from flask import Flask, render_template, request, url_for, flash, redirect, Request,session
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


def sql_get_email_login(correo):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()                                
                cur.execute("SELECT * FROM user WHERE email = ?", [correo])
                row = cur.fetchone()
                if row is None:
                    flash("El correo no se encuentra en la BD. Favor Registrate.")
                    return False
                else:
                    return True    
            except Error:
                print(Error)  

def sql_get_user_info_login(correo):

        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()                                
                cur.execute("SELECT * FROM user WHERE email = ?", [correo])
                row = cur.fetchone()
                if row is None:
                    flash("El correo no se encuentra en la BD.")
                    return row
                else:
                    return row    
            except Error:
                print(Error)                   

def sql_get_pwd_login(correo, clave):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()                                
                cur.execute("SELECT password FROM user WHERE email = ?", [correo])
                row = cur.fetchone()

                if row!=None:
                    hashclave=row[0] # trae una lista...ojo...

                    print(clave)  
                    print(row[0])  
                    if check_password_hash(hashclave,clave):
                        print("Entro al check")
                        print(row[0])
                        return True
                    else:
                        flash("Contraseña incorrecta" )
                        print("Entro al false")
                        print(row[0])                        
                        return False
                else:
                    flash("Usuario no existe"      )
                    return False
            except Error:
                print(Error)        
        
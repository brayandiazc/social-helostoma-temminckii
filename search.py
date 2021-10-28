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


from markupsafe import escape                        #Cambia lo ingresado en el formulario a texto
import hashlib #Criptografia
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

def sql_get_user_search(usuario):

        conn =create_connection("helostoma.db")
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()
                #my_data=str([usuario])
                my_data=('%'+usuario+'%',)
                print(my_data)
                cur.execute("SELECT * FROM view_user_find WHERE NAME_COMPLETE LIKE ?",my_data )
                row = cur.fetchall()
                return row
            except Error:
                print(Error)

def sql_get_user_search_all():

        conn =create_connection("helostoma.db")
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()
                cur.execute("SELECT * FROM view_user_find WHERE IS_ACTIVE=1")
                row = cur.fetchall()
                return row
            except Error:
                print(Error)
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


def sql_insert_post(usuario_id, titulo,contenido,estado,creado):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                cur = con.cursor()                                
                cur.execute("INSERT INTO post (author_ref_id,title, content,is_active, created_at) VALUES(?,?,?,?,?) ", (usuario_id, titulo,contenido,estado,creado))
                con.commit
            except Error:
                con.rollback()

def sql_insert_img(usuario_id, fuente,titulo,contenido,creado):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                cur = con.cursor()                                
                cur.execute("INSERT INTO image (user_id,src, title,content, created_at) VALUES(?,?,?,?,?) ", (usuario_id, fuente,titulo,contenido,creado))
                con.commit
            except Error:
                con.rollback()

def sql_insert_postimg(post_id, image_id):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                cur = con.cursor()                                
                cur.execute("INSERT INTO post_image (post_id,image_id) VALUES(?,?) ", (post_id, image_id))
                con.commit
            except Error:
                con.rollback()

def sql_get_post_id(usuario_id):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()                                
                cur.execute("SELECT MAX(ID) AS ID_MAX FROM POST WHERE author_ref_id = ?", [usuario_id])
                row = cur.fetchone()
                print(row)
                return row
            except Error:
                print(Error)

def sql_get_image_id(usuario_id):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()                                
                cur.execute("SELECT MAX(ID) AS ID_MAX FROM IMAGE WHERE user_id = ?", [usuario_id])
                row = cur.fetchone()
                print(row)
                return row
            except Error:
                print(Error)

def sql_get_post_detail(post_id):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()                                
                cur.execute("SELECT * FROM VIEW_USER_POST WHERE POST_ID = ?", [post_id])
                row = cur.fetchone()
                print(row)
                return row
            except Error:
                print(Error)                

def sql_get_comment_detail(post_id):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()                                
                cur.execute("SELECT * FROM VIEW_POST_COMMENT WHERE POST_ID = ? AND IS_ACTIVE=1", [post_id])
                row = cur.fetchall()
                print(row)
                return row
            except Error:
                print(Error)                   

def sql_insert_comment(usuario_id, id_publicacion,contenido,creado, estado):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                cur = con.cursor()                                
                cur.execute("INSERT INTO comment (user_id,ref_id, content, created_at, is_active) VALUES(?,?,?,?,?) ", (usuario_id, id_publicacion,contenido,creado, estado))
                con.commit
            except Error:
                con.rollback()

#------------------------------------------------
def sql_get_post_search(usuario_id):
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()        
                #my_data=str([publicacion])
                # my_data=('%'+publicacion+'%',) 
                # print(my_data)
                cur.execute("SELECT * FROM view_user_post WHERE USER_ID= ?",[usuario_id] )
                row = cur.fetchall()
                return row
            except Error:
                print(Error)  

def sql_get_post_search_all():
        
        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()        
                cur.execute("SELECT * FROM view_user_post WHERE IS_ACTIVE=1")
                row = cur.fetchall()
                return row
            except Error:
                print(Error)                  

def sql_get_user_info_login_post(usuario_id):

        conn =create_connection("helostoma.db") 
        with conn as con:
            try:
                con.row_factory=sqlite3.Row
                cur = con.cursor()                                
                cur.execute("SELECT * FROM view_user_find WHERE id = ?", [usuario_id])
                row = cur.fetchone()
                if row is None:
                    flash("El usuario no se encuentra en la BD.")
                    return row
                else:
                    return row    
            except Error:
                print(Error)                 
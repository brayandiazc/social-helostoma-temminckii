from flask import Flask, render_template, request, url_for, flash, redirect, Request, session
from settings import config
import utils
import os
import random
import sqlite3
from sqlite3 import Error
from datetime import date

# En tu programa que utiliza el paquete package
#from settings import create_connection
from settings.config import create_connection
from forms import formEditProfile, formRegister, formLogin, formSearch
from registers import * #register, sql_insert_user,sql_get_user
from login import *
from search import*


from markupsafe import escape #Cambia lo ingresado en el formulario a texto

import hashlib #Criptografia
from werkzeug.security import generate_password_hash 
from werkzeug.security import check_password_hash




app = Flask(__name__)
app.secret_key = os.urandom(24)

#Se crea una lista de usuarios para el tema de logica algoritmica simple.
usuarios_sistema=["Brayan","Fernando","Sergio","Geovanny","Jairo"]


#Se crea un diccionario de usuarios reuniniendo los requisitos del sistema by Geo
    # ID:{'user':"string",'fullname': "string",'birth':['dia', 'mes', 'año'],'email': "string",'genre':"string",'tipo': "string"}
lista_usuarios={
    101:{'user':"Brayan",'full_name':"Brayan Díaz",'birth':['03','12','1980'],'email':"brayan@gmail.com",'genre':"Masculino",'tipo':"super_admin"},
    102:{'user':"Fernando",'full_name':"Fernando Sandoval",'birth':['04','11','1999'],'email':"fernando@gmail.com",'genre':"Masculino",'tipo':"usuario"},
    103:{'user':"Sergio",'full_name':"Sergio Balcazar",'birth':['05','10','1980'],'email':"sergio@gmail.com",'genre':"Masculino",'tipo':"usuario"},
    104:{'user':"Geovanny",'full_name':"Geovanny Rambauth",'birth':['06','09','2000'],'email':"geovanny@gmail.com",'genre':"Masculino",'tipo':"usuario"},
    105:{'user':"Jairo",'full_name':"Jairo Viñas",'birth':['07','08','1989'],'email':"jairo@gmail.com",'genre':"Masculino",'tipo':"admin"},
    106:{'user':"Shary",'full_name':"Shary Tutora",'birth':['08','06','1999'],'email':"shary@gmail.com",'genre':"Masculino",'tipo':"usuario"},
}

#print(lista_usuarios[101])
#print(lista_usuarios[random.randint(101,106)])
#Se crea un dicicionario de publicaciones con la finalidad de validar la algoritmica simple
lista_publicaciones={
    123:{'titulo':"publicaciones #1",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    124:{'titulo':"publicaciones #2",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    125:{'titulo':"publicaciones #3",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    126:{'titulo':"publicaciones #4",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    127:{'titulo':"publicaciones #5",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    128:{'titulo':"publicaciones #6",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    129:{'titulo':"publicaciones #7",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    130:{'titulo':"publicaciones #8",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    131:{'titulo':"publicaciones #9",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
}

lista__publicaciones={
    2001:{'titulo':"Publicación hecha por: " + usuarios_sistema[0],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #1",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2002:{'titulo':"Publicación hecha por: " + usuarios_sistema[1],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #2",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2003:{'titulo':"Publicación hecha por: " + usuarios_sistema[2],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #3",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2004:{'titulo':"Publicación hecha por: " + usuarios_sistema[3],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #4",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2005:{'titulo':"Publicación hecha por: " + usuarios_sistema[4],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #5",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2006:{'titulo':"Publicación hecha por: " + usuarios_sistema[0],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #6",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2007:{'titulo':"Publicación hecha por: " + usuarios_sistema[1],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #7",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2008:{'titulo':"Publicación hecha por: " + usuarios_sistema[2],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #8",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2009:{'titulo':"Publicación hecha por: " + usuarios_sistema[3],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #9",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,1,1,1,1]},
    2010:{'titulo':"Publicación hecha por: " + usuarios_sistema[4],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #10",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,0,0,0]},
    2011:{'titulo':"Publicación hecha por: " + usuarios_sistema[0],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #11",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2012:{'titulo':"Publicación hecha por: " + usuarios_sistema[4],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #12",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2013:{'titulo':"Publicación hecha por: " + usuarios_sistema[2],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #13",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2014:{'titulo':"Publicación hecha por: " + usuarios_sistema[1],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #14",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2015:{'titulo':"Publicación hecha por: " + usuarios_sistema[3],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #15",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2016:{'titulo':"Publicación hecha por: " + usuarios_sistema[0],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #16",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2017:{'titulo':"Publicación hecha por: " + usuarios_sistema[4],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #17",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2018:{'titulo':"Publicación hecha por: " + usuarios_sistema[2],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #18",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2019:{'titulo':"Publicación hecha por: " + usuarios_sistema[3],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #19",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2020:{'titulo':"Publicación hecha por: " + usuarios_sistema[1],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #20",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2021:{'titulo':"Publicación hecha por: " + usuarios_sistema[0],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #21",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2022:{'titulo':"Publicación hecha por: " + usuarios_sistema[1],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #22",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2023:{'titulo':"Publicación hecha por: " + usuarios_sistema[2],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #23",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2024:{'titulo':"Publicación hecha por: " + usuarios_sistema[3],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #24",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2025:{'titulo':"Publicación hecha por: " + usuarios_sistema[4],'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #25",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]}
    
}

#print(lista__publicaciones)
#Se crea un dicicionario de publicaciones con la finalidad de validar la algoritmica simple
lista_mensaje={
    223:{'mensaje':"Mensaje #1",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    223:{'mensaje':"Mensaje #1",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    224:{'mensaje':"Mensaje #2",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    224:{'mensaje':"Mensaje #2",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    225:{'mensaje':"Mensaje #3",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    225:{'mensaje':"Mensaje #3",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    226:{'mensaje':"Mensaje #4",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    226:{'mensaje':"Mensaje #4",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    227:{'mensaje':"Mensaje #5",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    227:{'mensaje':"Mensaje #5",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    228:{'mensaje':"Mensaje #6",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    228:{'mensaje':"Mensaje #6",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    229:{'mensaje':"Mensaje #7",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    230:{'mensaje':"Mensaje #8",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    231:{'mensaje':"Mensaje #9",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
}

# Se crea esta variable para probar el inicio de sesion.
sesion_iniciada=False
sesion_usuario=''

# Ruta Raiz ----------------------
@app.route("/", methods=["GET"])

# Index ----------------------
@app.route("/index", methods=["GET"])
def index():
    #Si ya inicio Sesion ->Lista de publicaciones Feed.
    #Sino -> Bienvenida
    #return render_template("register.html")
    return render_template("index.html", sesion_iniciada=sesion_iniciada)

# Ingreso ----------------------
@app.route("/ingreso",methods=["GET","POST"])
def ingreso():
    global sesion_iniciada
    global sesion_usuario

    form = formLogin()
    return render_template("login.html", form=form)    


'''    if request.method=="GET":
        return render_template("login.html")
    else:
        email=request.form["email"]

        for key, usuarios in lista_usuarios.items():
            #print(usuarios["email"])
            if email==usuarios["email"]:
                sesion_iniciada=True
                sesion_usuario='javinas'
                return redirect('/publicaciones')
                break
        cadena=f"Error, el email {email} no exite en la base de datos"
        return render_template('login.html',cadena=cadena)
'''

@app.route("/ingreso/get",methods=["POST"])
def ingreso_get():
    global sesion_iniciada
    global sesion_usuario
    form = formLogin()
    if request.method == "POST":
        correo=escape(form.correo.data)
        clave=escape(form.clave.data)
        if (sql_get_email_login(correo)==True):
            try:    
                row_info=sql_get_user_info_login(correo)
                usuario=row_info["username"]
                nombre=row_info["name"]
                apellido=row_info["lastname"]
                tipo=row_info["id_type"]                
                if (sql_get_pwd_login(correo, clave)==True):
                    print(row_info["username"])
                    session["user"]=usuario
                    session["id_type"]=tipo
                    session["name"]=nombre
                    session["lastname"]=apellido  
                    sesion_iniciada=True

                    form=formLogin()
                    flash(f'Ingreso de sesion de {usuario}')
                    return redirect('/publicaciones')   
                else:
                   return render_template("login.html", form=form)                       
            except Error:
                print(os.error)
        else:
            flash("Usuario no registrado en la aplicación")
            return render_template("login.html", form=form)               


# Salir ----------------------
@app.route("/salir")
def salir():
    global sesion_iniciada
    sesion_iniciada=False
    session.pop("user", None)
    session.clear
    return redirect('/index')

# Perfil ----------------------
@app.route("/perfil",methods=["GET","POST"])
def perfil():
        return render_template("perfil.html", sesion_iniciada=sesion_iniciada,lista_publicaciones=lista__publicaciones)

@app.route("/perfil_edit",methods=["GET","POST"])
def perfil_edit():
    form=formEditProfile()
    #row_info=sql_get_user_info(sesion_usuario)
    row_info=sql_get_user_info(session["user"])
    print(row_info)
    return render_template("perfil_edit.html", sesion_iniciada=sesion_iniciada,form=form, sesion_usuario=sesion_usuario, row_info=row_info)

@app.route("/perfil_edit/save",methods=["GET","POST"])
def perfil_edit_save():
    form=formEditProfile()
    #row_info=sql_get_user_info(sesion_usuario)
    row_info=sql_get_user_info(session["user"])    
    print(row_info)
   
    if request.method == "POST":
        usuario=escape(form.usuario.data)
        nombre=escape(form.nombre.data)  
        apellido=escape(form.apellido.data)      
        correo=escape(form.correo.data)
        clave=escape(form.clave.data)
        bd=escape(form.bd.data)
        genero=escape(form.genero.data)
        como=escape(form.como.data)        
        hashclave=generate_password_hash(clave) #se genera el hash + salt critografia.

        try:
       

            if (sql_get_email_profile(usuario,correo)==True):
                    #metodo para hacer insert a la base de datos. Se encuentra en la clase register.py
                    sql_update_user_profile(usuario,nombre, apellido, correo,hashclave,bd,genero, como)
                    #flash("Usuario editado con Exito")
                    row_info=sql_get_user_info(session["user"]) 
                    return render_template("perfil_edit.html", sesion_iniciada=sesion_iniciada, sesion_usuario=sesion_usuario,form=form,row_info=row_info)   
            else:
                    flash("Correo ya esta asociado a otro usuario en la Base de datos.")
                    row_info=sql_get_user_info(session["user"]) 
                    return render_template("perfil_edit.html", sesion_iniciada=sesion_iniciada, sesion_usuario=sesion_usuario,form=form,row_info=row_info)                    
        
        except Error:
            row_info=sql_get_user_info(session["user"]) 
            return render_template("perfil_edit.html", sesion_iniciada=sesion_iniciada, sesion_usuario=sesion_usuario,form=form,row_info=row_info)  
        #Metodo de envio de correo.    

    row_info=sql_get_user_info(session["user"]) 
    return render_template("perfil_edit.html", sesion_iniciada=sesion_iniciada, sesion_usuario=sesion_usuario,form=form,row_info=row_info)  

# Perfil usuarios ---------------------------
@app.route("/usuario/<id_usuario>",methods=["GET"])
def usuario_informacion(id_usuario):
    #validacion simple de usuario ..............................................
    id_usuario=int(id_usuario)
    if id_usuario in lista_usuarios:
        return f"Pagina del Perfil del usuario {id_usuario}"    #validacion simple de usuario
    else:
        return f"Error, el usuario {id_usuario} no exite en la base de datos"

# Perfil admin  ..............
@app.route("/admin/<id_admin>",methods=["GET","POST"])
def admin_informacion(id_admin):
    id_admin=int(id_admin)
    if id_admin in lista_usuarios:
        #return f"Pagina del Perfil del usuario Admin {id_admin}"   #validacion simple de Perfil admin
        return render_template("dashboard.html", sesion_iniciada=sesion_iniciada,lista_usuarios=lista_usuarios, id_admin=id_admin)
    else:
        return f"Error, el usuario {id_admin} no exite en la base de datos"

# Perfil superadmin ............
@app.route("/superadmin/<id_superadmin>",methods=["GET"])
def superadmin_informacion(id_superadmin):
    if id_superadmin in usuarios_sistema:
        return f"Pagina del Perfil del usuario Superadmin {id_superadmin}"  #validacion simple de Perfil superadmin
    else:
        return f"Error, el usuario {id_superadmin} no exite en la base de datos"

# Publicacion nueva --------------
@app.route("/publicacion_new",methods=["GET","POST"])
def publicacion_new():
    global sesion_iniciada
    return render_template("publicacion_new.html", sesion_iniciada=sesion_iniciada)

# Publicaciones --------------
@app.route("/publicaciones",methods=["GET","POST"])
def publicacion():
    global sesion_iniciada
    #return "Pagina de todas las publicaciones"  #publicaciones.html .....................
    return render_template("publicaciones.html", sesion_iniciada=sesion_iniciada,lista_publicaciones=lista__publicaciones)

# Detalle de las publicaciones -----------
@app.route("/detalle_pub/<id_publicacion>",methods=["GET","POST"])
def detalle_pub(id_publicacion):
    try:
        id_publicacion=int(id_publicacion)
    except Exception as e:
        id_publicacion=0

    if id_publicacion in lista__publicaciones:
        #return lista__publicaciones[id_publicacion]
        return render_template("publicacion.html", sesion_iniciada=sesion_iniciada,lista_publicaciones=lista__publicaciones, id_publicacion=id_publicacion)
    else:
        return f"Error, la publicacion {id_publicacion} no exite en la base de datos"
        #return f"Pagina detalle de la publicacion {id_publicacion}"  #detalla_pub.html

# Busqueda de usuario ---------------------------
@app.route("/busqueda/",methods=["GET"])
def busqueda():
    form=formSearch()
    if "user" in session:   
        row_info=sql_get_user_search_all()    
        for row in row_info:
            print(row["username"])

        return render_template("busqueda.html", sesion_iniciada=sesion_iniciada,form=form, row_info=row_info)  
        #return render_template("busqueda.html", sesion_iniciada=sesion_iniciada,form=form)
    else:
        flash("El usuario debe iniciar sesión.")
        return render_template("index.html", sesion_iniciada=sesion_iniciada)

# Busqueda de usuario ---------------------------
@app.route("/busqueda/get",methods=["GET","POST"])
def busqueda_get():

    form=formSearch()
    data_search=escape(form.usuario.data)

    if "user" in session:  
        row_info=sql_get_user_search(data_search)
        if row_info is None:
           #return "Elemento no encontrado" 
           return render_template("busqueda.html", sesion_iniciada=sesion_iniciada,form=form, row_info=row_info)    
        else:
            #return "Exito en Busqueda"
            return render_template("busqueda.html", sesion_iniciada=sesion_iniciada,form=form, row_info=row_info)   
    else:
        flash("El usuario debe iniciar sesión.")
        return render_template("index.html", sesion_iniciada=sesion_iniciada)    


        #return render_template("busqueda.html", sesion_iniciada=sesion_iniciada,lista_publicaciones=lista__publicaciones)



# Busqueda de usuario ---------------------------
@app.route("/busqueda/<id_usuario>",methods=["GET","POST"])
def busqueda_usuario(id_usuario):
    id_usuario=int(id_usuario)
    if id_usuario in lista_usuarios:
        #return f"El usuario que buscas Existe: {id_usuario}, en la Base de Datos."
        return render_template("busqueda.html", sesion_iniciada=sesion_iniciada,lista_usuarios=lista_usuarios, id_usuario=id_usuario,lista_publicaciones=lista__publicaciones)
    else:
        return f"El usuario que buscas no existe: {id_usuario}"

# Mensajes ---------------------
@app.route("/msg",methods=["GET"])
def msg():
    global sesion_iniciada
    #return f"Pagina de Mensajes"  #msg.html
    return render_template("mensajes.html", sesion_iniciada=sesion_iniciada,lista_mensaje=lista_mensaje)

# Mensajes privados --------------
@app.route("/msg_privado/<id_msg>",methods=["GET","POST"])
def msg_privado(id_msg):
    try:
        id_msg=int(id_msg)
    except Exception as e:
        id_publicacion=0

    if id_msg in lista_mensaje:
        return lista_mensaje[id_msg]
    else:
        return f"Error, el mensaje {id_msg} no exite en la base de datos"
    #return f"Pagina - Mensaje privado : {id_msg}"  #msg_privado.html

# Registrar ---------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    form = formRegister()
    return render_template("register.html", form=form)

@app.route('/register/save', methods=["POST"]) #Ruta para guardar claves
def encriptar():
    form=formRegister()
    if request.method == "POST":
        usuario=escape(form.usuario.data)
        correo=escape(form.correo.data)
        clave=escape(form.clave.data)
        clave1=escape(form.clave1.data)
        estado=escape(form.estado.data)
        hashclave=generate_password_hash(clave) #se genera el hash + salt critografia.
        is_active=1
        created_at=date.today()
        id_type=1

        if (clave !=clave1):
            error="Password no coincide"
            flash(error)
            return render_template("register.html", form=form)
            #Registro en la base de datos.   
            #  
        try:

            if (sql_get_user(usuario)==False):
                if (sql_get_email(correo)==False):
                    #metodo para hacer insert a la base de datos. Se encuentra en la clase register.py
                    sql_insert_user(usuario, correo,hashclave,is_active,created_at,id_type)
                    flash("usuario registrado con Exito")
                    #return render_template("/ingreso")   
                    return redirect('/ingreso')   
                else:
                    flash("Correo ya esta registrado en la Base de datos.")
                    return render_template("register.html", form=form)                    
            else:
                flash("usuario ya esta registrado en la Base de datos.")
                return render_template("register.html", form=form) 

        except Error:
            return render_template("register.html", form=form) 
        #Metodo de envio de correo.             
    return "No metodo POST"

if __name__=='__main__':
    app.run(debug=True, port=8081)
    
    

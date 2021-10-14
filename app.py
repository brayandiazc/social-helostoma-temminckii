from flask import Flask, render_template, request, url_for, flash, redirect, Request
import yagmail
import utils
import os
import random

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
    2001:{'titulo':"Publicación hecha por: usuario 101",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #1",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2002:{'titulo':"Publicación hecha por: usuario 102",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #2",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2003:{'titulo':"Publicación hecha por: usuario 103",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #3",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2004:{'titulo':"Publicación hecha por: usuario 104",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #4",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2005:{'titulo':"Publicación hecha por: usuario 105",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #5",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2006:{'titulo':"Publicación hecha por: usuario 101",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #6",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2007:{'titulo':"Publicación hecha por: usuario 102",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #7",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2008:{'titulo':"Publicación hecha por: usuario 103",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #8",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2009:{'titulo':"Publicación hecha por: usuario 104",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #9",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,1,1,1,1]},
    2010:{'titulo':"Publicación hecha por: usuario 105",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #10",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,0,0,0]},
    2011:{'titulo':"Publicación hecha por: usuario 101",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #11",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2012:{'titulo':"Publicación hecha por: usuario 102",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #12",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2013:{'titulo':"Publicación hecha por: usuario 103",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #13",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2014:{'titulo':"Publicación hecha por: usuario 104",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #14",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2015:{'titulo':"Publicación hecha por: usuario 105",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #15",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2016:{'titulo':"Publicación hecha por: usuario 101",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #16",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2017:{'titulo':"Publicación hecha por: usuario 102",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #17",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2018:{'titulo':"Publicación hecha por: usuario 103",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #18",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2019:{'titulo':"Publicación hecha por: usuario 104",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #19",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2020:{'titulo':"Publicación hecha por: usuario 105",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #20",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2021:{'titulo':"Publicación hecha por: usuario 101",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #21",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2022:{'titulo':"Publicación hecha por: usuario 102",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #22",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2023:{'titulo':"Publicación hecha por: usuario 103",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #23",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2024:{'titulo':"Publicación hecha por: usuario 104",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #24",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2025:{'titulo':"Publicación hecha por: usuario 105",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #25",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2026:{'titulo':"Publicación hecha por: usuario 101",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #26",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2027:{'titulo':"Publicación hecha por: usuario 102",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #27",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2028:{'titulo':"Publicación hecha por: usuario 103",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #28",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2029:{'titulo':"Publicación hecha por: usuario 104",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #29",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2030:{'titulo':"Publicación hecha por: usuario 105",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #30",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2031:{'titulo':"Publicación hecha por: usuario 101",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #31",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2032:{'titulo':"Publicación hecha por: usuario 102",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #32",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2033:{'titulo':"Publicación hecha por: usuario 103",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #33",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2034:{'titulo':"Publicación hecha por: usuario 104",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #34",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2035:{'titulo':"Publicación hecha por: usuario 105",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #35",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2036:{'titulo':"Publicación hecha por: usuario 101",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #36",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2037:{'titulo':"Publicación hecha por: usuario 102",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #37",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2038:{'titulo':"Publicación hecha por: usuario 103",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #38",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2039:{'titulo':"Publicación hecha por: usuario 104",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #39",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2040:{'titulo':"Publicación hecha por: usuario 105",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #40",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2041:{'titulo':"Publicación hecha por: usuario 101",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #41",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2042:{'titulo':"Publicación hecha por: usuario 102",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #42",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2043:{'titulo':"Publicación hecha por: usuario 103",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #43",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2044:{'titulo':"Publicación hecha por: usuario 104",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #44",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2045:{'titulo':"Publicación hecha por: usuario 105",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #45",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2046:{'titulo':"Publicación hecha por: usuario 101",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #46",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2047:{'titulo':"Publicación hecha por: usuario 102",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #47",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2048:{'titulo':"Publicación hecha por: usuario 103",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #48",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2049:{'titulo':"Publicación hecha por: usuario 104",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #49",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
    2050:{'titulo':"Publicación hecha por: usuario 105",'contenido':"La idea aquí es hacer publicaciones comparando tu producto o servicio con la competencia en el mercado.  Por ejemplo, en un asunto que aquí nos compete en nuestro blog, sería hacer el comparativo entre el marketing de contenidos y la publicidad. No obstante, para que este tipo de contenidos gane relevancia, a veces es interesante que presentes algunos casos en los que tu producto NO es la mejor opción. #50",'fecha_inicio':"datetimeinicio",'fecha_final':"datetimefin",'id_usuario':"101",'img_id':"idimagen",'estado':"0",'calificacion_id':[1,0,1,1,0]},
}

print(lista__publicaciones)
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
    if request.method=="GET":
        return render_template("login.html")
    else:
        email=request.form["email"]

        for key, usuarios in lista_usuarios.items():
            #print(usuarios["email"])
            if email==usuarios["email"]:
                sesion_iniciada=True
                return redirect('/publicaciones')
                break
        cadena=f"Error, el email {email} no exite en la base de datos"
        return render_template('login.html',cadena=cadena)


        #sesion_iniciada=True
        #return redirect('/publicaciones')

# Salir ----------------------
@app.route("/salir",methods=["GET","POST"])
def salir():
    global sesion_iniciada
    sesion_iniciada=False
    return redirect('/index')

# Perfil ----------------------
@app.route("/perfil",methods=["GET","POST"])
def perfil():
        return render_template("perfil.html", sesion_iniciada=sesion_iniciada,lista_publicaciones=lista__publicaciones)

@app.route("/perfil_edit",methods=["GET","POST"])
def perfil_edit():
        return render_template("perfil_edit.html", sesion_iniciada=sesion_iniciada)

# Perfil usuarios ---------------------------
@app.route("/usuario/<id_usuario>",methods=["GET"])
def usuario_informacion(id_usuario):
    #validacion simple de usuario ..............................................
    if id_usuario in usuarios_sistema:
        return f"Pagina del Perfil del usuario {id_usuario}"    #validacion simple de usuario
    else:
        return f"Error, el usuario {id_usuario} no exite en la base de datos"

# Perfil admin  ..............
@app.route("/admin/<id_admin>",methods=["GET"])
def admin_informacion(id_admin):
    if id_admin in usuarios_sistema:
        return f"Pagina del Perfil del usuario Admin {id_admin}"   #validacion simple de Perfil admin
    else:
        return f"Error, el usuario {id_admin} no exite en la base de datos"

# Perfil superadmin ............
@app.route("/superadmin/<id_superadmin>",methods=["GET"])
def superadmin_informacion(id_superadmin):
    if id_superadmin in usuarios_sistema:
        return f"Pagina del Perfil del usuario Superadmin {id_superadmin}"  #validacion simple de Perfil superadmin
    else:
        return f"Error, el usuario {id_superadmin} no exite en la base de datos"

# Publicaciones --------------
@app.route("/publicaciones",methods=["GET"])
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

    if id_publicacion in lista_publicaciones:
        return lista_publicaciones[id_publicacion]
    else:
        return f"Error, la publicacion {id_publicacion} no exite en la base de datos"
        #return f"Pagina detalle de la publicacion {id_publicacion}"  #detalla_pub.html

# Busqueda de usuario ---------------------------
@app.route("/busqueda/<id_usuario>",methods=["GET","POST"])
def busqueda_usuario(id_usuario):
    if id_usuario in usuarios_sistema:
        return f"El usuario que buscas Existe: {id_usuario}, en la Base de Datos."
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
@app.route("/register" , methods=["GET","POST"])
def register():
    global sesion_iniciada
    try:
        if request.method=="POST":
            user1=request.form["username"]
            pass1=request.form["password"]
            c_pass1=request.form["c_password"]
            email=request.form["correo"]
            error = None

            if not utils.isUsernameValid(user1):
                error ="El usuario no es correcto"
                flash(error)
                return render_template("register.html")

            if not utils.isPasswordValid(pass1):
                error="Password invalido"
                flash(error)
                return render_template("register.html")

            if not utils.isPasswordValid(c_pass1):
                error="Password invalido"
                flash(error)
                return render_template("register.html")

            if (c_pass1 !=pass1):
                error="Password no coincide"
                flash(error)
                return render_template("register.html")

            if not utils.isEmailValid(email):
                error="Correo invalido"
                flash(error)
                return render_template("register.html")

            yag=yagmail.SMTP("pruebamintic2022","Jmd12345678")
            print("Paso por yag.")
            yag.send(to=email, subject="Activa tu cuenta", contents="Bienvenido, usa este link para activar tu cuenta")
            flash("Revisa tu correo para activar tu cuenta")
            return render_template("login.html")

        return render_template("register.html")
    except:
        return render_template("register.html")

if __name__=='__main__':
    app.run(debug=True, port=8080)

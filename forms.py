from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField,  fields
from wtforms.validators import DataRequired, InputRequired, InputRequired
from wtforms.fields.html5 import EmailField,DateField
from wtforms.validators import Length, Email
from wtforms.fields import TextAreaField
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename




'''class formEstudiante(FlaskForm):
    documento=StringField('Documento', validators=[DataRequired(message="no dejar Vacio")], render_kw={'placeholder':'Identificación', 'class':'form_control'})
    nombre=StringField('Nombre', validators=[DataRequired(message="no dejar Vacio")], render_kw={'placeholder':'Nombre', 'class':'form_control'})
    ciclo=SelectField('Ciclo', choices=[('Python'), ('Java'),('Web')])
    sexo=StringField('Sexo', validators=[DataRequired(message="no dejar Vacio")], render_kw={'placeholder':'M/F', 'class':'form_control'})
    estado=BooleanField('Estado')

    # botones
    enviar=SubmitField('Enviar', render_kw={'onmouseover':'guardarEst()', 'class':'form_boton'})
    consultar=SubmitField('Consultar', render_kw={'onmouseover':'consultarEst()', 'class':'form_boton'})
    listar=SubmitField('Listar', render_kw={'onmouseover':'listarEst()', 'class':'form_boton'})
    actualizar=SubmitField('Actualizar', render_kw={'onmouseover':'actualizarEst()', 'class':'form_boton'})
    eliminar=SubmitField('eliminar', render_kw={'onmouseover':'eliminarEst()', 'class':'form_boton'})

    # Eventos

class  formLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Usuario'} )
    clave = PasswordField('Clave', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Contraseña', 'id':'password'} )
    enviar = SubmitField('Enviar', render_kw={'class':'form_boton', 'onmouseover':'consultar_login()', 'class':'form_boton' })
    guardar = SubmitField('Guardar', render_kw={'class':'form_boton','onmouseover':'crear_login()', 'class':'form_boton'} )
'''

class  formRegister(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Usuario', 'class':'input','type':'text', 'id':'username', 'autocomplete':'username', 'required':'true', 'placeholder':'pepitoperez'} )
    correo = EmailField('correo', validators=[DataRequired(message='No dejar vacio')],render_kw={'class':'input', 
	'type':'text',
	'id':'email',
        'maxlength':'100',
        'placeholder':'e.g. alex@example.com',
        'autocomplete':'email',
        'required':'true',
        'pattern': '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$',
        'style':'text-transform: lowercase',
        'onkeyup':'javascript:this.value:this.value.toLowerCase();'})
    clave = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacio')], render_kw={'class':'input',
        'type':'password',
        'id':'password',
        'placeholder':'Contraseña',
        'required':'true',
        'minlength':'6'} )
    clave1 = PasswordField('Confirmar contraseña', validators=[DataRequired(message='No dejar vacio')], render_kw={'class':'input',
        'type':'password',
        'id':'password1',
        'placeholder':'Confirmar contraseña',
        'required':'true',
        'minlength':'6'} )
    estado=BooleanField('Estado',render_kw={'type':'checkbox', 'required':'true'})    
    guardar = SubmitField('Registrate!', render_kw={'onmouseover':'crear_register()',  'class':'button is-link is-fullwidth', 'type':'submit', 'value':'Registrate!'} )    


class  formEditProfile(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Usuario', 'class':'input','type':'text', 'id':'username', 'autocomplete':'username', 'required':'true', 'placeholder':'pepitoperez','readonly': True} )
    nombre = StringField('Nombre', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Nombre', 'class':'input','type':'text', 'id':'name', 'autocomplete':'name', 'required':'true', 'placeholder':'Nicolás'} )
    apellido = StringField('Apellido', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Apellido', 'class':'input','type':'text', 'id':'lastname', 'autocomplete':'lastname', 'required':'true', 'placeholder':'Montes de Oca'} )
    correo = EmailField('correo', validators=[DataRequired(message='No dejar vacio')],render_kw={'class':'input', 
	'type':'text',
	'id':'email',
        'maxlength':'100',
        'placeholder':'e.g. alex@example.com',
        'autocomplete':'email',
        'required':'true',
        'pattern': '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$',
        'style':'text-transform: lowercase',
        'onkeyup':'javascript:this.value:this.value.toLowerCase();'})
    clave = PasswordField('Contraseña', render_kw={'class':'input',
        'type':'password',
        'id':'password',
        'placeholder':'Contraseña',
        #'required':'true',
        'minlength':'6'})

    bd = DateField('Fecha Nacimiento', render_kw={'placeholder':'Fecha nacimiento', 'class':'input'})    
    genero = SelectField('Género', choices=[('Masculino'), ('Femenino')])
    #como = TextAreaField('Sobre mi', default='Sobre mi', render_kw={'class':'textarea'})
    como = StringField('Sobre mi', render_kw={'placeholder':'Sobre mi', 'class':'textarea'})    

    #estado=BooleanField('Estado',render_kw={'type':'checkbox', 'required':'true'})    ---actualizar_register()
    guardar = SubmitField('Guardar', render_kw={'onmouseover':'actualizar_register()',  'class':'button is-link is-fullwidth', 'type':'submit', 'value':'Guardar'} )    
    cancelar = SubmitField('Cancelar', render_kw={'onmouseover':'ir_publicaciones()',  'class':'button is-link is-light', 'type':'submit', 'value':'Cancelar'} )    


class  formLogin(FlaskForm):
    correo = EmailField('correo', validators=[DataRequired(message='No dejar vacio')],render_kw={'class':'input', 
	'type':'text',
	'id':'email',
        'maxlength':'100',
        'placeholder':'e.g. alex@example.com',
        'autocomplete':'email',
        'required':'true',
        'pattern': '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$',
        'style':'text-transform: lowercase',
        'onkeyup':'javascript:this.value:this.value.toLowerCase();'})
    clave = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacio')], render_kw={'class':'input',
        'type':'password',
        'id':'password',
        'placeholder':'Contraseña',
        'required':'true',
        'minlength':'6'} )
    enviar = SubmitField('Inicia Sesión!', render_kw={'onmouseover':'consultar_login()',  'class':'button is-link is-fullwidth', 'type':'submit', 'value':'Inicia Sesión'} )


class  formSearch(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Datos de Busqueda', 'class':'input','type':'text', 'id':'search_user', 'autocomplete':'search_user', 'placeholder':'pepitoperez'} )
    enviar = SubmitField('Busqueda', render_kw={'onmouseover':'consultar_user()',  'class':'button is-link is-fullwidth', 'type':'submit', 'value':'Busqueda'} )


class  PhotoForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Título', 'class':'input','type':'text', 'id':'username', 'autocomplete':'titulo', 'required':'true', 'placeholder':'Título Publicación'} )
    #url_img = StringField('Url Imagen', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Url Imagen', 'class':'input','type':'text', 'id':'username', 'autocomplete':'url_img', 'required':'true', 'placeholder':'Url Imagen'} )
    photo = FileField(validators=[FileRequired()], render_kw={'class':'file-input', 'type':'file'})
    contenido = TextAreaField('Contenido Publición', default='Contenido Publicación', render_kw={'class':'textarea'})
    #como = StringField('Sobre mi', render_kw={'placeholder':'Sobre mi', 'class':'textarea'})    
    guardar = SubmitField('Publicar', render_kw={'onmouseover':'adicionar_publicacion()',  'class':'button is-link is-fullwidth', 'type':'submit', 'value':'Publicar'} )    
    cancelar = SubmitField('Cancelar', render_kw={'onmouseover':'ir_publicaciones()',  'class':'button is-link is-light', 'type':'submit', 'value':'Cancelar'} )    

class  CommentsForm(FlaskForm):
    pub = StringField('', render_kw={'class':'input','type':'hidden', 'id':'pub'} )
    contenido = TextAreaField('Comentar', default='Comentar', render_kw={'class':'textarea'})
    guardar = SubmitField('Publicar comentario', render_kw={'onmouseover':'adicionar_comentario()',  'class':'button', 'type':'submit', 'value':'Publicar comentario'} )    
    


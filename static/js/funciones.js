function guardarEst(){
    document.getElementById("formulario").action="/estudiante/save"
}
function consultarEst(){
    document.getElementById("formulario").action="/estudiante/get"
}


function listarEst(){
    document.getElementById("formulario").action="/estudiante/list"
}
function actualizarEst(){
    document.getElementById("formulario").action="/estudiante/update"
}
function eliminarEst(){
    document.getElementById("formulario").action="/estudiante/delete"
}
<<<<<<< HEAD
function crear_login(){
    document.getElementById("formularioLogin").action="/login/save"
}
=======

>>>>>>> 9faa014551c53d21cc759daea42d4ebddfcc1d41

function mostraContrasena(){
    var tipo = document.getElementById("password")
    if (tipo.type == "password"){
        tipo.type = "text"
    }else{
        tipo.type="password"
    }
}

<<<<<<< HEAD




function consultar_login(){
    document.getElementById("formLogin").action="/ingreso/get"
=======
function crear_login(){
    document.getElementById("formularioLogin").action="/login/save"
}


function consultar_login(){
    document.getElementById("formularioLogin").action="/login/get"
>>>>>>> 9faa014551c53d21cc759daea42d4ebddfcc1d41
}

function crear_register(){
    document.getElementById("formRegister").action="/register/save"
}

function ir_publicaciones(){
    document.getElementById("formEditProfile").action="/publicaciones"
}

function actualizar_register(){
    document.getElementById("formEditProfile").action="/perfil_edit/save"
}

function ir_register(){
    document.getElementById("formEditProfile").action="/perfil_edit/"
}
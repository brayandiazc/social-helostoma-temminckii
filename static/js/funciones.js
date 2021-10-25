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
function crear_login(){
    document.getElementById("formularioLogin").action="/login/save"
}

function mostraContrasena(){
    var tipo = document.getElementById("password")
    if (tipo.type == "password"){
        tipo.type = "text"
    }else{
        tipo.type="password"
    }
}





function consultar_login(){
    document.getElementById("formLogin").action="/ingreso/get"
}

consultar_user
function consultar_user(){
    document.getElementById("formSearch").action="/busqueda/get"
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


function adicionar_publicacion(){
    document.getElementById("PhotoForm").action="/publicacion_new/save"
}

function ir_publicaciones(){
    document.getElementById("PhotoForm").action="/publicaciones"
}
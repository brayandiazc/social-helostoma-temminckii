/** 
                                          *** @Modelo de la base de datos *** 
                       Nota:(La mayoría de las tablas incluyen su ID para ser relacionadas con otras tablas) 
                                                                                                                **/
                       
/**  ----------------------------------------------------------------------------------------------        **/
/* Tipo user */
CREATE TABLE user (
    id           INTEGER       NOT NULL
                               PRIMARY KEY AUTOINCREMENT, /** id: es la llave primaria auto incremental de la tabla **/                              
    name         VARCHAR (50),              /** Nombre real del usuario **/
    lastname     VARCHAR (50),              /** Apellidos del usuario **/
    username     VARCHAR (50),              /** Nombre de usuario para inciar sesión **/
    email        VARCHAR (255),             /** Correo para iniciar sesión y para recibir notificaciones **/
    password     VARCHAR (60),              /** Contraseña del usuario para iniciar sesión **/
    gender       VARCHAR (1),               /** Genero del Usuario **/
    image        VARCHAR (255),             /** Imagen del usuario para guardar las imagenes **/
    image_header VARCHAR (255),             /** Encabezado de la imagen **/
    likes        TEXT,                      /** Cosas que te gustan **/
    is_active    BOOLEAN       DEFAULT 0,   /** Si el usuario está activo **/
    id_type      INT,                       /** Tipo de usuario **/
    created_at   DATETIME,                  /** Fecha de creación  **/
    FOREIGN KEY (
        id_type                             /** Identificador del tipo llave foreana **/
    )
    REFERENCES type_user (id)               /** Relación User -> type_user  **/
);

/**  ----------------------------------------------------------------------------------------------        **/
/* Tipo Usuario o Perfil del usuario */
CREATE TABLE type_user (
    id               INTEGER      NOT NULL
                                  PRIMARY KEY AUTOINCREMENT, /** Identificador type_user llave primaria **/
    description_type VARCHAR (50),                           /** Descripción del tipo de usuario: User, admin,sup_admin **/
    is_active        BOOLEAN      DEFAULT 0,                 /** Si el tipo de usuario esta activo **/
    created_at       DATETIME                                /** Fecha de creación del tipo de usuario **/
);

/**  ----------------------------------------------------------------------------------------------        **/
/* Tipo Imagen  */
CREATE TABLE image (
    id         INTEGER       NOT NULL
                             PRIMARY KEY AUTOINCREMENT,      /** Identificador imagen llave primaria **/
    src        VARCHAR (255),                                /** Nombre del archivo de imagen, se guardaran las imagenes **/
    title      VARCHAR (200),                                /** Titulo de la imagen **/                               
    content    VARCHAR (500),                                /** Descripción de la imagen del usuario **/
    user_id    INT,                                          /** Id del usuario propietario de la imagen **/
    created_at DATETIME,                                     /** Fecha de creación o publicación de la imagen **/
    FOREIGN KEY (
        user_id                                              /** relación del identificador del usuario **/
    )
    REFERENCES user (id)                                     /** relación id user **/
);

/**  ----------------------------------------------------------------------------------------------        **/
/* Tipo post o publicaciones  */
CREATE TABLE post (
    id            INTEGER       NOT NULL
                                PRIMARY KEY AUTOINCREMENT,   /** Identificador del post o publicaciones llave primaria **/
    title         VARCHAR (500),                             /** Titulo de la publicación **/
    content       TEXT,                                      /** Contenido de la publicación **/
    lat           DOUBLE,                                    /** Coordenada latitud para la ubicación **/
    lng           DOUBLE,                                    /** Coordenada longitud para la ubicación **/
    start_at      DATETIME,                                  /** Fecha de inicio de la publicación **/
    finish_at     DATETIME,                                  /** Fecha de fin de la publicación **/
    author_ref_id INT,                                       /** El id del usuario que publica **/
    created_at    DATETIME,                                  /** Fecha de creación de la publicación **/
    is_active     BOOLEAN,                                   /** La publicación se encuentra activa o desactivada**/
    FOREIGN KEY (
        author_ref_id                                        /** identificacdor author_ref_id llave foreana **/
    )
    REFERENCES user (id)                                     /** relación id user **/
);

/**  ----------------------------------------------------------------------------------------------        **/
/* Tipo post o publicaciones a imagenes  */
CREATE TABLE post_image (
    post_id  INT,                                            /** Identificador de la publicación **/
    image_id INT,                                            /** Identificador de la imagen **/
    FOREIGN KEY (                          
        post_id                                              /** Relación post_id llave foreana **/
    )
    REFERENCES post (id),                                    /** Relación post_id **/
    FOREIGN KEY (
        image_id                                             /** Relación imagen_id llave foreana **/                                           
    )
    REFERENCES image (id)                                    /** Referenciada a imagen_id **/
);

/**  ----------------------------------------------------------------------------------------------        **/
/* Tipo qualification  */
CREATE TABLE qualification (
    id         INTEGER  NOT NULL
                        PRIMARY KEY AUTOINCREMENT,           /** Identificador del qualification llave primaria **/
    ref_id     INT,                                          /**  El id de referencia del usuario que califica la publicación **/
    user_id    INT,                                          /**  El id del usuario que califica la publicación **/
    created_at DATETIME,                                     /**  El fecha de calificación la publicación **/
    FOREIGN KEY (
        user_id                                              /**  El id del usuario que califica **/
    )
    REFERENCES user (id)                                     /**  Relación con user **/
);

/**  --------------------------------------------------------------         **/
/* Tipo comment  */
CREATE TABLE comment (
    id         INTEGER  NOT NULL
                        PRIMARY KEY AUTOINCREMENT,           /** Identificador del comentario llave primaria **/
    type_id    INT,                                          /** Identificador del Tipo, si es para posts, imágenes etc. **/
    ref_id     INT,                                          /** Identificador del del post, imagen o album según el caso **/
    user_id    INT,                                          /** Identificador del usuario que crea el comentario **/
    content    TEXT,                                         /** Contenido del comentario **/
    comment_id INT,                                          /** Si es un comentario de otro comentario, se guarda el id del comentario superior **/
    created_at DATETIME,                                     /** Fecha de creación del comentario **/
    is_active  BOOLEAN,                                      /** Está activo el comentario o bloqueado  **/
    FOREIGN KEY (
        user_id                                              /** Identificador del user que comenta llave foreana **/
    )
    REFERENCES user (id),                                    /** Identificador del qualification llave primaria **/
    FOREIGN KEY (
        ref_id                                               /** Fecha de creación llave foreana **/              
    )
    REFERENCES post (id)                                     /** realción del post **/
);

/**  --------------------------------------------------------------         **/
/* Tipo conversation  */
CREATE TABLE conversation (
    id          INTEGER  NOT NULL
                         PRIMARY KEY AUTOINCREMENT,           /** Identificador de la conversación llave primaria **/
    sender_id   INT,                                          /** Identificador Usuario que envía la solicitud de amistad **/
    receptor_id INT,                                          /** Identificador Usuario que recibe la solicitud **/
    created_at  DATETIME,                                     /** Fecha de creacion de la solicitud **/
    is_active   BOOLEAN,                                      /** Está activa la conversación **/
    FOREIGN KEY (
        sender_id                                             /** Identificador del comentario llave primaria **/
    )
    REFERENCES user (id),                                     /** Referencias id user **/
    FOREIGN KEY (
        receptor_id                                           /** Identificador Usuario que recibe la solicitud **/
    )
    REFERENCES user (id)                                      /** Referencias id user **/
);

/**  --------------------------------------------------------------         **/
/* Tipo message  */
CREATE TABLE message (
    id              INTEGER  NOT NULL
                             PRIMARY KEY AUTOINCREMENT,       /** Identificador del la message llave primaria **/
    content         TEXT,                                     /** Contenido del mensaje **/
    user_id         INT,                                      /** Usuario que envía el mensaje **/
    conversation_id INT,                                      /**  Id de la conversación **/
    created_at      DATETIME,                                 /** Fecha de creación del mensaje **/
    is_readed       BOOLEAN  DEFAULT 0,                       /** Si el mensaje ya fue leído por el otro usuario **/
    FOREIGN KEY (
        user_id                                               /** Identificador del usuario **/
    )
    REFERENCES user (id),                                     /** Identificador user **/
    FOREIGN KEY (
        conversation_id                                       /** Identificador de la conversación llave foreana **/
    )
    REFERENCES conversation (id)                              /** Referencia id conversación **/
);

/**  --------------------------------------------------------------         **/
/* Tipo notification  */
CREATE TABLE notification (
    id          INTEGER  NOT NULL 
                         PRIMARY KEY AUTOINCREMENT,           /** Identificador del la message llave primaria **/
    ref_id      INT,                                          /** Id del contenido que activa la notificación **/
    receptor_id INT,                                          /** Usuario que va a recibir la notificación **/
    sender_id   INT,                                          /** Usuario que activa la notificación **/
    is_readed   BOOLEAN  DEFAULT 0,                           /** Si ya fue leída la notificación **/
    created_at  DATETIME,                                     /** Fecha de creación de la notificación **/
    FOREIGN KEY (
        sender_id                                             /** Identificador Usuario que activa o envia la notificación para llave foreana **/
    )
    REFERENCES user (id),                                     /** Identificador Usuario **/
    FOREIGN KEY (
        receptor_id                                           /** Identificador Usuario que va a recibir **/
    ) 
    REFERENCES user (id)                                      /** Referencia Usuario id **/
);

/**  --------------------------------------------------------------         **/
/* Tipo profile  */
CREATE TABLE profile (
    id         INTEGER  NOT NULL
                        PRIMARY KEY AUTOINCREMENT,            /** Identificador del profile de los user llave primaria **/
    post       BOOLEAN  DEFAULT (0),                          /** Activar desactivar publicaciones **/
    comment    BOOLEAN  DEFAULT (0),                          /** Activar desactivar comentarios **/
    messaje    BOOLEAN  DEFAULT (0),                          /** Activar desactivar mensajes **/
    user_id    INT,                                           /** Identificador user **/
    created_at DATETIME,                                      /** fecha de creación de perfiles **/
    FOREIGN KEY (
        user_id                                               /** Identificador Usuario llave foreana **/
    )
    REFERENCES user (id)                                      /** Referencia Usuario id **/
);
/**  ----------------------------------------------------------------------------------------------        **/
/**  ----------------------------------------------------------------------------------------------        **/
/**  ----------------------------------------------------------------------------------------------        **/
/**  ----------------------------------------------------------------------------------------------        **/
/**  ----------------------------------------------------------------------------------------------        **/
/**  ----------------------------------------------------------------------------------------------        **/
/**  ----------------------------------------------------------------------------------------------        **/
/* para grupos: no puedo usar la palabra reservada group, entonces uso team */

/*create table team (
	id int not null auto_increment primary key,
	image varchar(200),
	title varchar(200),
	description varchar(500) ,
	user_id int,
	status int default 1 *//* 1.- open, 2.- closed */,
	/*created_at datetime,
	foreign key (user_id) references user(id)
);*/

/**  ----------------------------------------------------------------------------------------------        **/
/*
create table friend(
	id int not null auto_increment primary key,
	sender_id int,
	receptor_id int,
	is_accepted boolean default 0,
	is_readed boolean default 0,
	created_at datetime,
	foreign key (sender_id) references user(id),
	foreign key (receptor_id) references user(id)
);*/
/**  ----------------------------------------------------------------------------------------------        **/

/**
* post_type_id
* 1.- status
* 2.- event
**/
/**  ----------------------------------------------------------------------------------------------        **/

/*
create table level(
	id int not null auto_increment primary key,
	name varchar(50)
);

insert into level (name) values ("Publico"), ("Solo amigos"), ("Amigos de mis amigos");
*/
/*
create table country(
	id int not null auto_increment primary key,
	name varchar(50),
	preffix varchar(50)
);

insert into country(name,preffix) values ("Mexico","mx"),("Argentina","ar"),("Espa~a","es"),("Estados Unidos","eu"),("Chile","cl"),("Colombia","co"),("Peru","pe");
*/
/*
create table sentimental(
	id int not null auto_increment primary key,
	name varchar(50)
);

insert into sentimental(name) values ("Soltero"),("Casado");
*/

/*
create table profile(
	day_of_birth date ,
	gender varchar(1) ,
	country_id int ,
	image varchar(255),
	image_header varchar(255),
	title varchar(255),
	bio varchar(255),
	likes text,
	dislikes text,
	address varchar(255) ,
	phone varchar(255) ,
	public_email varchar(255) ,
	user_id int ,
	level_id int ,
	sentimental_id int ,
	foreign key (sentimental_id) references sentimental(id),
	foreign key (country_id) references country(id),
	foreign key (level_id) references level(id),
	foreign key (user_id) references user(id)
);*/
/**  ----------------------------------------------------------------------------------------------        **/
/*
create table album(
	id int not null auto_increment primary key,
	title varchar(200),
	content varchar(500),
	user_id int,
	level_id int,
	created_at datetime,
	foreign key (user_id) references user(id),
	foreign key (level_id) references level(id)
);
*/
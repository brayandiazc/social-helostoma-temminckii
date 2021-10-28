/** 
                                          *** @Modelo de la base de datos *** 
                       Nota:(La mayor�a de las tablas incluyen su ID para ser relacionadas con otras tablas) 
                                                                                                                **/
                       
/**  ----------------------------------------------------------------------------------------------        **/
/* Tipo user */
CREATE TABLE user (
    id           INTEGER       NOT NULL
                               PRIMARY KEY AUTOINCREMENT, /** id: es la llave primaria auto incremental de la tabla **/                              
    name         VARCHAR (50),              /** Nombre real del usuario **/
    lastname     VARCHAR (50),              /** Apellidos del usuario **/
    username     VARCHAR (50),              /** Nombre de usuario para inciar sesi�n **/
    email        VARCHAR (255),             /** Correo para iniciar sesi�n y para recibir notificaciones **/
    password     VARCHAR (60),              /** Contrase�a del usuario para iniciar sesi�n **/
    gender       VARCHAR (1),               /** Genero del Usuario **/
    image        VARCHAR (255),             /** Imagen del usuario para guardar las imagenes **/
    image_header VARCHAR (255),             /** Encabezado de la imagen **/
    likes        TEXT,                      /** Cosas que te gustan **/
    is_active    BOOLEAN       DEFAULT 0,   /** Si el usuario est� activo **/
    id_type      INT,                       /** Tipo de usuario **/
    created_at   DATETIME,                  /** Fecha de creaci�n  **/
    bd           DATETIME,                  /** Fecha de nacimiento  **/
    FOREIGN KEY (
        id_type                             /** Identificador del tipo llave foreana **/
    )
    REFERENCES type_user (id)               /** Relaci�n User -> type_user  **/
);

/**  ----------------------------------------------------------------------------------------------        **/
/* Tipo Usuario o Perfil del usuario */
CREATE TABLE type_user (
    id               INTEGER      NOT NULL
                                  PRIMARY KEY AUTOINCREMENT, /** Identificador type_user llave primaria **/
    description_type VARCHAR (50),                           /** Descripci�n del tipo de usuario: User, admin,sup_admin **/
    is_active        BOOLEAN      DEFAULT 0,                 /** Si el tipo de usuario esta activo **/
    created_at       DATETIME                                /** Fecha de creaci�n del tipo de usuario **/
);

/**  ----------------------------------------------------------------------------------------------        **/
/* Tipo Imagen  */
CREATE TABLE image (
    id         INTEGER       NOT NULL
                             PRIMARY KEY AUTOINCREMENT,      /** Identificador imagen llave primaria **/
    src        VARCHAR (255),                                /** Nombre del archivo de imagen, se guardaran las imagenes **/
    title      VARCHAR (200),                                /** Titulo de la imagen **/                               
    content    VARCHAR (500),                                /** Descripci�n de la imagen del usuario **/
    user_id    INT,                                          /** Id del usuario propietario de la imagen **/
    created_at DATETIME,                                     /** Fecha de creaci�n o publicaci�n de la imagen **/
    FOREIGN KEY (
        user_id                                              /** relaci�n del identificador del usuario **/
    )
    REFERENCES user (id)                                     /** relaci�n id user **/
);

/**  ----------------------------------------------------------------------------------------------        **/
/* Tipo post o publicaciones  */
CREATE TABLE post (
    id            INTEGER       NOT NULL
                                PRIMARY KEY AUTOINCREMENT,   /** Identificador del post o publicaciones llave primaria **/
    title         VARCHAR (500),                             /** Titulo de la publicaci�n **/
    content       TEXT,                                      /** Contenido de la publicaci�n **/
    lat           DOUBLE,                                    /** Coordenada latitud para la ubicaci�n **/
    lng           DOUBLE,                                    /** Coordenada longitud para la ubicaci�n **/
    start_at      DATETIME,                                  /** Fecha de inicio de la publicaci�n **/
    finish_at     DATETIME,                                  /** Fecha de fin de la publicaci�n **/
    author_ref_id INT,                                       /** El id del usuario que publica **/
    created_at    DATETIME,                                  /** Fecha de creaci�n de la publicaci�n **/
    is_active     BOOLEAN,                                   /** La publicaci�n se encuentra activa o desactivada**/
    FOREIGN KEY (
        author_ref_id                                        /** identificacdor author_ref_id llave foreana **/
    )
    REFERENCES user (id)                                     /** relaci�n id user **/
);

/**  ----------------------------------------------------------------------------------------------        **/
/* Tipo post o publicaciones a imagenes  */
CREATE TABLE post_image (
    post_id  INT,                                            /** Identificador de la publicaci�n **/
    image_id INT,                                            /** Identificador de la imagen **/
    FOREIGN KEY (                          
        post_id                                              /** Relaci�n post_id llave foreana **/
    )
    REFERENCES post (id),                                    /** Relaci�n post_id **/
    FOREIGN KEY (
        image_id                                             /** Relaci�n imagen_id llave foreana **/                                           
    )
    REFERENCES image (id)                                    /** Referenciada a imagen_id **/
);

/**  ----------------------------------------------------------------------------------------------        **/
/* Tipo qualification  */
CREATE TABLE qualification (
    id         INTEGER  NOT NULL
                        PRIMARY KEY AUTOINCREMENT,           /** Identificador del qualification llave primaria **/
    ref_id     INT,                                          /**  El id de referencia del usuario que califica la publicaci�n **/
    user_id    INT,                                          /**  El id del usuario que califica la publicaci�n **/
    created_at DATETIME,                                     /**  El fecha de calificaci�n la publicaci�n **/
    FOREIGN KEY (
        user_id                                              /**  El id del usuario que califica **/
    )
    REFERENCES user (id)                                     /**  Relaci�n con user **/
);

/**  --------------------------------------------------------------         **/
/* Tipo comment  */
CREATE TABLE comment (
    id         INTEGER  NOT NULL
                        PRIMARY KEY AUTOINCREMENT,           /** Identificador del comentario llave primaria **/
    type_id    INT,                                          /** Identificador del Tipo, si es para posts, im�genes etc. **/
    ref_id     INT,                                          /** Identificador del del post, imagen o album seg�n el caso **/
    user_id    INT,                                          /** Identificador del usuario que crea el comentario **/
    content    TEXT,                                         /** Contenido del comentario **/
    comment_id INT,                                          /** Si es un comentario de otro comentario, se guarda el id del comentario superior **/
    created_at DATETIME,                                     /** Fecha de creaci�n del comentario **/
    is_active  BOOLEAN,                                      /** Est� activo el comentario o bloqueado  **/
    FOREIGN KEY (
        user_id                                              /** Identificador del user que comenta llave foreana **/
    )
    REFERENCES user (id),                                    /** Identificador del qualification llave primaria **/
    FOREIGN KEY (
        ref_id                                               /** Fecha de creaci�n llave foreana **/              
    )
    REFERENCES post (id)                                     /** realci�n del post **/
);

/**  --------------------------------------------------------------         **/
/* Tipo conversation  */
CREATE TABLE conversation (
    id          INTEGER  NOT NULL
                         PRIMARY KEY AUTOINCREMENT,           /** Identificador de la conversaci�n llave primaria **/
    sender_id   INT,                                          /** Identificador Usuario que env�a la solicitud de amistad **/
    receptor_id INT,                                          /** Identificador Usuario que recibe la solicitud **/
    created_at  DATETIME,                                     /** Fecha de creacion de la solicitud **/
    is_active   BOOLEAN,                                      /** Est� activa la conversaci�n **/
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
    user_id         INT,                                      /** Usuario que env�a el mensaje **/
    conversation_id INT,                                      /**  Id de la conversaci�n **/
    created_at      DATETIME,                                 /** Fecha de creaci�n del mensaje **/
    is_readed       BOOLEAN  DEFAULT 0,                       /** Si el mensaje ya fue le�do por el otro usuario **/
    FOREIGN KEY (
        user_id                                               /** Identificador del usuario **/
    )
    REFERENCES user (id),                                     /** Identificador user **/
    FOREIGN KEY (
        conversation_id                                       /** Identificador de la conversaci�n llave foreana **/
    )
    REFERENCES conversation (id)                              /** Referencia id conversaci�n **/
);

/**  --------------------------------------------------------------         **/
/* Tipo notification  */
CREATE TABLE notification (
    id          INTEGER  NOT NULL 
                         PRIMARY KEY AUTOINCREMENT,           /** Identificador del la message llave primaria **/
    ref_id      INT,                                          /** Id del contenido que activa la notificaci�n **/
    receptor_id INT,                                          /** Usuario que va a recibir la notificaci�n **/
    sender_id   INT,                                          /** Usuario que activa la notificaci�n **/
    is_readed   BOOLEAN  DEFAULT 0,                           /** Si ya fue le�da la notificaci�n **/
    created_at  DATETIME,                                     /** Fecha de creaci�n de la notificaci�n **/
    FOREIGN KEY (
        sender_id                                             /** Identificador Usuario que activa o envia la notificaci�n para llave foreana **/
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
    created_at DATETIME,                                      /** fecha de creaci�n de perfiles **/
    FOREIGN KEY (
        user_id                                               /** Identificador Usuario llave foreana **/
    )
    REFERENCES user (id)                                      /** Referencia Usuario id **/
);
                           /** View Sqlite  **/

DROP VIEW view_user_find;                                     /** Se creó vista busqueda usuario en Sqlite  **/

CREATE VIEW view_user_find AS
    SELECT USERNAME,
           NAME || " " || LASTNAME AS NAME_COMPLETE,
           LIKES,
           IS_ACTIVE
      FROM USER;

                           /** View Sqlite  **/
			   
DROP VIEW view_post_comment;

CREATE VIEW view_post_comment AS                              /** Se creó vista comentario publicaciones en Sqlite  **/
    SELECT B.ID AS POST_ID,
           B.AUTHOR_REF_ID AS USER_ID_POST,
           E.ID,
           E.USER_ID,
           E.CONTENT,
           E.CREATED_AT,
           E.IS_ACTIVE,
           A.USERNAME,
           A.NAME || " " || A.LASTNAME AS NAME_COMPLETE_POST,
           (

		   
		                   /** View Sqlite  **/
SELECT NAME || " " || LASTNAME
                 FROM USER
                WHERE ID = E.USER_ID
           )
           AS NAME_COMPLETE_COMMENT
      FROM POST AS B,
           COMMENT AS E,
           USER AS A
     WHERE B.ID = E.REF_ID AND 
           B.AUTHOR_REF_ID = A.ID;


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

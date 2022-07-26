CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios(
    id          int AUTO_INCREMENT NOT NULL,
    nombre      varchar(100),
    apellidos   varchar(255),
    email       varchar(255),
    pass        varchar(255),
    fecha       date not null,
    CONSTRAINT  pk_usuarios PRIMARY KEY(id),
    CONSTRAINT  uq_email UNIQUE(email)
)   ENGINE=InnoDb;

CREATE TABLE notas(
    id          int AUTO_INCREMENT NOT NULL,
    usuario_id  int NOT NULL,
    titulo      varchar(255) NOT NULL,
    descripcion MEDIUMTEXT,
    fecha       date NOT NULL,
    CONSTRAINT  pk_notas PRIMARY KEY(id),
    CONSTRAINT  fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;
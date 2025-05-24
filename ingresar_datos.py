from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import csv

# Importamos las clases del archivo generar_tablas
from generar_tablas import Usuario, Publicacion, Reaccion

# Importar la información de configuracion
from configuracion import cadena_base_datos
# Generación del enlace a la base de datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# CARGA DE LOS USUARIOS
usuarios_dict = {} # Diccionario para almacenar los usuarios
# Para cargar los usuarios desde un archivo CSV vamos a generar un diccionario
# y apartir de este diccionario añadirlos a la base de datos
with open('DATA/usuarios_red_x.csv', mode='r', encoding='utf-8') as usuarios_csv:
    lector = csv.DictReader(usuarios_csv)
    for f in lector:
        # Creacción de un objeto de tipo Usuairo
        usuario = Usuario(
            nombre=f['usuario']
        )
        # Añadir a la session los usuairos
        session.add(usuario)
        # Guardamos en el diccionario los usuarios para hacer las relaciones
        # a través del nombre del usuario
        usuarios_dict[f['usuario']] = usuario

# Confirmamos la transacción
session.commit()

# CARGA DE LAS PUBLICACIONES
publicaciones_dict = {} # Diccionario para almacenar las publicaciones
# Para cargar las publicaciones desde un archivo CSV vamos a generar un diccionario
# y apartir de este diccionario añadirlos a la base de datos
with open('DATA/usuarios_publicaciones.csv', mode='r', encoding='utf-8') as publicaciones_csv:
    lector = csv.DictReader(publicaciones_csv, delimiter='|')
    for f in lector:
        # Almacenamos el nombre del usuario
        usuario = f['usuario']
        # Obtenemos el objeto de tipo Usuario con el nombre correspondiente
        obj_usuario = usuarios_dict.get(usuario)

        # Creacción de un objeto de tipo Publicacion
        publicacion = Publicacion(
            publicacion=f['publicacion'],
            usuario=obj_usuario
        )
        # Añadir a la session las publicaciones
        session.add(publicacion)
        # Guardamos en el diccionario las publicaciones para hacer las relaciones
        # a través las publicaciones de las publicaiones
        publicaciones_dict[f['publicacion']] = publicacion

# Confirmamos la transacción
session.commit()

# CARGA DE LAS REACCIONES
# Para cargar las reacciones desde un archivo CSV vamos a generar un diccionario
# y apartir de este diccionario añadirlos a la base de datos
with open('DATA/usuario_publicacion_emocion.csv', mode='r', encoding='utf-8') as reacciones_csv:
    lector = csv.DictReader(reacciones_csv, delimiter='|')
    for f in lector:
        # Almacenamos el nombre del usuario
        usuario = f['Usuario']
        # Obtenemos el objeto de tipo Usuario con el nombre correspondiente
        obj_usuario = usuarios_dict.get(usuario)

        # Almacenamos la publicacion de los comentarios
        publicacion = f['comentario']
        # Obtenemos el objeto de tipo Publicacion con la publicación que corresponde
        obj_publicacion = publicaciones_dict.get(publicacion)

        # Creacción de un objeto de tipo Reaccion
        reaccion = Reaccion(
            tipo_emocion=f['tipo emocion'],
            usuario=obj_usuario,
            publicacion=obj_publicacion
        )
        # Añadir a la session las publicaciones
        session.add(reaccion)

# Confirmamos la transacción
session.commit()

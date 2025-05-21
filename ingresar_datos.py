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
# Para cargar los usuarios desde un archivo CSV vamos a generar un diccionario
# y apartir de este diccionario añadirlos a la base de datos
usuarios_dict = {} # Diccionario para almacenar los usuarios

with open('DATA/usuarios_red_x.csv', mode='r', encoding='utf-8') as usuarios_csv:
    lector = csv.DictReader(usuarios_csv)
    for f in lector:
        # Creacció de un objeto de tipo Usuairo
        usuario = Usuario(
            nombre=f['usuario']
        )
        # Añadir a la session los usuairos
        session.add(usuario)
        # Guardamos en el diccionario los usuarios
        usuarios_dict[f['nombre']] = usuario

# Confirmamos la transacción
session.commit()
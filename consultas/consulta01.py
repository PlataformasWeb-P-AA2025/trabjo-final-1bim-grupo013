from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
# Importamos lo necesario para realizar las consultas

# Importamos las clases del archivo generar_tablas
from generar_tablas import Usuario, Publicacion, Reaccion

# Importamos la información del archivo configuracion
from configuracion import cadena_base_datos
# Enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# CONSULTA 1
# Listar publicaciones de un usuario.

# Obtenemos todos los registros de la entidad Usuario
publi_usuario = session.query(Usuario).all()
# Por cada Usuairo podemos acceder a sus publicaciones
for u in publi_usuario:
    print(f"{u}:")
    
    # Obtenemos la lista de publicaciones
    publicaciones = u.publicaciones
    for p in publicaciones:
        print(f"\t- {p.publicacion}")
    
    print("---------------------------------------")

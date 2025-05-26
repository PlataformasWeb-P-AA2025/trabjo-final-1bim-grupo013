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

# CONSULTA 2
# Listar las reacciones a una publicación.

# Obtenemos todos los registros de la entidad Publicacion
reaccion_publi = session.query(Publicacion).all()
# Por cada Publicacion podemos acceder a las reacciones
for p in reaccion_publi:
    print(f"{p}:")
    
    # Obtenemos la lista de reacciones
    reacciones = p.reacciones
    for r in reacciones:
        print(f"\t- {r.tipo_emocion}")
    
    print("---------------------------------------")

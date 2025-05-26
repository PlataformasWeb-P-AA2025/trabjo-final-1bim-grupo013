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

# CONSULTA 3
# Mostrar en qué publicaciones reaccionó un usuario.

# Obtenemos todos los registros de la entidad Usuario
usaurio_reaccion = session.query(Usuario).all()
# Por cada Usuario podemos acceder a las reacciones y de estas a las publicaciones
for u in usaurio_reaccion:
    print(f"{u}:")
    
    # Obtenemos la lista de reacciones
    reacciones = u.reacciones
    for r in reacciones:
        print(f"\t- Reaccionó a: {r.publicacion.publicacion} Con: {r.tipo_emocion}")
    
    print("---------------------------------------")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_
from sqlalchemy import func # Para hacer uso del count()
# Importamos lo necesario para realizar las consultas

# Importamos las clases del archivo generar_tablas
from generar_tablas import Usuario, Publicacion, Reaccion

# Importamos la información del archivo configuracion
from configuracion import cadena_base_datos
# Enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# CONSULTA 5
# Listar todas las reacciones de tipo "alegre", "enojado", "pensativo"
# que sean de usuarios que cuyos nombre no inicien con vocal.

# Obtenemos todos los registros de la entidad Usuario
# Y filtramos las reacciones y los nombres de usuairos
usaurio_reaccion = session.query(Reaccion, Usuario).join(Usuario)\
    .filter(
        or_(
            Reaccion.tipo_emocion == "alegre",
            Reaccion.tipo_emocion == "enojado",
            Reaccion.tipo_emocion == "pensativo"
        ),
        and_(
            Usuario.nombre.not_like("A%"),
            Usuario.nombre.not_like("E%"),
            Usuario.nombre.not_like("I%"),
            Usuario.nombre.not_like("O%"),
            Usuario.nombre.not_like("U%")
        ))\
            .order_by(Reaccion.tipo_emocion).all()

# Presnetación
for u in usaurio_reaccion:
    print(f"{u[0]} - {u[1]}")
    
    print("---------------------------------------")

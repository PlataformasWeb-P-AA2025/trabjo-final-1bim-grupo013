from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
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

# CONSULTA 4
# Obtener un reporte de reacciones en función del número de veces que fueron usadas.

# Obtenemos todos los registros de la entidad Reaccion
# Hacemos uso de func, para poder realizar un conteo y despues agrupar por tipo_emocion
reporte = session.query(Reaccion.tipo_emocion, func.count(Reaccion.tipo_emocion))\
    .group_by(Reaccion.tipo_emocion).all()

for emocion, n in reporte:
    print(f"{emocion}: {n}")

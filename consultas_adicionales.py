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

# Consulta 1
# Obtener el número de publicaciones que ha hecho cada usuario.

# Obtenemos todos los registros de la entidad Usuario y hacemos un conteo de las
# publicaciones después agrupamos por cada uno de los usuarios para obtener las
# publicaiones que ha realizado cada uno
consulta1 = session.query(Usuario, func.count(Usuario.publicaciones))\
    .join(Publicacion).group_by(Usuario.id).all()
print("CONSULTA ADICIONAL 1:")

for c in consulta1:
    print(f"{c[0].nombre} hizo {c[1]} publicaciones")

print("---------------------------------------")

# Consulta 2
# Listar los usuarios que no tienen publicaciones.

# Obtenemos todos los registros de la entidad Usuario y filtramos los usuarios
# que no tienen ninguna publicación
consulta2 = session.query(Usuario).filter(Usuario.publicaciones == None).all()
print("CONSULTA ADICIONAL 2:")

for c in consulta2:
    print(c)

print("---------------------------------------")

# Consulta 3
# Mostrar las publicaciones a las que reaccionaron usuarios cuyo nombre empieza por A.

# Obtenemos todos los registros de Publicacion y hacemos un join con Reaccion y Usuario
# para poder filtrar los nombres que emoiezan por A
consulta3 = session.query(Publicacion).join(Reaccion).join(Usuario).filter(Usuario.nombre.like("A%")).all()
print("CONSULTA ADICIONAL 3:")

for c in consulta3:
    print(c)

print("---------------------------------------")

# Consulta 4
# Obtener la lista de usuarios que han reaccionado con "enojado".

# Obtenemos los registros de Uauario y hacemos un join con Reaccion, esto para poder filtrar
# las reacciones que son "enojado"
consulta4 = session.query(Usuario).join(Reaccion).filter(Reaccion.tipo_emocion == "enojado").all()
print("CONSULTA ADICIONAL 4:")

for c in consulta4:
    print(c)

print("---------------------------------------")

# Consulta 5
# Mostrar cuántas reacciones ha hecho cada usuario.

# Obtenemos los registros de Usuarios y usamos la func.count() para contar el número de reacciones
# que cada usuario ha realizado
consulta5 = session.query(Usuario, func.count(Usuario.reacciones)).join(Reaccion).group_by(Usuario.id).all()
print("CONSULTA ADICIONAL 5:")

for c in consulta5:
    print(f"{c[0].nombre} ha realizado {c[1]} reacciones")

print("---------------------------------------")

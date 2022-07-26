"""
Proyecto Python-MySQL;
    -Abrir consola (asistente)
    -Login o registro
    -Registro: crea usuario en base de datos
    -Login: identifica al usuario y preguntará si necesita
    crear nota, mostrar nota o borrarlas.
"""
from usuarios import acciones

print("""
Acciones disponibles:
    -registro(1)
    -login(2)
""")

ejecutar = acciones.Acciones()

accion = input("Qué quieres hacer?: ")

if accion == "registro" or accion == "1":
    ejecutar.registro()

elif accion == "login" or accion == "2":
    ejecutar.login()

import usuarios.usuario as user
import notas.acciones

class Acciones:

    def registro(self):
        print("\nRegístrate en el sistema\n")
        
        nombre = input("Ingresa tu nombre: ")
        apellidos = input("Ingresa tu apellido: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = user.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Te has registrado {registro[1].nombre}!")
            print(f"tu email es {registro[1].email}")

        else:
            print("No te has registrado correctamente")

    def login(self):
        print("\nIdentifícate\n")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = user.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}! Te has registrado en el sistema en la fecha {login[5]}")
                self.proxAccion(login)
                
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"login incorrecto, intenta de nuevo")

    def proxAccion(self, usuario):
        print("""
            Acciones disponibles:
            -Crear nota (crear)
            -Mostrar tus notas (mostrar)
            -Eliminar nota (eliminar)
            -Salir (salir)
        """)

        accion = input("¿Qué quieres hacer?: ")
        ejecutar  = notas.acciones.Acciones()

        if accion == "crear":
            ejecutar.crear(usuario)
            self.proxAccion(usuario)

        elif accion == "mostrar":
            ejecutar.mostrar(usuario)
            self.proxAccion(usuario)

        elif accion == "eliminar":
            ejecutar.borrar(usuario)
            self.proxAccion(usuario)
        elif accion == "salir":
            print("Hasta la próxima")
            exit()
        
        return None
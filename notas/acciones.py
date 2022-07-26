import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"{usuario[1]}, vamos a crear una nota!")
        titulo = input("Introduce el titulo de la nota: ")
        descripcion = input("Mete el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Has guardado la nota: '{nota.titulo}'")

        else:
            print(f"{usuario[1]} no se pudo guardar la nota")

    def mostrar(self, usuario):
        print(f"{usuario[1]}, estas son tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n*************************************************")
            print(nota[2])
            print(nota[3])
            print("\n*************************************************")

    def borrar(self, usuario):
        print = (f"Hola {usuario[1]}! Aqui debes borrar tus notas")

        titulo = input("introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)

        eliminar = nota.eliminar()
        borrado = "Se ha borrado la nota"
        if eliminar[0] >= 1:
            print(borrado)
        else:
            print("No se ha borrado la nota")
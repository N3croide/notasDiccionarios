menu = "1. Registrar Alumno\n2. Registrar Nota\n3. Buscar un estudiante\n4. Mostrar notas\n5. Salir\n "
subMenuNotas = "1. Parciales\n2. Quices\n3. Trabajos\n4. Ingresar notas de otro estudiante\n5. Volver al menu anterior"


def menuPrincipal() -> int:
    print(menu)
    while(True):
        try:
            return int(input("Seleccione una opcion: "))
        except ValueError:
            print("Seleccione un valor valido del menu ")

def menuNotas() -> int:
    print(subMenuNotas)
    try:
        return int(input("Seleccione una opcion: "))
    except ValueError:
        print("Seleccione un valor valido del menu")

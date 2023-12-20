import os
pausa = lambda : input("\nPresione enter para continuar...")
borrarPantalla = lambda : os.system("clear")

def regAlumno() -> dict:
    codigo = input("Ingrese el codigo del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input(f"Ingrese la edad del estudiante {nombre}: "))
    alumno = {
        "codigo" : codigo,
        "nombre" : nombre,
        "edad  " : edad,
        "notas" : {
            "parciales" : [],
            "quices" : [],
            "trabajos" : []
        }
    }
    alumnoRegistrado = {codigo: alumno}
    print(alumnoRegistrado)
    return alumnoRegistrado

def buscarAlumno(alumnos : dict) -> dict:
    codAlumno = input("Ingrese el codigo del alumno: ")
    data = alumnos.get(codAlumno,-1)
    if (type(data) == dict):
        return data
    elif(data != None):
        print("No se encontro un estudiante con ese codigo")
        pausa()
    else:
        print("Debe haber almenos un estudiante registrado")
        pausa()

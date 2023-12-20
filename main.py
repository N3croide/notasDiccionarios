import alumnos as al
import menus as menu
import notas as notas
import os

pausa = lambda : input("\nPresione enter para continuar....")
borrarPantalla = lambda : os.system("clear") 
alumnos = {}
isActive = True
opMenu = 0
while(isActive):
    borrarPantalla()
    opMenu = menu.menuPrincipal()

    #Registrar estudiante
    if(opMenu == 1):
        registrarOtroEstudiante = "S"
        while(registrarOtroEstudiante in ["S","s"]):
            borrarPantalla()
            alumnos.update(al.regAlumno())
            pausa()
            registrarOtroEstudiante = input("Desea registrar otro estudiante?. S(si) o N(no)")

    #Ingresar Notas
    elif(opMenu == 2):
        opNotas = 0
        otroEstudiante = "s"
        while(otroEstudiante in "Ss"):
            borrarPantalla()
            estudiante = al.buscarAlumno(alumnos)
            if (estudiante != None):
                ingresarMasNotas = True
                while (ingresarMasNotas):
                    opNotas = menu.menuNotas()
                    if opNotas in [1,2,3]:
                        notas.ingresarNotas(opNotas, estudiante)
                    elif( opNotas == (4 or 5)):
                        ingresarMasNotas = False  
                    else:
                        print("Ingrese una opcion valida.")
            else:
                otroEstudiante = "n"
        if (opNotas == 5):
            break
    #Buscar Estudiante
    elif(opMenu == 3):
        al.buscarAlumno(alumnos)
        
    #Mostrar Notas
    elif(opMenu == 4):
        isActive = False

    #Salir
    elif(opMenu == 5):
        isActive = False
    else:
        print("Seleccione una opcion valida del 1 al 5")
os.system("clear")


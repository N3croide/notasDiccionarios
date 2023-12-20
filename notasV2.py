import menus,os 

pausa = lambda : input("Presione enter para continuar")
borrarPantalla = lambda : os.system("cls")

def ingresarNotas(opNotas : int, estudiante : dict):
    
    tipoNota = ""
    masNotas = "s"
    print(estudiante)
    while(masNotas in "Ss"):
        if(opNotas == 1):
            tipoNota = "parciales"
        elif(opNotas == 2):
            tipoNota = "quices"
        elif(opNotas == 3):
            tipoNota = "trabajos"

        nota = float(input(f"Ingrese la nota {(len(estudiante.get('notas').get(tipoNota)))+1} de {tipoNota}: "))
        estudiante.get("notas").get(tipoNota).append(nota)
        print(estudiante)
        masNotas = input("¿Quiere ingresar otra nota? S(si) N(n)")

import menus,os 

pausa = lambda : input("Presione enter para continuar")
borrarPantalla = lambda : os.system("clear")

def ingresarNotas(opNotas : int, estudiante : dict):
    
    tipoNota = ""
    masNotas = "s"
    while(masNotas in "Ss"):
        if(opNotas == 1):
            tipoNota = "parciales"
        elif(opNotas == 2):
            tipoNota = "quices"
        elif(opNotas == 3):
            tipoNota = "trabajos"

        nota = float(input(f"Ingrese la nota {(len(estudiante.get('notas').get(tipoNota)))+1} de {tipoNota}: \n"))
        estudiante.get("notas").get(tipoNota).append(nota)
        print(estudiante)
        masNotas = input("\n¿Quiere ingresar otra nota? S(si) N(n)")

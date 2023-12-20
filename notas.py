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

        nota = float(input(f"Ingrese la nota {(len(estudiante.get('notas').get(tipoNota)))+1} de {tipoNota}: "))
        estudiante.get("notas").get(tipoNota).append(nota)
        print(estudiante)
        masNotas = input(f"\n¿Quiere ingresar otra nota de {tipoNota}? S(si) N(n)")
        borrarPantalla()

def mostrarNotas(alumnos : dict):
    totalNotas = {
        "parciales" : [],
        "quices" : [],
        "trabajos" : []
    }
    porcentajes = {"parciales" : 0.6, "quices" : 0.25, "trabajos" : 0.15}
    for key,value in alumnos.items():
        for identificador,valores in value.items():
            totalTemp = float(0)
            if (type(valores) == dict):
                for tipoNota in valores:
                    totalTemp = sum(valores.get(tipoNota)) 
                    totalNotas.get(tipoNota).append(float((totalTemp/len(valores.get(tipoNota)))) * float(porcentajes.get(tipoNota)))
            if type(valores) != dict:
                print(f"{identificador} --- {valores}")
            else:
                for tipoNota,valoresNotas in valores.items():
                    print(f"total nota {tipoNota} \n   {valoresNotas}  ->{totalNotas.get(tipoNota)}")
    pausa()
        
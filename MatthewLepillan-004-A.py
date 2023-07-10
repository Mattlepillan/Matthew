import numpy as np
from datetime import date

""" Funciones  """

def menu():
    while True:
        try:
            print("CREATIVOS.CL\n \nMenu Principal: ")
            opcion = int(input("1.Comprar entradas\n2.Mostrar ubicaciones disponibles\n3.Ver listado de asistentes\n4.Mostrar ganancias totales\n5.Salir\n"))
            if opcion == True:
                return opcion
            else:
                print("Opcion no valida ")
        except:
            print("Caracter invalido ")

# Validaciones

def datos_Asis(message, tipo=False, asiento=False, run=False):
    while True:
        try:
            datosAsis = input(message)
            #Validacion tipo
            if tipo == True:
                if datosAsis.isdigit() == True:
                    datosAsis = int(datosAsis)
                else:
                    raise ValueError 

                if datosAsis in range(1,11):
                    pass
                else:
                    print("Numero de asiento invalido" )
                    continue
                #Validacion asiento
                if asiento == True:
                    if datosAsis.isdigit() == True:
                        datosAsis = int(datosAsis)
                    else:
                        raise ValueError   
            # Validacion run
            elif run == True:
                datosAsis = datosAsis.upper()

                if len(datosAsis) != 12:
                    print("Formato no valido ")
                    continue
                elif datosAsis[2] != "." or datosAsis[6] != "." or datosAsis[10] != ".":
                    print("Formato invalido ")
                    continue
                elif datosAsis[11] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'K']:
                    print("Formato no valido")
                    continue
            return datosAsis
        except ValueError:
            print("Caracter invalido")

def comprar_Entradas():
    while True:
        print("Precios:\n-Platinum: 120.000 UF\n-Gold: 80.000 UF\n-Silver: 50.800 UF ")
        tipo = datos_Asis("ingrese el tipo:\n1.Platinium\n2.Gold\n3.Silver\n")
        asiento = datos_Asis("Ingrese el número de asiento (1 al 100):" , asiento=True )


        

        run = datos_Asis("Ingrese su RUN: ", run=True)
        run = run.replace('-', '').replace('.', '').replace(run[-1], '')
        
        listaAsistentes.append(run)
        return
    
def mostrar_ubicaciones_disp():
    print("\n    ESCENARIO     ")
    print(" ----------------")
    print("1  2  3  4  5  6  7  8  9  10")
    print("11 12 13 14 15 16 17 18 19 20")
    print("21 22 23 24 25 26 27 28 29 30")
    print("31 32 33 34 35 36 37 38 39 40")
    print("41 42 43 44 45 46 47 48 49 50")
    print("51 52 53 54 55 56 57 58 59 60")
    print("61 62 63 64 65 66 67 68 69 70")
    print("71 72 73 74 75 76 77 78 79 80")
    print("81 82 83 84 85 86 87 88 89 90")
    print("91 92 93 94 95 96 97 98 99 100")
    print("")

  

def mostrar_Ganancias_totales():
    Platinum = int(0)
    Gold     = int(0)
    Silver   = int(0)

    for i in range(101):
       if matrizAsi[i, 0] == "X":
           Platinum += 1
       if matrizAsi[i, 1] == "X":
            Gold += 1
       if matrizAsi[i, 2] == "X":
            Silver += 1 

    cantTotal = Platinum + Gold + Silver 
    sumTotal = Platinum * 120000 + Gold * 80000 + Silver * 50000 
    print("\nTipo de Departamento | Cantidad | Total")
    print("---------------------+----------+------")
    print(f"Platinum 120.000 UF        {Platinum:4d}     | {Platinum*120000} UF")
    print("---------------------+----------+------")
    print(f"Gold      80.000 UF        {Gold:4d}         | {Gold*80000} UF")
    print("---------------------+----------+------")
    print(f"Silver    50.000 UF        {Silver:4d}       | {Silver*50000} UF")
    print("---------------------+----------+------")
    print(f"TOTAL                  {cantTotal:4d}        | {sumTotal} UF")
    print("---------------------+----------+------\n")


def ver_Asistentes():
    listaAsistentes.sort()
    print("Lista Asistentes\n")
    for i in listaAsistentes:
       print(f"{i}")
       print("------------")
    print("") 

def salir():
    print(f"Saliendo...\nMatthew Lepillán\n{date.today()}")
    menu = 0
    return


""" PROGRAMA PRINCIPAL """

menuu = int(1)
matrizAsi = np.empty((10, 10), dtype=object)
matrizAsi.fill("")

listaAsistentes = []

while menuu == 1:
    opcion = menu()

    match opcion:
        case 1:
            mostrar_ubicaciones_disp()
            comprar_Entradas()
        case 2:
            mostrar_ubicaciones_disp()
        case 3:
            ver_Asistentes()
        case 4:
            mostrar_Ganancias_totales()
        case 5:
            menuu = salir()        














    



           


















                












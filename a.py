import os, time
sw=1

while(sw==1):
    os.system("cls")
    print("           LIBRERÍA")
    print("1. Cuaderno       -        $900")
    print("2. Pintura        -        $1000")
    print("3. Estuche        -        $2000")
    print("4. Finalizar Compra")
    print("5. Salir")

    try:
        op=int(input("Elija su opción:\n\n"))

        if op==1:  
            cC = int(input("Ingrese la cantidad de cuadernos que comprara: "))
            while cC < 1:
                print("Ingrese un valor positivo")
                cC = int(input("Ingrese la cantidad de cuadernos que comprara: "))
            pC = 900 * cC
            total = total + pC
        elif op==2:
            cP = int(input("Ingrese la cantidad de pinturas que comprara: "))
            while cP < 1:
                print("Ingrese un valor positivo")
                cP = int(input("Ingrese la cantidad de pinturas que comprara: "))
            pP = 1000 * cP
            total = total + pP
        elif op==3:
            cE = int(input("Ingrese la cantidad de estuches que comprara: "))
            while cE < 1:
                print("Ingrese un valor positivo")
                cE = int(input("Ingrese la cantidad de estuches que comprara: "))
            pE = 2000 * cE
            total = total + pE
        elif op==4:
            nombre=input("Ingrese su Nombre: ")
            print("-------Boleta-------")
            print(f"Sr/a {nombre}")
            print("-----------------")
            if cC!=0:
                print(f"Cuadernos: {cC} - Precio: ${pC}")
            if cP!=0:
                print(f"Pinturas: {cP} - Precio: ${pP}")
            if cE!=0:
                print(f"Estuches: {cE} - Precio: ${pE}")
            print(f"Total: {total}")
            total = 0
            cP = 0
            cE = 0
            cC = 0
        elif op==5:
            print("Cerrando programa...")
            time.sleep(0.5)
            sw=0
        else:
            print("Opción Incorrecta")
    except:
        print("Intente Nuevamente")
        time.sleep(0.5)
    

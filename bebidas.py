#Hace un menú de bebidas que puedas ingresar las que quieras con nombre y precio
#Y un menú que puedas borrar, agregar, buscar o renombrar

from operator import itemgetter

diccionario = {}

while True:       
    print("\n\t.:Operador de Bebidas:.")
    print("\n1.- Agregar Bebida") 
    print("2.- Borrar Bebida")
    print("3.- Mostrar todas las bebidas")
    print("4.- Buscar Bebida especifica")
    print("5.- Renombrar Bebida")
    print("6.- Salir")

    opcion = int(input("\nOpcion: "))

    #Agregando una bebida

    if opcion==1:
        nuevaBebida = input("\nDigite el nombre de la bebida: ")
        nuevoPrecio = input("Digite el precio de la bebida: ")

        if nuevaBebida not in diccionario:
            diccionario[nuevaBebida] = nuevoPrecio
            print(f"\nLa bebida {nuevaBebida} a sido agregada con exito")
        
        else:
            print("\nEsa bebida ya existe")
    
    #Borrando una bebida

    elif opcion==2:
        borrarBebida = input("\nDigite la bebida que desea eliminar: ")

        if borrarBebida in diccionario:
            print(f"\nLa bebida {borrarBebida} a sido eliminada con exito")
            del(diccionario[borrarBebida])

        else:
            print("\nEsa bebida no existe")

    #Mostrando todas las bebidas

    elif opcion==3:

        #Ordenando alfabeticamente
        diccionario = dict(sorted(diccionario.items(), key=itemgetter(0)))

        print("\n\tLista de bebidas")

        for clave,valor in diccionario.items():
            print(f"Bebida: {clave} - Precio: ${valor}")

    #Buscando una bebida especifica

    elif opcion==4:

        busqueda = input("\nDigite la bebida que desea buscar: ")
        resultado = diccionario.get(busqueda,"Esa bebida no existe")

        for clave,valor in diccionario.items():
            print(f"Bebida: {clave} - Precio: ${valor}")

    #Renombrando una bebida

    elif opcion==5:
        nombreBebida = input("\nDigite el nombre de la bebida que desea renombrar: ")

        if nombreBebida in diccionario:
            renombrarBebida = input("Digite el nuevo nombre de la bebida: ")

            if renombrarBebida not in diccionario:
                print(f"\nLa bebida {nombreBebida} a sido remplazada por {renombrarBebida}")
                diccionario[renombrarBebida] = diccionario[nombreBebida]
                del(diccionario[nombreBebida])

            else:
                print("\nEsa bebida ya existe")

        else:
            print("\nEsa bebida no existe")

    #Saliendo del programa

    elif opcion==6:
        print("\nFinalizando programa")
        print()
        break

    else:
        print("Opcion incorrecta")
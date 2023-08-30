import os

def iniciar():
    while True:
        os.system('cls')
        print("===============================")
        print("     Bienvenidos al gestor     ")
        print("===============================")
        print(" [1] Listar los clientes ")
        print(" [2] Buscar un cliente ")
        print(" [3] Añadir un cliente ")
        print(" [4] Modificar un cliente ")
        print(" [5] Borrar un cliente ")
        print(" [0] Salir ")
        print("===============================")
        opcion = input("Opcion > ")
        os.system('cls')

        if opcion == '1':
            print("Listar clientes... ")
            # TODO
        elif opcion == '2':
            print("Buscar cliente... ")
            # TODO
        elif opcion == '3':
            print("Añadir cliente... ")
            # TODO
        elif opcion == '4':
            print("Modificar cliente... ")
            # TODO
        elif opcion == '5':
            print("Borrar cliente... ")
            # TODO
        elif opcion == '0':
            print("Salir... ")
            break
        else:
            print("Opcion incorrecta, por favor introduzca una opcion valida... ")
            iniciar()
        input("\n     Hasta pronto!     ")
        input("\nPresione ENTER para continuar...")
import os

def pausar_app():
    return input("Presione ENTER para continuar...")

def limpiar_app():
    #TODO : aca vamos a limpiar la pantalla de la app
    pass

def iniciar_app():
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
            pausar_app()
            # TODO
        elif opcion == '2':
            print("Buscar cliente... ")
            pausar_app()
            # TODO
        elif opcion == '3':
            print("Añadir cliente... ")
            pausar_app()
            # TODO
        elif opcion == '4':
            print("Modificar cliente... ")
            pausar_app()
            # TODO
        elif opcion == '5':
            print("Borrar cliente... ")
            pausar_app()
            # TODO
        elif opcion == '0':
            print("Salir... ")
            input("\nHasta pronto! \nPresione ENTER para continuar...")
            break
        else:
            print("Opcion incorrecta, por favor introduzca una opcion valida...")
            pausar_app()
            iniciar_app()
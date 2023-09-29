import os

def pausar_app():
    return input("Presione ENTER para continuar...")

def limpiar_app():
    return os.system('cls')

def iniciar_app():
    while True:
        limpiar_app()
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
        limpiar_app()

        if opcion == '1':
            print("Listar clientes... ")
            pausar_app()
            # TODO: debemos crear la funcion para listar a los clientes guardados en clientes.csv
        elif opcion == '2':
            print("Buscar cliente... ")
            pausar_app()
            # TODO: crear el buscador para mostrar datos del cliente segun su RUT
        elif opcion == '3':
            print("Añadir cliente... ")
            pausar_app()
            # TODO: crear funcion para insertar/crear un cliente nuevo
        elif opcion == '4':
            print("Modificar cliente... ")
            pausar_app()
            # TODO: crear funcion para modificar/editar un cliene existente
        elif opcion == '5':
            print("Borrar cliente... ")
            pausar_app()
            # TODO: crear funcion para borrar cliente de la DB clientes.csv
        elif opcion == '0':
            print("Salir... ")
            print("\nHasta pronto!\n")
            pausar_app()
            break
        else:
            print("Opcion incorrecta, por favor introduzca una opcion valida...")
            pausar_app()
            iniciar_app()
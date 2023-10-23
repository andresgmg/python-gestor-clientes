import helpers
import db

def iniciar_app():
    while True:
        helpers.limpiar_app()
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
        helpers.limpiar_app()

        if opcion == '1':
            print("Listando los clientes... ")
            for cliente in db.Clientes.lista:
                print(cliente)
            helpers.pausar_app()
        elif opcion == '2':
            print("Buscando un cliente... ")
            rut = helpers.leer_texto(6,10,"ingrese un rut valido (con guion)").upper()
            cliente = db.Clientes.buscar(rut)
            print(cliente) if cliente else print("cliente no encontrado!")
            helpers.pausar_app()
        elif opcion == '3':
            print("Añadir cliente... ")
            while True:
                rut = helpers.leer_texto(6,10,"ingrese un rut valido (con guion)").upper()
                valido = helpers.rut_validator(rut, db.Clientes.lista)
                if valido:
                    break
            nombre = helpers.leer_texto(1,30,"Nombre (de 2 a 30 char)").capitalize()
            apellido = helpers.leer_texto(1,30,"Apellido (de 2 a 30 char)").capitalize()
            db.Clientes.crear(rut, nombre, apellido)
            print("Cliente añadido correctamente!")
            helpers.pausar_app()
        elif opcion == '4':
            print("Modificar cliente... ")
            rut = helpers.leer_texto(6,10,"ingrese un rut valido (con guion)").upper()
            cliente = db.Clientes.buscar(rut)
            if cliente:
                nombre = helpers.leer_texto(1,30,"Nombre (de 2 a 30 char) [{}]".format(cliente.nombre)).capitalize()
                apellido = helpers.leer_texto(1,30,"Apellido (de 2 a 30 char) [{}]".format(cliente.apellido)).capitalize()
                db.Clientes.modificar(cliente.rut, nombre, apellido)
                print("cliente {} modificado!".format(cliente.rut))
            else:
                print("cliente no encontrado!")
            helpers.pausar_app()
        elif opcion == '5':
            print("Borrar cliente... ")
            rut = helpers.leer_texto(6,10,"ingrese un rut valido (con guion)").upper()
            print("Cliente eliminado!") if db.Clientes.borrar(rut) else print("Cliente no encontrado!")
            helpers.pausar_app()
        elif opcion == '0':
            print("Salir... ")
            print("\nHasta pronto!\n")
            helpers.pausar_app()
            break
        else:
            print("Opcion incorrecta, por favor introduzca una opcion valida...")
            helpers.pausar_app()
            iniciar_app()
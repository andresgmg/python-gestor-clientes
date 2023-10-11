import csv

class Cliente:
    def __init__(self, rut, nombre, apellido):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.rut}) {self.nombre} {self.apellido}"

class Clientes:
    lista = []
    with open('clientes.csv', newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=',')
        for rut, nombre, apellido in reader:
            cliente = Cliente(rut, nombre, apellido)
            lista.append(cliente)

    @staticmethod
    def buscar(rut):
        for cliente in Clientes.lista:
            if cliente.rut == rut:
                return cliente

    @staticmethod
    def crear(rut, nombre, apellido):
        cliente = Cliente(rut, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar_csv()
        return cliente

    @staticmethod
    def modificar(rut, nombre, apellido):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.rut == rut:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].apellido = apellido
                Clientes.guardar_csv()
                return cliente

    @staticmethod
    def borrar(rut):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.rut == rut:
                cliente = Clientes.lista.pop(i)
                Clientes.guardar_csv()
                return cliente

    @staticmethod
    def guardar_csv():
        with open("clientes.csv", "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=",")
            for cliente in Clientes.lista:
                writer.writerow((cliente.rut, cliente.nombre, cliente.apellido))
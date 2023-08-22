class Cliente:
    def __init__(self, rut, nombre, apellido):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.rut}) {self.nombre} {self.apellido}"

class Clientes:
    lista = []

    @staticmethod
    def buscar(rut):
        for cliente in Clientes.lista:
            if cliente.rut == rut:
                return cliente

    @staticmethod
    def crear(rut, nombre, apellido):
        cliente = Cliente(rut, nombre, apellido)
        Clientes.lista.append(cliente)
        return cliente

    @staticmethod
    def modificar(rut, nombre, apellido):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.rut == rut:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].apellido = apellido
                return Clientes.lista[i]

    @staticmethod
    def borrar(rut):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.rut == rut:
                return Clientes.lista.pop[i]
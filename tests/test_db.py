import unittest
import db
import copy

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('15K', 'Marta', 'Perez'),
            db.Cliente('16K', 'manolo', 'lopez'),
            db.Cliente('18K','Ana', 'Garcia')
        ]
        return super().setUp()

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('15K')
        cliente_inexistente = db.Clientes.buscar('20M')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('10A', 'Andres', 'Marquez')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.rut, '10A')
        self.assertEqual(nuevo_cliente.nombre, 'Andres')
        self.assertEqual(nuevo_cliente.apellido, 'Marquez')

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('18K'))
        cliente_modificado = db.Clientes.modificar('18K', 'Andres', 'Marquez')
        self.assertEqual(cliente_a_modificar.nombre, 'Ana')
        self.assertEqual(cliente_modificado.nombre, 'Andres')
        self.assertEqual(cliente_a_modificar.apellido, 'Garcia')
        self.assertEqual(cliente_modificado.apellido, 'Marquez')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('16K')
        cliente_rebuscado = db.Clientes.buscar('16K')
        self.assertEqual(len(db.Clientes.lista), 2)
        self.assertEqual(cliente_borrado.rut, '16K')
        self.assertIsNone(cliente_rebuscado)
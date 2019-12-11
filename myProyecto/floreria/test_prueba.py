import unittest
from prueba import probar_usuario,probar_contraseña

class TestProbar_usuario(unittest.TestCase):
    def test_usuario(self):
        self.assertAlmostEqual(probar_usuario('Floreria'),'Floreria')

class TestProbar_contraseña(unittest.TestCase):
    def test_contraseña(self):
        self.assertAlmostEqual(probar_contraseña(123),123)

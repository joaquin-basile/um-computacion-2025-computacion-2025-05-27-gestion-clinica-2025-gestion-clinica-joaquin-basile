import unittest
from models.especialidad import Especialidad
from constants.dias import Dia

class TestEspecialidad(unittest.TestCase):
    def test_get_especialidad(self):
        especialidad1 = Especialidad("Pediatra", [Dia.lunes])
        self.assertEqual(especialidad1.get_especialidad(), "Pediatra")

    def test_get_dias(self):
        especialidad1 = Especialidad("Pediatra", [Dia.lunes, Dia.martes])
        dias = especialidad1.get_dias()
        self.assertIn(Dia.lunes, dias)
        self.assertIn(Dia.martes, dias)

    def test_verificar_dia(self):
        especialidad1 = Especialidad("Pediatra", [Dia.lunes, Dia.martes])
        self.assertTrue(especialidad1.verificar_dia(Dia.lunes))
        self.assertFalse(especialidad1.verificar_dia(Dia.miercoles))


if __name__ == '__main__':
    unittest.main() 

import unittest
from models.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_get_dni(self):
        dni = "45.123.412"
        p1 = Paciente("Juan", dni, "02/03/2005")
        self.assertEqual(p1.get_dni(), dni)
    def test_str(self):
        p1 = Paciente("Juan", "54.234.123", "02/03/2005")
        self.assertEqual(str(p1), "Paciente: Juan, DNI: 54.234.123, Fecha de Nacimiento: 02/03/2005")

if __name__ == '__main__':
    unittest.main() 

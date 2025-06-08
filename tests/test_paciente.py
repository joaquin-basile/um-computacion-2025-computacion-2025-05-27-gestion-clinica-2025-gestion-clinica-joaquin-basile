import unittest
from models.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_get_dni(self):
        dni = "45.123.412"
        p1 = Paciente("Juan", dni, "02/03/2005")
        self.assertEqual(p1.get_dni(), dni)

if __name__ == '__main__':
    unittest.main() 

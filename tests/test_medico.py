import unittest
from models.medico import Medico
from models.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def test_str(self):
        cardiologo = Especialidad("Cardiologo")
        pediatra = Especialidad("Pediatra")
        d1 = Medico("Dr. Smith", "123456", [cardiologo, pediatra])
        expected_str = "Medico: Dr. Smith\n Matricula: 123456 \n Especialidades:\n - Cardiologo\n - Pediatra"
        self.assertEqual(str(d1), expected_str)


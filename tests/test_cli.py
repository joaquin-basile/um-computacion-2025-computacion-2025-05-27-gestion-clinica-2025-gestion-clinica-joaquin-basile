import unittest
import sys
from models.cli import CLI
from unittest.mock import patch
from io import StringIO

from exceptions.errors import MedicoNoEncontradoException

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()
    
    @patch('builtins.input', side_effect=['123', 'Cardiologia', 'lunes, martes'])
    def test_agregar_especialidad_medico_no_registrado(self, mock_input):
        with self.assertRaises(MedicoNoEncontradoException) as e:
            self.cli.agregar_especialidad_por_matricula()
        self.assertEqual("No existe médico con matrícula 123", str(e.exception))


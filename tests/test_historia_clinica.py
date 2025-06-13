from models.historia_clinica import HistoriaClinica
from models.paciente import Paciente
from models.turno import Turno
from models.receta import Receta
from models.medico import Medico
from models.especialidad import Especialidad
from constants.dias import Dia
from datetime import datetime
import unittest

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "02/02/2005")
        self.medico = Medico(
            "Dr. Smith",
            "98765432",
            [
                Especialidad("Pediatria"), [Dia.lunes]
            ]
        )
        self.turno1 = Turno(self.paciente, self.medico, datetime(2025,6,14,10,40), "Pediatria")
        self.turno2 = Turno(self.paciente, self.medico, datetime(2025,6,20,12,30), "Pediatria")
        self.receta1 = Receta(self.paciente, self.medico, ["Ibuprofeno"], datetime(2025,6,14,11,40))
        self.receta2 = Receta(self.paciente, self.medico, ["Flenaler Cort"], datetime(2025,6,20,13,40))
        self.historia_clinica = HistoriaClinica(self.paciente, [self.turno1], [self.receta1])

    def test_get_turnos(self):
        self.assertEqual(self.historia_clinica.get_turnos(), [self.turno1])

    def test_get_recetas(self):
        self.assertEqual(self.historia_clinica.get_recetas(), [self.receta1])

    def test_agregar_turno(self):
        self.historia_clinica.agregar_turno(self.turno2)
        self.assertEqual(self.historia_clinica.get_turnos(), [self.turno1, self.turno2])

    def test_agregar_receta(self):
        self.historia_clinica.agregar_receta(self.receta2)
        self.assertEqual(self.historia_clinica.get_recetas(), [self.receta1, self.receta2])



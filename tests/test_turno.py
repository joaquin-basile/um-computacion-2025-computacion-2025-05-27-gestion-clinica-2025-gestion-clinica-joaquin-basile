import unittest
from models.medico import Medico
from models.especialidad import Especialidad
from models.paciente import Paciente
from models.turno import Turno
from datetime import datetime

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.medico1 = Medico("Dr. Juan Perez", "12345", [
            Especialidad("Cardiología", ["Lunes", "Miércoles"]),
            Especialidad("Neurología", ["Martes", "Jueves"])
        ])
        self.paciente1 = Paciente("Ana Gómez", "12345678", "01/11/2000")
        self.fecha_hora = datetime(2025, 6, 10, 10, 30)
        self.turno1 = Turno(self.paciente1, self.medico1, self.fecha_hora, "Cardiología")


    def test_str(self):
        expeted_str = f"Turno: \nPaciente: Ana Gómez \nMedico: Dr. Juan Perez \nEspecialidad: Cardiología \nFecha/hora: {self.fecha_hora}"
        self.assertEqual(str(self.turno1), expeted_str)

    def test_get_medico(self):
        self.assertEqual(self.medico1, self.turno1.get_medico())

    def test_get_fecha_hora(self):
        self.assertEqual(self.fecha_hora, self.turno1.get_fecha_hora())

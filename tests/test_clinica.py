import unittest
from models import clinica, medico, especialidad, paciente, turno
from constants.dias import Dia
from exceptions.errors import PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException, RecetaInvalidaException, MedicoNoEncontradoException
from datetime import datetime

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica1 = clinica.Clinica()
        self.medico1 = medico.Medico("Dr. Juan Perez", "12345", [especialidad.Especialidad("Cardiología", [Dia.lunes])])
        self.paciente1 = paciente.Paciente("Ana Gómez", "12345678", "01/11/2000")

    #Test paciente
    def test_agregar_paciente(self):
        self.clinica1.agregar_paciente(self.paciente1)
        self.assertEqual(self.clinica1.get_pacientes()[0], self.paciente1)
        # Test paciente duplicado
        with self.assertRaises(ValueError):
            self.clinica1.agregar_paciente(self.paciente1)
        #Test paciente vacio 
        with self.assertRaises(ValueError):
            self.clinica1.agregar_paciente(paciente.Paciente("", "", ""))

    def test_validar_paciente(self):
        self.clinica1.agregar_paciente(self.paciente1)
        dni = self.paciente1.get_dni()
        self.assertIsNone(self.clinica1.validar_existencia_paciente(dni))
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica1.validar_existencia_paciente("")

    #Test medico
    def test_agregar_medico(self):
        self.clinica1.agregar_medico(self.medico1)
        self.assertEqual(self.clinica1.get_medicos(), [self.medico1])

        #Test medico duplicado
        with self.assertRaises(ValueError):
            self.clinica1.agregar_medico(self.medico1)
        #Test medico vacio
        with self.assertRaises(ValueError):
            self.clinica1.agregar_medico(Medico("", ""))

    def test_get_medico_por_matricula(self):
        self.clinica1.agregar_medico(self.medico1)
        medico = self.clinica1.get_medico_por_matricula(self.medico1.get_matricula())
        self.assertEqual(medico, self.medico1)

    def test_validar_medico(self):
        self.clinica1.agregar_medico(self.medico1)
        matricula = self.medico1.get_matricula()
        self.assertIsNone(self.clinica1.validar_existencia_medico(matricula))
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica1.validar_existencia_medico("")

    def test_get_medicos(self):
        self.clinica1.agregar_medico(self.medico1)
        medicos = self.clinica1.get_medicos()
        self.assertEqual(len(medicos), 1)
        self.assertEqual(medicos[0].get_matricula(), self.medico1.get_matricula())

    #Test especialidad
    def test_agregar_especialidad(self):
        self.clinica1.agregar_medico(self.medico1)
        with self.assertRaises(ValueError) as e:
            self.clinica1.agregar_especialidad(self.medico1, "Pediatria", ["", "MARTES", "miercoles", "miercoles", "juebebes"])

        especialidades = self.medico1.get_especialidades()
        self.assertEqual(especialidades[])

        



    #Test receta
    def test_emitir_receta(self):
        self.clinica1.agregar_paciente(self.paciente1)
        self.clinica1.agregar_medico(self.medico1)
        self.clinica1.emitir_receta(self.paciente1.get_dni(), self.medico1.get_matricula(), ["Aspirina"])
        recetas = self.clinica1.get_historia_clinica_por_dni(self.paciente1.get_dni()).get_recetas()
        self.assertEqual(len(recetas), 1)

        with self.assertRaises(RecetaInvalidaException):
            self.clinica1.emitir_receta("", "", "")

    #Test turnos
    def test_agregar_turno(self):
        self.clinica1.agregar_paciente(self.paciente1)
        self.clinica1.agregar_medico(self.medico1)
        turno_un_lunes = datetime(2025,6,16,10,30)
        self.clinica1.agendar_turno(self.paciente1.get_dni(), self.medico1.get_matricula(), "Cardiología", turno_un_lunes)
        turnos = self.clinica1.get_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].get_medico(), self.medico1)
        
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica1.agendar_turno("", self.medico1.get_matricula(), "Cardiología", turno_un_lunes)

        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica1.agendar_turno(self.paciente1.get_dni(), "", "Cardiología", turno_un_lunes)

        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica1.agendar_turno(self.paciente1.get_dni(), self.medico1.get_matricula(), "", turno_un_lunes)

        turno_un_martes = datetime(2025,6,17,10,30)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica1.agendar_turno(self.paciente1.get_dni(), self.medico1.get_matricula(), "Cardiología", turno_un_martes)
        
        with self.assertRaises(TurnoOcupadoException):
            self.clinica1.agendar_turno(self.paciente1.get_dni(), self.medico1.get_matricula(), "Cardiología", turno_un_lunes)



if __name__ == '__main__':
    unittest.main() 

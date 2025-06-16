import unittest
from models.medico import Medico, DiaOcupadoException, EspecialidadExistenteException
from models.especialidad import Especialidad
from constants.dias import Dia

class TestMedico(unittest.TestCase):
    def setUp(self):
        self.cardiologo = Especialidad("Cardiologo", [Dia.lunes, Dia.miercoles])
        self.pediatra = Especialidad("Pediatra", [Dia.martes])

    def test_get_espcialidades(self):
        medico1 = Medico("Dr. Smith", "123456", [self.cardiologo, self.pediatra])
        especialidades = medico1.get_especialidades()
        self.assertIn(self.cardiologo, especialidades)
        self.assertIn(self.pediatra, especialidades)

    def test_agregar_especialidad(self):
        medico1 = Medico("Dr. Smith", "123456", [self.cardiologo])
        medico1.agregar_especialidad(self.pediatra)
        especialidades = medico1.get_especialidades()
        self.assertIn(self.pediatra, especialidades)

    def test_agregar_especialidad_existente(self):
        medico1 = Medico("Dr. Smith", "123456", [self.cardiologo])
        with self.assertRaises(EspecialidadExistenteException) as ex:
            medico1.agregar_especialidad(self.cardiologo)
        self.assertEqual(str(ex.exception), "El medico ya tiene la especialidad Cardiologo")
        self.assertEqual(len(medico1.get_especialidades()), 1)

    def test_agregar_especialidad_para_dia_existente(self):
        medico1 = Medico("Dr. Smith", "123456", [self.cardiologo])
        neurologo = Especialidad("Neurologo", [Dia.lunes])
        with self.assertRaises(DiaOcupadoException) as ex:
            medico1.agregar_especialidad(neurologo)
        self.assertEqual(str(ex.exception), "El medico ya atiende otra especialidad el dia lunes")
        self.assertEqual(len(medico1.get_especialidades()), 1)

    def test_get_matricula(self):
        matricula = "123456"
        medico1 = Medico("Dr. Smith", matricula, [self.cardiologo])
        self.assertEqual(medico1.get_matricula(), matricula)

    def test_get_especialidad_para_dia(self):
        medico1 = Medico("Dr. Smith", "123456", [self.cardiologo, self.pediatra])
        self.assertEqual("Cardiologo", medico1.get_especialidad_para_dia(Dia.lunes))
        self.assertEqual("Cardiologo", medico1.get_especialidad_para_dia(Dia.miercoles))
        self.assertEqual("Pediatra", medico1.get_especialidad_para_dia(Dia.martes))
        self.assertIsNone(medico1.get_especialidad_para_dia(Dia.domingo))


if __name__ == '__main__':
    unittest.main() 

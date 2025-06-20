from datetime import datetime
from models.paciente import Paciente
from models.medico import Medico
class Turno ():
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        self.__fecha_hora = fecha_hora
        self.__paciente = paciente
        self.__medico = medico
        self.__especialidad = especialidad

    def get_medico(self):
        return self.__medico

    def get_fecha_hora(self):
        return self.__fecha_hora
    def __str__(self):
        return (
            "Turno(\n"
            f"  {str(self.__paciente)},\n"
            f"  {str(self.__medico)},\n"
            f"  Fecha y hora: {self.__fecha_hora.strftime('%Y-%m-%d %H:%M:%S')},\n"
            f"  Especialidad: {self.__especialidad}\n"
            ")"
        )

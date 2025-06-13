from models.paciente import Paciente
from models.medico import Medico
from datetime import datetime

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str], fecha_emision: datetime):
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha_emision = fecha_emision

    # def __str__(self):
    #     return f"Receta({str(self.__paciente)}, \n{str(self.__medico)}), \n{self.__medicamentos}, \n{self.__fecha_emision}\n)"
    

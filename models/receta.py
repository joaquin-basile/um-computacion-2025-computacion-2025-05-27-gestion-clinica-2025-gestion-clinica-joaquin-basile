from models.paciente import Paciente
from models.medico import Medico
from datetime import datetime

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str], fecha_emision: datetime):
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha_emision = fecha_emision

    def __str__(self):
        medicamentos_str = ", ".join(self.__medicamentos)
        return (
            "Receta(\n"
            f"  {str(self.__paciente)},\n"
            f"  {str(self.__medico)},\n"
            f"  Medicamentos: [{medicamentos_str}],\n"
            f"  Fecha de emisión: {self.__fecha_emision.strftime('%Y-%m-%d %H:%M:%S')}\n"
            ")"
        )
    

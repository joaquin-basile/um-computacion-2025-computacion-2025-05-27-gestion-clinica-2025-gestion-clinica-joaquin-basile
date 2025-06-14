from models.paciente import Paciente
from models.turno import Turno
from models.receta import Receta

class HistoriaClinica:
    def __init__(self, paciente: Paciente, turnos: list[Turno], recetas: list[Receta]):
        self.__paciente = paciente
        self.__turnos = turnos
        self.__recetas = recetas

    def agregar_turno(self, turno: Turno):
        self.__turnos.append(turno)

    def get_turnos(self) -> list[Turno]:
        return self.__turnos

    def agregar_receta(self, receta: Receta):
        self.__recetas.append(receta)

    def get_recetas(self):
        return self.__recetas

    def __str__(self):
        turnos_str = "\n    ".join(str(turno) for turno in self.__turnos)
        recetas_str = "\n    ".join(str(receta) for receta in self.__recetas)
        return (
            "HistoriaClinica(\n"
            f"  {str(self.__paciente)},\n"
            f"  Turnos: [\n    {turnos_str}\n  ],\n"
            f"  Recetas: [\n    {recetas_str}\n  ]\n"
            ")"
        )

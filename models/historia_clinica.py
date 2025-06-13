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

    # def __str__(self):
    #     turnos_str = "("
    #     recetas_str = "("
    #     for turno in self.__turnos:
    #         turnos_str += f"\n{str(turno)}"
    #     return f"Historia Clinica(\n {str(self.__paciente)}, \n{turnos_str}, \n{recetas_str})"

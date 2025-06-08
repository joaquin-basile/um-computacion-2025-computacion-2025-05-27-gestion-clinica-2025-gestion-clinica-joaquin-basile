from models.especialidad import Especialidad
class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: list[Especialidad]):
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = especialidades

    def __str__(self):
        medico_str = f"Medico: {self.__nombre}\n Matricula: {self.__matricula} \n Especialidades:"
        for especialidad in self.__especialidades:
            medico_str += f"\n - {especialidad.get_nombre()}"
        return ""

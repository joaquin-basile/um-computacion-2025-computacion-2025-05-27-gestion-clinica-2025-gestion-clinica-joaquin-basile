from models.especialidad import Especialidad
from constants.dias import Dia
from exceptions.errors import DiaOcupadoException, EspecialidadExistenteException


class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: list[Especialidad] = None):
        if nombre == "" or matricula == "":
            raise ValueError("El nombre y la matrícula del médico no pueden estar vacíos.")
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = [] if especialidades is None else especialidades
        

    def get_especialidades(self)-> list[Especialidad]:
        return self.__especialidades.copy()

    def get_matricula(self) -> str:
        return self.__matricula

    def get_nombre(self):
        return self.__nombre

    def agregar_especialidad(self, especialidad: Especialidad):
        for especialidad_existente in self.__especialidades:
            if especialidad.get_especialidad() == especialidad_existente.get_especialidad():
                raise EspecialidadExistenteException(f"El medico ya tiene la especialidad {especialidad.get_especialidad()}")

            for dia in especialidad.get_dias():
                if dia in especialidad_existente.get_dias():
                   raise DiaOcupadoException(f"El medico ya atiende otra especialidad el dia {dia.value}")

        self.__especialidades.append(especialidad)

    def get_especialidad_para_dia(self, dia: Dia)-> str | None:
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia):
                return especialidad.get_especialidad()
        return

    def __str__(self):
        especialidades_str = ",\n    ".join(str(especialidad) for especialidad in self.__especialidades)
        return (
            "Medico(\n"
            f"  Nombre: {self.__nombre},\n"
            f"  Matrícula: {self.__matricula},\n"
            f"  Especialidades: [\n"
            f"    {especialidades_str}\n"
            "  ]\n"
            ")"
    )

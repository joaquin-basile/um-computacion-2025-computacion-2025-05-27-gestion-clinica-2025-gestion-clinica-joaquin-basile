from models.especialidad import Especialidad
from constants.dias import Dia

class DiaOcupadoException(Exception):
    """"Excepción para indicar que un día ya está ocupado por una especialidad."""
    def __init__(self, mensaje="La nueva especialidad no puede ser agregada porque ya existe una especialidad para ese día."):
        super().__init__(mensaje)

class EspecialidadExistenteException(Exception):
    """Excepción para indicar que una especialidad ya existe en la lista de especialidades del médico."""
    def __init__(self, mensaje="La especialidad ya existe en la lista."):
        super().__init__(mensaje)

class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: list[Especialidad]):
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = especialidades

    def get_especialidades(self)-> list[Especialidad]:
        return self.__especialidades

    def get_matricula(self) -> str:
        return self.__matricula

    def get_nombre(self):
        return self.__nombre

    def agregar_especialidad(self, especialidad: Especialidad):
        if especialidad in self.__especialidades:
            raise EspecialidadExistenteException()

        for especialidad_existente in self.__especialidades:
            for dia in especialidad.get_dias():
                if dia in especialidad_existente.get_dias():
                   raise DiaOcupadoException() 
        self.__especialidades.append(especialidad)

    def get_especialidad_para_dia(self, dia: Dia)-> str | None:
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia):
                return especialidad.get_especialidad()
        return


    def __str__(self):
        medico_str = f"Medico: {self.__nombre}\n Matricula: {self.__matricula} \n Especialidades:"
        for especialidad in self.__especialidades:
            medico_str += f"\n - {especialidad.get_especialidad()}"
        return medico_str

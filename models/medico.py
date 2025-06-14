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
                raise EspecialidadExistenteException()

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

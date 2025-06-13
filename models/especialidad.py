from constants.dias import Dia

class Especialidad:
    def __init__(self, tipo: str, dias: list[Dia]):
        self.__tipo = tipo
        self.__dias = dias

    def get_especialidad(self):
        return self.__tipo

    def get_dias(self):
        return self.__dias

    def verificar_dia(self, dia: Dia)-> bool:
        return dia in self.__dias

    def __str__(self):
        dias_str = ", ".join(dia.value for dia in self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"

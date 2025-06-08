class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        self.__nombre = nombre
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento

    def get_dni(self)-> str:
        return self.__dni

    def __str__(self)-> str:
        return ""

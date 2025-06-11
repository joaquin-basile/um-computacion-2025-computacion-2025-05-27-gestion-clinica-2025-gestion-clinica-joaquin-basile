class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        self.__nombre = nombre
        self.__dni = dni
        """fecha_nacimiento debe ser una cadena en formato 'DD/MM/AAAA'."""
        self.__fecha_nacimiento = fecha_nacimiento

    def get_dni(self)-> str:
        return self.__dni

    def get_nombre(self)-> str:
        return self.__nombre

    def __str__(self)-> str:
        return f"Paciente: {self.__nombre}, DNI: {self.__dni}, Fecha de Nacimiento: {self.__fecha_nacimiento}"

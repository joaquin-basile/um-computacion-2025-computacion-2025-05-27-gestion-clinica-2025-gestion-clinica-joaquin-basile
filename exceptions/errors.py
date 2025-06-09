class DatosInsuficientesException(Exception):
    """Excepción para indicar que los datos proporcionados son insuficientes."""
    def __init__(self, mensaje="Faltan los siguientes campos: ",campos_faltantes list[str] ):
        msj = mensaje + ", ".join(campos_faltantes)
        super().__init__(msj)

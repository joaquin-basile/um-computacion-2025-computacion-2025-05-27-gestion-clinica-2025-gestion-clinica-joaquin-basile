class PacienteNoEncontradoException(Exception):
    """Excepción lanzada cuando no se encuentra un paciente."""
    def __init__(self, mensaje="Paciente no encontrado."):
        super().__init__(mensaje)

class MedicoNoDisponibleException(Exception):
    """Excepción lanzada cuando un médico no está disponible."""
    def __init__(self, mensaje="Médico no disponible para la especialidad o día solicitado."):
        super().__init__(mensaje)

class TurnoOcupadoException(Exception):
    """Excepción lanzada cuando un turno ya está ocupado."""
    def __init__(self, mensaje="El turno ya está ocupado para ese médico en esa fecha y hora."):
        super().__init__(mensaje)

class RecetaInvalidaException(Exception):
    """Excepción lanzada cuando una receta es inválida."""
    def __init__(self, mensaje="La receta es inválida."):
        super().__init__(mensaje)

class MedicoNoEncontradoException(Exception):
    """Excepción lanzada cuando no se encuentra un médico."""
    def __init__(self, mensaje="Médico no encontrado."):
        super().__init__(mensaje)


class DiaOcupadoException(Exception):
    """"Excepción para indicar que un día ya está ocupado por una especialidad."""
    def __init__(self, mensaje="El medico ya realiza una especialidad ese dia"):
        super().__init__(mensaje)

class EspecialidadExistenteException(Exception):
    """Excepción para indicar que una especialidad ya existe en la lista de especialidades del médico."""
    def __init__(self, mensaje="La especialidad ya existe en la lista."):
        super().__init__(mensaje)

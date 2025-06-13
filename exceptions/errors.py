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

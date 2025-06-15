# models/clinica.py
from datetime import datetime
from models.paciente import Paciente
from models.medico import Medico
from models.turno import Turno
from models.receta import Receta
from models.historia_clinica import HistoriaClinica
from constants.dias import Dia
from exceptions.errors import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class Clinica:
    def __init__(self):
        self.__pacientes: dict[str, Paciente] = {}
        self.__medicos: dict[str, Medico] = {}
        self.__turnos: list[Turno] = []
        self.__historias_clinicas: dict[str, HistoriaClinica] = {}
    # Setters
    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.get_dni()
        if dni in self.__pacientes:
            raise ValueError(f"El paciente con DNI {dni} ya está registrado.")
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente, [], [])

    def agregar_medico(self, medico: Medico):
        matricula = medico.get_matricula()
        if matricula in self.__medicos:
            raise ValueError(f"El médico con matrícula {matricula} ya está registrado.")
        self.__medicos[matricula] = medico

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        dia_semana = self.datetime_to_dia(fecha_hora)

        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        if not medicamentos:
            raise RecetaInvalidaException("La receta debe contener al menos un medicamento.")

        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        receta = Receta(paciente, medico, medicamentos, datetime.now())

        self.__historias_clinicas[dni].agregar_receta(receta)

    def agregar_especialidad(self, medico: Medico, tipo_especialidad: str, dias: list[str]):
        dias_enum = []
        for dia_str in dias:
            dia_enum = Dia[dia_str]
            dias_enum.append(dia_enum)
        
        if dias_enum:
            especialidad = Especialidad(tipo_especialidad, dias_enum)
            medico.agregar_especialidad(especialidad)
            print("Especialidad agregada exitosamente.")
        else:
            print("No se pudo agregar la especialidad por falta de días válidos.")

    # Getters 
    def get_pacientes(self) -> list[Paciente]:
        return list(self.__pacientes.values())

    def get_medicos(self) -> list[Medico]:
        return list(self.__medicos.values())

    def get_turnos(self) -> list[Turno]:
        return self.__turnos

    def get_medico_por_matricula(self, matricula: str) -> Medico:
        self.validar_existencia_medico(matricula)
        return self.__medicos[matricula]

    def get_historia_clinica_por_dni(self, dni: str) -> HistoriaClinica:
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]

    #Validaciones
    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(f"No existe paciente con DNI {dni}")

    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException(f"No existe médico con matrícula {matricula}")

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for turno in self.__turnos:
            if (turno.get_medico().get_matricula() == matricula and turno.get_fecha_hora() == fecha_hora):
                raise TurnoOcupadoException(
                    f"El médico ya tiene un turno agendado para {fecha_hora}"
                )

    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: Dia):
        especialidad = medico.get_especialidad_para_dia(dia_semana)
        if especialidad is None:
            raise MedicoNoDisponibleException(
                    f"El médico no tiene especialidades asignadas para los {dia_semana.value}"
            )
        if especialidad != especialidad_solicitada:
            raise MedicoNoDisponibleException(
                f"El médico no atiende {especialidad_solicitada} atiende {especialidad}"
            )

    #Utilidades
    def datetime_to_dia(self, fecha_hora: datetime) -> Dia:
        dias_semana = {
            0: Dia.lunes,
            1: Dia.martes,
            2: Dia.miercoles,
            3: Dia.jueves,
            4: Dia.viernes,
            5: Dia.sabado,
            6: Dia.domingo
        }
        return dias_semana[fecha_hora.weekday()]

    def get_especialidad_disponible(self, medico: Medico, dia_semana: Dia) -> str:
        return medico.get_especialidad_para_dia(dia_semana)


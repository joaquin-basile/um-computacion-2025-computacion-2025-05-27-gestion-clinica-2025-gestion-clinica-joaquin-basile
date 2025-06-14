from datetime import datetime
from models.clinica import Clinica
from models.paciente import Paciente
from models.medico import Medico
from models.especialidad import Especialidad
from constants.dias import Dia
from exceptions.errors import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        print("\n--- Menú Clínica ---")
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agendar turno")
        print("4) Agregar especialidad")
        print("5) Emitir receta")
        print("6) Ver historia clínica")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            try:
                opcion = input("\nSeleccione una opción: ")
                
                if opcion == "0":
                    break
                elif opcion == "1":
                    self.agregar_paciente()
                elif opcion == "2":
                    self.agregar_medico()
                elif opcion == "3":
                    self.agendar_turno()
                elif opcion == "4":
                    self.agregar_especialidad_por_matricula()
                elif opcion == "5":
                    self.emitir_receta()
                elif opcion == "6":
                    self.ver_historia_clinica()
                elif opcion == "7":
                    self.ver_todos_los_turnos()
                elif opcion == "8":
                    self.ver_todos_los_pacientes()
                elif opcion == "9":
                    self.ver_todos_los_medicos()
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
                    
            except Exception as e:
                print(f"Error: {e}")

    def agregar_paciente(self):
        try:
            nombre = input("Ingrese el nombre del paciente: ")
            dni = input("Ingrese el DNI del paciente: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
            
            paciente = Paciente(nombre, dni, fecha_nacimiento)
            self.clinica.agregar_paciente(paciente)
            print("Paciente agregado exitosamente.")
            
        except Exception as e:
            print(f"Error al agregar paciente: {e}")

    def agregar_medico(self):
        try:
            nombre = input("Ingrese el nombre del médico: ")
            matricula = input("Ingrese la matrícula del médico: ")
            
            medico = Medico(nombre, matricula)
            
            # Agregar especialidades
            while True:
                agregar_esp = input("¿Desea agregar una especialidad? (s/n): ").lower()
                if agregar_esp != 's':
                    break
                self.agregar_especialidad(medico)
            
            self.clinica.agregar_medico(medico)
            print("Médico agregado exitosamente.")
            
        except Exception as e:
            print(f"Error al agregar médico: {e}")

    def agendar_turno(self):
        try:
            dni = input("Ingrese el DNI del paciente: ")
            matricula = input("Ingrese la matrícula del médico: ")
            especialidad = input("Ingrese la especialidad: ")
            
            fecha_str = input("Ingrese la fecha (DD/MM/AAAA): ")
            hora_str = input("Ingrese la hora (HH:MM): ")
            print("Fecha ingresada: ", fecha_str)
            
            # Parsear fecha y hora
            fecha_hora_str = f"{fecha_str} {hora_str}"
            fecha_hora = datetime.strptime(fecha_hora_str, "%d/%m/%Y %H:%M")
            
            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("Turno agendado exitosamente.")
            
        except (PacienteNoEncontradoException, MedicoNoEncontradoException, 
                MedicoNoDisponibleException, TurnoOcupadoException) as e:
            print(f"Error al agendar turno: {e}")
        except ValueError as e:
            print(f"Error en el formato de fecha/hora: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def agregar_especialidad(self, medico: Medico): 
        try:   
            tipo_esp = input("Ingrese el tipo de especialidad: ")
            print("Ingrese los días de atención (separados por coma):")
            print("Opciones: lunes, martes, miercoles, jueves, viernes, sabado, domingo")
            dias_str = input("Días: ")
            dias_input = [dia.strip().lower() for dia in dias_str.split(",")]
            
            dias_enum = []
            for dia_str in dias_input:
                try:
                    dia_enum = Dia[dia_str]
                    dias_enum.append(dia_enum)
                except KeyError:
                    print(f"Día inválido: {dia_str}. Será ignorado.")
            
            if dias_enum:
                especialidad = Especialidad(tipo_esp, dias_enum)
                medico.agregar_especialidad(especialidad)
                print("Especialidad agregada exitosamente.")
            else:
                print("No se pudo agregar la especialidad por falta de días válidos.")

        except (MedicoNoEncontradoException) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error al agregar especialidad: {e}")

    def agregar_especialidad_por_matricula(self):
            matricula = input("Ingrese la matrícula del médico: ")
            medico = self.clinica.get_medico_por_matricula(matricula)
            self.agregar_especialidad(medico)

    def emitir_receta(self):
        try:
            dni = input("Ingrese el DNI del paciente: ")
            matricula = input("Ingrese la matrícula del médico: ")
            
            print("Ingrese los medicamentos (presione Enter sin texto para terminar):")
            medicamentos = []
            while True:
                medicamento = input("Medicamento: ").strip()
                if not medicamento:
                    break
                medicamentos.append(medicamento)
            
            if not medicamentos:
                print("Debe ingresar al menos un medicamento.")
                return
                
            self.clinica.emitir_receta(dni, matricula, medicamentos)
            print("Receta emitida exitosamente.")
            
        except (PacienteNoEncontradoException, MedicoNoEncontradoException, 
                RecetaInvalidaException) as e:
            print(f"Error al emitir receta: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def ver_historia_clinica(self):
        try:
            dni = input("Ingrese el DNI del paciente: ")
            historia = self.clinica.get_historia_clinica_por_dni(dni)
            
            print("\n=== HISTORIA CLÍNICA ===")
            print(historia)
            
        except PacienteNoEncontradoException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error al obtener historia clínica: {e}")

    def ver_todos_los_turnos(self):
        try:
            turnos = self.clinica.get_turnos()
            
            if not turnos:
                print("No hay turnos agendados.")
                return
                
            print("\n=== TODOS LOS TURNOS ===")
            for i, turno in enumerate(turnos, 1):
                print(f"{i}. {str(turno)}")
                
        except Exception as e:
            print(f"Error al obtener turnos: {e}")

    def ver_todos_los_pacientes(self):
        try:
            pacientes = self.clinica.get_pacientes()
            
            if not pacientes:
                print("No hay pacientes registrados.")
                return
                
            print("\n=== TODOS LOS PACIENTES ===")
            for i, paciente in enumerate(pacientes, 1):
                print(f"{i}. {paciente}")
                
        except Exception as e:
            print(f"Error al obtener pacientes: {e}")

    def ver_todos_los_medicos(self):
        try:
            medicos = self.clinica.get_medicos()
            
            if not medicos:
                print("No hay médicos registrados.")
                return
                
            print("\n=== TODOS LOS MÉDICOS ===")
            for i, medico in enumerate(medicos, 1):
                print(f"{i}. {medico}")
                
        except Exception as e:
            print(f"Error al obtener médicos: {e}")


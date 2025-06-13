from models import paciente, medico, turno, receta, historia_clinica, especialidad
from constants.dias import Dia
from datetime import datetime

def main():
    paciente1 = paciente.Paciente("Juan", "54.123.312", "02/01/2005")
    medico1 = medico.Medico("Dr Gonzales", "10231", [especialidad.Especialidad("Cardiología", [Dia.lunes])])
    turno1 = turno.Turno(paciente1, medico1, datetime(2025, 10, 1, 10, 30), "Cardiología")
    receta1 = receta.Receta(paciente1, medico1, ["Ibuprofeno 400mg", "Paracetamol 500mg"], datetime(2023, 10, 1))
    historiaClinica1 = historia_clinica.HistoriaClinica(paciente1, [turno1], [receta1])

    print(str(medico1))
    print(str(turno1))
    print(str(receta1))
    print(str(historiaClinica1))

if __name__ == "__main__":
    main()

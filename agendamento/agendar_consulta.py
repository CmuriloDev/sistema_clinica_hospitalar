from models.consulta import Consulta
from cadastro.cadastro_medico import medicos 
from cadastro.cadastro_paciente import pacientes
from datetime import datetime

#Armazenar as consultas agendadas 
consultas = []

def agendar_consulta(cpf_paciente, crm_medico, data_hora):
    paciente_encontrado = None
    for paciente in pacientes:
        if paciente.cpf == cpf_paciente:
            paciente_encontrado = paciente
            break
    
    if not paciente_encontrado:
        return False, "Paciente não cadastrado."

    medico_encontrado = None
    for medico in medicos:
        if medico.crm == crm_medico:
            medico_encontrado = medico
            break

    if not medico_encontrado:
        return False, "Médico não cadastrado."
    
        
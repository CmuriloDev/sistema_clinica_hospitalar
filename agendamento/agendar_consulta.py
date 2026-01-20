from models.consulta import Consulta
from cadastro.cadastro_medico import medicos 
from cadastro.cadastro_paciente import pacientes
from datetime import datetime

consultas = []  

def agendar_consulta(cpf_paciente, crm_medico, data_hora):      
    for paciente in pacientes:
        if paciente.cpf == cpf_paciente:
            return paciente
    
        return False, "Paciente não cadastrado."
    
    medico_encontrado = None
    for medico in medicos:
        if medico.crm == crm_medico:
            medico_encontrado == medico
            return medico
           
        return False, "Médico não cadastrado."

    try:
        data_hora = datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
    except ValueError:
        return False, "Formato de data/hora inválido. Use DD/MM/AAAA HH:MM."
    
    if data_hora < datetime.now():
        return False, "Data/hora inválidos, tente novamente."

    for consulta in consultas:
        if consulta.medico.crm == medico_encontrado and consulta.data_hora == data_hora:
            return False, "Médico já possui consulta agendada nesse horário."
        
    nova_consulta = Consulta(paciente, medico, data_hora, status="AGENDADA")
    consultas.append(nova_consulta)
    return True, "Consulta agendada com sucesso."
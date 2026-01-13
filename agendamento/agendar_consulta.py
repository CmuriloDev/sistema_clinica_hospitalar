from models.consulta import Consulta
from cadastro.cadastro_medico import medicos 
from cadastro.cadastro_paciente import pacientes
from datetime import datetime

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

    try:
        data_hora = datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
    except ValueError:
        return False, "Formato de data/hora inválido. Use DD/MM/AAAA HH:MM."
    
    if data_hora < datetime.now():
        return False, "Data/hora inválidos, tente novamente."

    for consulta in consultas:
        if consulta.medico.crm and consulta.data_hora == data_hora:
            return False, "Médico já possui consulta agendada nesse horário."
        
    nova_consulta = Consulta(paciente_encontrado, medico_encontrado, data_hora, status="AGENDADA")
    consultas.append(nova_consulta)
    return True, "Consulta agendada com sucesso."
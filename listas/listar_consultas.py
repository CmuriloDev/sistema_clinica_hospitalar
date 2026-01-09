from agendamento.agendar_consulta import consultas

 
def listar_consultas():
    if not consultas:
        return False, "Nenhuma consulta agendada."
    
    consultas_listadas = []
    
    for consulta in consultas:
        consulta_dicionario = {
        "Paciente": consulta.paciente.nome,
        "Cpf Do Paciente": consulta.paciente.cpf,
        "Médico": consulta.medico.nome,
        "CRM": consulta.medico.crm,
        "Especialidade": consulta.medico.especialidade,
        "Data": consulta.data_hora,
        "Status": consulta.status
         }
        
    consultas_listadas.append(consulta_dicionario)
    return 
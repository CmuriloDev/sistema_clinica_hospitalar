from agendamento.agendar_consulta import consultas

 
def listar_consultas():
    if not consultas:
        return False, "Nenhuma consulta agendada."
    
    consultas_listadas = []
    
    for consulta in consultas:
        consulta_dict = {
        "nome do paciente": consulta.paciente.nome,
        "cpf do paciente": consulta.paciente.cpf,
        "telefone do paciente": consulta.paciente.telefone,
        "nome do medico": consulta.medico.nome,
        "crm": consulta.medico.crm,
        "especialidade": consulta.medico.especialidade,
        "data e hora": consulta.data_hora,
        "status": consulta.status
         }
        
        consultas_listadas.append(consulta_dict)
    return True, consultas_listadas
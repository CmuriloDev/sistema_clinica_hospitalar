from agendamento.agendar_consulta import consultas
#from cadastro.cadastro_medico import medicos -------> analisar a veracidade
#from cadastro.cadastro_paciente import pacientes -------> analisar a veracidade

 
def listar_consultas():
    if not consultas:
        return False, "Nenhuma consulta agendada."
    
    consultas_listadas = []
    
    for consulta in consultas:
        consulta_dict = {
        "paciente": consulta.paciente.nome,
        "cpf do paciente": consulta.paciente.cpf,
        "telefone do paciente": consulta.paciente.telefone,
        "medico": consulta.medico.nome,
        "crm": consulta.medico.crm,
        "especialidade": consulta.medico.especialidade,
        "data": consulta.data_hora,
        "status": consulta.status
         }
        
        consultas_listadas.append(consulta_dict)
    return True, consultas_listadas
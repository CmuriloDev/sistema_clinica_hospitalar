from agendamento.agendar_consulta import consultas

def listar_consultas():
    if not consultas:
        return False, "Nenhuma consulta agendada."
    
    return consultas 

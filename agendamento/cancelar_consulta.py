from agendamento.cancelar_consulta import consultas

def cancelar_consulta(cpf_paciente, data_hora):
    if not consultas:
        return False, "Não há consultas agendadas para cancelar."

    for consulta in consultas:
        if consulta.cpf_paciente == cpf_paciente and consulta.data_hora == data_hora:
            if consulta.status == "REALIZADA":
                return False, "Consulta já realizada."
            
            if consulta.status == "CANCELADA":
                return False, "Consulta já cancelada."
            
            consulta.status = "CANCELADA"
            return True, "Consulta cancelada com sucesso."
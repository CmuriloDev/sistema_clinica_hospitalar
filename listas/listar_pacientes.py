from cadastro.cadastro_paciente import pacientes

def listar_pacientes():
    if not pacientes:
        return False, "Nenhum paciente cadastrado."
    
    pacientes_listados = []

    for paciente in pacientes:
        paciente_dict = {
            "nome": paciente.nome,
            "cpf": paciente.cpf,
            "telefone": paciente.telefone,
            "email": paciente.email
        }

        pacientes_listados.append(paciente_dict)
    return True, pacientes_listados
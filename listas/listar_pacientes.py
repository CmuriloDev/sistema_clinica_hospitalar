from cadastro.cadastro_paciente import pacientes

def listar_pacientes():
    if not pacientes:
        return False, "Nenhum paciente cadastrado."
    
    return pacientes
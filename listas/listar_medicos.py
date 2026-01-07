from cadastro.cadastro_medico import medicos

def listar_medicos():
    if not medicos:
        return False, "Nenhum médico cadastrado."
    
    return medicos
from cadastro.cadastro_medico import medicos

def listar_medicos():
    if not medicos:
        return False, "Nenhum médico cadastrado."
    
    medicos_listados = []
    
    for medico in medicos:
        medico_dict = {
            "nome": medico.nome,
            "crm": medico.crm,
            "especialidade": medico.especialidade
        }

        medicos_listados.append(medico_dict)
    return True, medicos_listados

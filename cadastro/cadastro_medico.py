from models.medico import Medico 
import re

#Lista que armazena os Médicos 
medicos = []

#Função para cadastrar os Médicos 
def cadastrar_medico(nome, email, senha_hash, especialidade, crm,):
    for medico in medicos:
        if medico.crm == crm:
            return False, "CRM já cadastrado."
        
    medico_cadastrado = Medico(nome, email, senha_hash, especialidade, crm)
    medicos.append(medico_cadastrado)
    return True, "Médico cadastrado com sucesso"
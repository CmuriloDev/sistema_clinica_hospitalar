from models.medico import Medico 
import re

#Lista que armazena os Médicos 
medicos = []

#Função para cadastrar os Médicos 
def cadastrar_medico():
    print("\n--- Cadastro de Médico ---")
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
#Faz com que ao digitar o CRM, seja possível digitar só numeros
    while True:
        crm = input("CRM (apenas números): ")
        if crm.isdigit():
            break
        else:
            print("⚠️ Entrada inválida. Digite apenas números.")


    for medico in medicos:
        if medico.crm == crm:
            print("⚠️ CRM já cadastrado.")
            return
        
    novo_medico = Medico(nome, especialidade, crm)
    medicos.append(novo_medico)
    print("✅ Médico cadastrado com sucesso!")
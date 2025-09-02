from models.paciente import Paciente
import re

#Lista que armazena os pacientes  
pacientes = []

#Função para cadastrar os pacientes 
def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome: ")
    
    #Faz com que ao digitar o CRM, seja possível digitar só numeros
    while True:
        cpf = input("CPF (apenas números): ")
        if cpf.isdigit():
            break
        else:
            print("⚠️ Entrada inválida. Digite apenas números.")

    email = input("E-mail: ")

    for paciente in pacientes:
        if paciente.cpf == cpf:
            print("⚠️ CPF já cadastrado.")
            return 
        
    novo_paciente = Paciente(nome, cpf, email)
    pacientes.append(novo_paciente)
    print("✅ Paciente cadastrado com sucesso!")
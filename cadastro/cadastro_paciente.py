from models.paciente import Paciente
import re

#Lista que armazena os pacientes  
pacientes = []

#Função para cadastrar os pacientes 
def cadastrar_paciente(nome, cpf, email):
    for paciente in pacientes:
      if paciente.cpf == cpf:
         return False, "CPF já cadastrado."
      
    paciente_cadastrado = Paciente(nome, cpf, email)
    pacientes.append(paciente_cadastrado)
    return True, "Paciente cadastrado com sucesso"
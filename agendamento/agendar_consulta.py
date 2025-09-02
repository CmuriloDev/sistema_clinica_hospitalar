from models.consulta import Consulta
from cadastro.cadastro_medico import medicos 
from cadastro.cadastro_paciente import pacientes
from datetime import datetime

#Armazenar as consultas agendadas 
consultas = []

def agendar_consulta():
    print("\n--- Agendamento de consulta ---")
    #Verificar se há paciente cadastrado, se não tiver, interrompe o agendamento
    if not pacientes:
        print("⚠️ Nenhum paciente cadastrado.")
        return 
    
    if not medicos:
        print("⚠️ Nenhum médico cadastrado.")
        
    #Fazer uma lista enumerada e escolher um paciente enumerado
    print("\nPacientes disponíveis: ")
    for i, paciente in enumerate(pacientes):
        print(f"{i + 1}. {paciente}") 

    paciente_enumerado = int(input("Digite o número do paciente: ")) - 1

    #Verificar se o paciente existe na lista
    if paciente_enumerado < 0 or paciente_enumerado >= len(pacientes):
         print("❌ Paciente inválido.")
         return
    
    paciente_escolhido = pacientes[paciente_enumerado]  

    #Fazer uma lista enumerada e escolher um médico enumerado
    print("\nMédicos disponíveis: ")
    for i, medico in enumerate(medicos):
        print(f"{i + 1}. {medico}")

    medico_enumerado = int(input("Digite o número do médico: ")) - 1

    #Verificar se o médico existe na lista
    if medico_enumerado < 0 or medico_enumerado >= len(medicos):
        print("❌ Médico inválido.")
        return
    
    medico_escolhido = medicos[medico_enumerado]

    #Solicita data e hora da consulta com validação 
    try:
        data_str = input("Data da consulta (DD/MM/YYYY): ") 
        hora_str = input("Horário da consulta (HH:MM): ")
        data_hora = datetime.strptime(f"{data_str} {hora_str}", "%d/%m/%Y %H:%M")
        #não permite consultas no passado
        if data_hora < datetime.now():
            print("❌ Não é possível agendar uma consulta em data/hora passadas.")
            return

    except ValueError:
        print("❌ Data ou horário inválidos. Use o formato correto (DD/MM/YYYY HH:MM).")
        return
    
    # Verifica se o médico já tem uma consulta marcada nesse dia e hora
    for consulta in consultas:
        if consulta.medico.crm == medico_escolhido.crm and consulta.data_hora == data_hora:
            print("❌ O médico já tem uma consulta marcada nesse horário.")
            return

    #Adiciona uma nova consulta na lista
    nova_consulta = Consulta(paciente_escolhido, medico_escolhido, data_str, hora_str)
    consultas.append(nova_consulta)
    print("✅ Consulta agendada com sucesso!") 




from cadastro.cadastro_paciente import cadastrar_paciente
from cadastro.cadastro_medico import cadastrar_medico
from agendamento.agendar_consulta import agendar_consulta
from listas.listar_consultas import listar_consultas
from listas.listar_medicos import listar_medicos
from listas.listar_pacientes import listar_pacientes

#Função do menu
def mostrar_menu():
    print("\n=== Sistema de Agendamento de Consultas ===")
    print("1. Cadastrar paciente")
    print("2. Cadastrar médico")
    print("3. Agendar consulta")
    print("4. Listar médicos")
    print("5. Listar consultas")
    print("6. Listar pacientes")
    print("0. Sair")

#Função que controla o fluxo do sistema
def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo do sistema...")
            break

        elif opcao == "1":
            cadastrar_paciente()

        elif opcao == "2":
            cadastrar_medico()

        elif opcao == "3":
            agendar_consulta()

        elif opcao == "4":
            listar_medicos()

        elif opcao == "5":
            listar_consultas()

        elif opcao == "6":
            listar_pacientes
            
        else:
            print(f"Opção {opcao} ainda não implementada.")

if __name__ == "__main__":
    main()
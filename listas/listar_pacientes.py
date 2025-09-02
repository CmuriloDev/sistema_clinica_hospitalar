from cadastro.cadastro_paciente import pacientes

def listar_pacientes():
    print("\n--- Pacientes cadastrados ---")

    if not pacientes:
        print("⚠️ Nenhum paciente cadastrado.")
        return
    
    for i, paciente in enumerate(pacientes, start=1):
        print(f"{i}. {paciente}")
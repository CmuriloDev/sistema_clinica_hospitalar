from cadastro.cadastro_medico import medicos

def listar_medicos():
    print("\n--- Médicos cadastrados ---")

    if not medicos:
        print("⚠️ Nenhum médico cadastrado.")
        return
    
    for i, medico in enumerate(medicos, start=1):
        print(f"{i}. {medico}")
    
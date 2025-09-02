from agendamento.agendar_consulta import consultas

def listar_consultas():
    print("\n--- Consultas Agendadas ---")
    
    if not consultas:
        print("⚠️ Nenhuma consulta agendada.")
        return

    for i, consulta in enumerate(consultas, start=1):
        print(f"\nConsulta {i}:")
        print(f" Paciente: {consulta.paciente.nome}")
        print(f" Médico: {consulta.medico.nome} (CRM: {consulta.medico.crm})")
        print(f" Data: {consulta.data}")
        print(f" Hora: {consulta.hora}")
from firebase_admin import firestore

db = firestore.client()
 
def cancelar_consulta():
    id_consulta = input('Digite o ID da consulta que quer cancelar: ')
    
    try:
        #Busca a consulta no firebase
        consulta_ref = db.collection("consultas").document(id_consulta)
        consulta_doc = consulta_ref.get()

        if consulta_doc.exists:
            consulta_data = consulta_doc.to_dict()

        #verifica se o status permite cancelamento
            if consulta_data.get("status") == "Agendada":
                consulta_ref.update({"status": "Cancelada"})
                print(f"Consulta {id_consulta} cancelada com sucesso.✅")

            else:
                print(f"Não é possível cancelar, o status atual é '{consulta_data.get('status')}'.")
        
        else:
            print(f"Consulta não encontrada.❌")

    except Exception as e:
        print(f"Erro ao cancelar consulta: {e}❌")

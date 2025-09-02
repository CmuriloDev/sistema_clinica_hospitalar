#Classe do Médico
class Medico:
    def __init__(self, nome, especialidade, crm):
        self.nome = nome
        self.especialidade = especialidade
        self.crm = crm

#Imprime as informações 
    def __str__(self):
        return f"Dr(a). {self.nome} - {self.especialidade} - (CRM: {self.crm})"
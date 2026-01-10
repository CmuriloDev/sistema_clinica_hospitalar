#Classe da consulta 
class Consulta:
    def __init__(self, paciente, medico, data, hora, status):
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.hora = hora
        self.status = status

#Imprime as informações 
    def __str__(self):
        return (f"Consulta com {self.medico} para {self.paciente.nome}"
                f"na data {self.data} no horário de {self.hora} - Status: {self.status}")

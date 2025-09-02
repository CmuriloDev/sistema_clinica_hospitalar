# Classe do paciente
class Paciente:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    # Imprime as informações formatadas
    def __str__(self):
        cpf_formatado = f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        return f"{self.nome} (CPF: {cpf_formatado})"



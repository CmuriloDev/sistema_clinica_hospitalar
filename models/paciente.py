from models.usuario import Usuario

class Paciente(Usuario):
    def __init__(self, nome, cpf, senha_hash, email, telefone, ativo=True):
        super().__init__(nome, email, senha_hash, role="PACIENTE", ativo=ativo)
        self.cpf = cpf
        self.telefone = telefone


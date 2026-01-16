from models.usuario import Usuario

class Medico(Usuario):
    def __init__(self, nome, email, senha_hash, especialidade, crm, ativo=True):
        super.__init__(nome, email, senha_hash, role="MEDICO", ativo=ativo)
        self.crm = crm
        self.especialidade = especialidade

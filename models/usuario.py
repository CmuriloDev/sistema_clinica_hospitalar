class Usuario:
    def __init__(self, nome, email, senha_hash, role, ativo=True):
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash
        self.role = role
        self.ativo = ativo
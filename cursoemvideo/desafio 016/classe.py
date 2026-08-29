class Funcionario:

    empresa:str = "Curso em Vídeo" 
    # Para acessar use (nome_da_classe).(nome_do_atributo)

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> str:
        return f"Olá eu me chamo {self.nome}! Trabalho como {self.cargo} no setor de {self.setor} na empresa {Funcionario.empresa}"

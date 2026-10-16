from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):

    def __init__(self, nome:str, nascimento:int):
        self._nome = nome
        self._nascimento = None

        self.nascimento = nascimento


    @property
    def nascimento(self) -> int:
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano:int):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é inválido!")


    @property
    def idade(self) -> int:
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor:int):
        raise PermissionError("Você não pode alterar a idade. Mude a data de nascimento.")



class Aluno(Pessoa):

    cursosOficiais = ["ADM", "SI", "CONT", "CC", "ADS"]

    def __init__(self, nome:str, nascimento:int, curso:str):
        super().__init__(nome, nascimento)
        self._curso = None

        self.curso = curso


    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso:str):
        if curso in Aluno.cursosOficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais.")


    def add_curso(self, nomeCurso:str):
        nomeCurso = nomeCurso.strip().upper()

        if not nomeCurso in Aluno.cursosOficiais:

            if 2 <= len(nomeCurso) <= 5:
                Aluno.cursosOficiais.append(nomeCurso)

            else:
                raise ValueError(f"Nome {nomeCurso} está fora do padrão para cursos!")

        else:
            print(f"O curso {nomeCurso} já está na lista.")
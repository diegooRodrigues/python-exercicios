class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):

    def fazer_som(self):
        print("au-au")


class Gato(Animal):

    def fazer_som(self):
        print("miau")


c = Cachorro("dog")
g = Gato("gatinho")

animais = [c, g]

for animal in animais:
    animal.fazer_som()
    
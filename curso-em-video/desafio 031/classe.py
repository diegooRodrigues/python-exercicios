class Retangulo:

    def __init__(self, base=1, altura=1):
        self._base = None           # Atributo PROTEGIDO
        self._altura = None         # Atributo PROTEGIDO
        self._area = None           # Atributo PROTEGIDO

        self.base = base
        self.altura = altura
        

    # Método GETTER de base
    @property
    def base(self):
        return self._base
    
    #Método SETTER de base
    @base.setter
    def base(self, valor):
        if not isinstance(valor, int) and not isinstance(valor, float):
            raise TypeError("O valor da base deve ser um número inteiro ou float!")
        if valor < 0:
            raise ValueError("Valor INVÁLIDO! O valor deve ser positivo!")
        else:
            self._base = valor


    # Método GETTER de altura
    @property
    def altura(self):
        return self._altura
    
    #Método SETTER de altura
    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, int) and not isinstance(valor, float):
            raise TypeError("O valor da altura deve ser um número inteiro ou float!")
        if valor < 0:
            raise ValueError("Valor INVÁLIDO! O valor deve ser positivo!")
        else:
            self._altura = valor


    #Método GETTER de area
    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    # Método SETTER de area
    @area.setter
    def area(self, valor):
        raise PermissionError("Área NÃO pode ser definida!")


    # Método GETTER de medidas
    @property
    def medidas(self):
        return f"Base: {self._base} \nAltura: {self._altura} \nÁrea: {self.area}"
    
    #Método SETTER de medidas
    @medidas.setter
    def medidas(self, medidas:tuple):
        if not isinstance(medidas, tuple):
            raise TypeError("As medidas devem ser informadas dentro de uma tupla!")
        
        if len(medidas) != 2:
            raise SyntaxError("A tupla deve conter somente dois valores numéricos")
        
        if isinstance(medidas[0], int) or isinstance(medidas[0], float):
            self.base = medidas[0]
        else:
            raise TypeError("A base deve ser um número.")
        
        if isinstance(medidas[1], int) or isinstance(medidas[1], float):
            self.altura = medidas[1]
        else:
            raise TypeError("A altura deve ser um número.")
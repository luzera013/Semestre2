class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
#r1 = pessoa("laura", 25)
#print(r1.apresentar())

pessoa = [
    pessoa("luiz", 18),
    pessoa("pedro", 35),
    pessoa("lucas", 44)
    ]

print(pessoa)

for p in pessoa:
    print(p.apresentar())

####################################################

class pessoa:
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso
        self.altura + self.peso
    def apresentar(self):
        return f"Sua altura é {self.altura} e seu peso é {self.peso}, o seu imc é {self.peso / self.altura**2}"
    
p1 = pessoa(180, 65)
print(p1.apresentar())
    
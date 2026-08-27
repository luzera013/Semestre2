import pandas as pd

class notas:
    def __init__(self, nota1, nota2, nota3, nota4, frequencia, ):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.frequencia = frequencia
    def final(self):
        return round((self.nota1 + self.nota2 + self.nota3 + self.nota4) / 2)
    
    def resultado(self):
       return self.final() + self.frequencia
   
aluno1 = notas( 6, 7, 6, 8, 90)
aluno2 = notas(4, 4, 9, 10, 85)
aluno3 = notas(5, 6, 4, 8, 95)

dados = []

for i in notas:
    linha = {
        "nota1": i.nota1,
        "nota2": i.nota2,
        "nota3": i.nota3,
        "nota4": i.nota4,
        "frequencia": i.frequencia
        }
    dados.append(notas)

df = pd.DataFrame(dados)
print(df)


##############################################################################
#correção


import pandas as pd

class Notas: # Boa prática: nomes de classe começam com letra maiúscula
    def __init__(self, nota1, nota2, nota3, nota4, frequencia):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.frequencia = frequencia
        
    def final(self):
        # Nota: a soma de 4 notas dividida por 2 não dá a média (seria por 4). 
        # Mantive o cálculo original, mas ajustei o round.
        return round((self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4, 1)
    
    def resultado(self):
        # Adicionados os parênteses em self.final()
        return self.final() + self.frequencia
   
aluno1 = Notas(6, 7, 6, 8, 90)
aluno2 = Notas(4, 4, 9, 10, 85)
aluno3 = Notas(5, 6, 4, 8, 95)

# CORREÇÃO 1: Criar uma lista com as instâncias dos alunos
lista_alunos = [aluno1, aluno2, aluno3]

dados = []

# CORREÇÃO 1: Iterar sobre a lista de alunos, não sobre a classe
for i in lista_alunos:
    linha = {
        "nota1": i.nota1,
        "nota2": i.nota2,
        "nota3": i.nota3,
        "nota4": i.nota4,
        "frequencia": i.frequencia,
        "Média Final": i.final(),      # Aproveitando seu método
        "Resultado": i.resultado()     # Aproveitando seu método
    }
    dados.append(linha) # CORREÇÃO 3: Salvando a 'linha' criada, não a classe 'notas'

df = pd.DataFrame(dados)
print(df)
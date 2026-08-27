import pandas as pd

class investimento:
    def __init__(self, nome, capital, taxa, tempo):
        self.nome = nome
        self.capital = capital
        self.taxa = taxa
        self.tempo = tempo
        
    def monitoramento(self):
        return round(self.capital * (1 + self.taxa / 100) ** self.tempo, 2)
    
    def lucro(self):
        return round(self.monitoramento() - self.capital, 2)
    
inv1 = investimento("CDB banco X", 10000, 1.2, 12)
inv2 = investimento("Tesouro", 15000, 1.0, 18)
inv3 = investimento("Fundo Y", 8000, 1.5, 10)

dados = []

for i in investimento:
    linha = {
        "investimento": i.nome,
        "Capital": i.capital,
        "Taxa": i.taxa,
        "tempo": i.tempo,
        "Montate": i.montante(),
        "Lucro": i.lucro()
    }
    dados.append(linha)
    
df = pd.DataFrame(dados)
print(df)

###########################################################

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
        print(f"Nota final {self.final}, com a frenquecia em {self.frequencia}")

######################################################################################



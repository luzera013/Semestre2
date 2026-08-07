dados = [[], [], [], [], []]
contador = 0

while contador < 4:
    marca = input("Digite a marca do carro: ")
    versao = input("Digite a versão do carro: ")
    modelo = input("Digite o modelo do carro: ")
    ano = int(input("Digite o ano do carro: "))
    cor = input("Digite a cor do carro: ")

    dados[0].append(marca)
    dados[1].append(versao)
    dados[2].append(modelo)
    dados[3].append(ano)
    dados[4].append(cor)
    contador += 1

print(dados)
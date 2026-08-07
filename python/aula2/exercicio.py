dadoascarro = [[],[],[],[]]
contador = 0

while contador < 2:
    print(f"Dados do {contador + 1}º carro:")
    marca = input("Digite a marca do carro: ")
    dadoascarro[0].append(marca)
    modelo = input("Digite o modelo do carro: ")
    dadoascarro[1].append(modelo)
    ano = int(input("Digite o ano do carro: "))
    dadoascarro[2].append(ano)
    cor = input("Digite a cor do carro: ")
    dadoascarro[3].append(cor)
    contador += 1

    print(dadoascarro)
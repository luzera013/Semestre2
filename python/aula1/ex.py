lista_dados = []

for i in range(3):
    print(f"Listas {i + 1}")
    nomes = input("Digite seu nome: ")
    lista_dados.append(nomes)
    idade = int(input(f"Digite sua idade {nomes}: "))
    lista_dados.append(idade)

    print(lista_dados)

##@

lista_completa = []

for k in range(2):
    nomes = input("Digite seu nome: ")
    idade = int(input(f"Digite sua idade {nomes}: "))
    sexo = input("Digite seu sexo: (M/F): ")
    lista = [nome, idade, sexo]
    lista_completa.append()
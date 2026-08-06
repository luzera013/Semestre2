lista_nome = []
lista_idades = []
lista_sexo = []

for i in range(2):
    print(f"\nDados da {i + 1} pessoa:")
    nome = input("Digite seu nome:")
    lista_nome.append(nome)
    idade = int(input("Digite sua idade:"))
    lista_idades.append(idade)
    sexo = input("Digite M para masculino e F para feminino")
    lista_sexo.append(sexo)

print(lista_nome)
print(lista_idades)
print(lista_sexo)

#teste
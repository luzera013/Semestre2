#(resumo aula1)

dados = [[], [], []]
contador = 0

while contador < 2:
    print(f"\nDados do {contador + 1}º aluno:")
    nome = input("Digite o nome do aluno: ")
    dados[0].append(nome)
    idade = int(input("Digite a idade do aluno: "))
    dados[1].append(idade)
    sexo = input("Digite o sexo do aluno (M/F): ")
    dados[2].append(sexo)
    contador += 1

    print("\nDados coletados:")
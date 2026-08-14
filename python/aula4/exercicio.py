listaNotas = []

nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
if (nota + nota2 + nota3) / 3 >= 6:
    print(f"{nome} foi aprovado com as notas {nota}, {nota2} e {nota3}")
    print(listaNotas)
else:
    print(f"{nome} foi reprovado com as notas {nota}, {nota2} e {nota3}")

    listaNotas.append((nome, nota, nota2, nota3))


#não deu muito certo 

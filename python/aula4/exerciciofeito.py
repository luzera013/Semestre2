def exercicio_01():
    alunos = {}
    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["nota1"] = float(input("Digite a primeira nota: "))
    aluno["nota2"] = float(input("Digite a segunda nota: "))
    aluno["nota3"] = float(input("Digite a terceira nota: "))

    media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3
    if media >= 6:
        print(f"{aluno['nome']} foi aprovado com média {media}")
    else:
        print(f"{aluno['nome']} foi reprovado com média {media}")
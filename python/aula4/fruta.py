#FOR fruta in estoque:
#    original = fruta

for fruta in estoque:
    print(f"{fruta}: {qtd} unidades")

#######################################################

alunos = {
    "ana": {"n1": 8, "n2": 9, "n3": 10},
    "bruno": {"n1": 7, "n2": 8, "n3": 9}
}

for nome, notas in alunos.items():
    for prova, valor in notas.items():
        print(nome, prova, valor)

alunos = {
    "ana": {"n1": 8, "n2": 9, "n3": 10},
    "bruno": {"n1": 7, "n2": 8, "n3": 9}
}

for nome, notas in alunos.items():
    media = sum(notas.values()) / len(notas)
    print(f"{nome}: {media:.2f}")
carrinho = {}
produto = ""

while produto != "sair":
    produto = input("Produto:")
    if produto != "sair":
        break
    preco = float(input("Preço:"))
    carrinho[produto] = preco

print(carrinho)

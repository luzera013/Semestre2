cliente = {"nome": "ana", "idade": 30}
cliente = ["idade"] = 31
cliente.update({"tel": "119999999"})
del cliente["nome"]
tel = cliente.pop("tel")
print(cliente, tel)
#O metodo Pop() evita o erro KeyError ao mesmo tempo que recupera o dado excluido
#Use Del para deletar uma chave, ou Pop() para remover 
####################################
produto = {"preco": 800, "estoque": 3}
if produto['preco'] > 1000:
    categoria = 'preco alto'
else:
  categoria = 'preco baixo'
  
print(categoria)

#################################

cliente = {"nome": "ana", "idade": 30, "cidade": "sp"}
print(cliente.keys())
print(cliente.values())
print(cliente.items())


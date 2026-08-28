lista = []
tupla = ["a", "b", "c"]

for i in range(3):
    nome = input("Innome: ")
    lista.append(nome)
    
print(tupla)

####################################

tupla = ('a', 'b', 'c')

for k in tupla:
    print(k)
  
print(tupla[1])  
print(tupla[2])
print(tupla[0])

###################

lista_nova = list(tupla)
print(lista_nova)

#########################################

i = 0

while i <= 99:
    print(i)
    i += 1
    
    ########################################
    
i = 0

while i <= 3:
    if i == 2:
        break
    print(i)
    i += 1    
    
###################################################################

for i in range(1, 6):
    if i == 3:
        print(i)
        continue    #Só conta o 3
#####################################################################


soma = 0
for numero in range(10):
    soma += numero
    print("A soma dos números de 1, a 3 é: ", soma)

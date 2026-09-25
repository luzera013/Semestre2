p1 = int(input("Me diz de 0 a 10 e quão triste você está: "))
p2 = int(input("Me diz de 0 a 10 e quão triste você está esta semana: "))
p3 = int(input("Me diz de 0 a 10 o quão louco você está: "))
p4 = int(input("Me diz o quanto você quer ela de volta, junto com sua felicidade: "))

if p1 + p2 + p3 + p4 >= 30:
    print("Já esperava")
elif p1 + p2 + p3 + p4 >= 20:
    print("triste")
else:
    print("Tudo bem, morra feliz, mas morra")
    
########################################################################################

def calcular_tristeza(p1, p2, p3, p4):
    total = p1 + p2 + p3 + p4
    porcentagem = (total / 40) * 100
    return porcentagem


p1 = int(input("De 0 a 10, quão triste você está? "))
p2 = int(input("De 0 a 10, quão triste você esteve esta semana? "))
p3 = int(input("De 0 a 10, o quão louco você está? "))
p4 = int(input("De 0 a 10, o quanto você quer ela de volta junto com sua felicidade? "))

resultado = calcular_tristeza(p1, p2, p3, p4)

print(f"Seu nível de tristeza é {resultado:.1f}%")

if resultado >= 75:
    print("Já esperava.")
elif resultado >= 50:
    print("Triste.")
else:
    print("Tudo bem, morra feliz, mas morra")

#######################################################################################

While True:
    p1 = int(input("De 0 a 10, quão triste você está? "))
    p2 = int(input("De 0 a 10, quão triste você esteve esta semana? "))
    p3 = int(input("De 0 a 10, o quão louco você está? "))
    p4 = int(input("De 0 a 10, o quanto você quer ela de volta junto com sua felicidade? "))

    resultado = calcular_tristeza(p1, p2, p3, p4)

    print(f"Seu nível de tristeza é {resultado:.1f}%")

    if resultado >= 75:
        print("Já esperava.")
    elif resultado >= 50:
        print("Triste.")
    else:
        print("Tudo bem, morra feliz, mas morra")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break
    
########################################################################################

for i in range(5):
    p1 = int(input("De 0 a 10, quão triste você está? "))
    p2 = int(input("De 0 a 10, quão triste você esteve esta semana? "))
    p3 = int(input("De 0 a 10, o quão louco você está? "))
    p4 = int(input("De 0 a 10, o quanto você quer ela de volta junto com sua felicidade? "))

    resultado = calcular_tristeza(p1, p2, p3, p4)

    print(f"Seu nível de tristeza é {resultado:.1f}%")

    if resultado >= 75:
        print("Já esperava.")
    elif resultado >= 50:
        print("Triste.")
    else:
        print("Tudo bem, morra feliz, mas morra")
        
#########################################################################################

match resultado:
    case resultado if resultado >= 75:
        print("Já esperava.") 
    case resultado if resultado >= 50:
        print("Triste.")
    case _:
        print("Tudo bem, morra feliz, mas morra")
        
##########################################################################################

resultado = 67.5

if resultado >= 75:
    faixa = 3
elif resultado >= 50:
    faixa = 2
else:
    faixa = 1

match faixa:
    case 3:
        print("Já esperava.")
    case 2:
        print("Triste.")
    case 1:
        print("Tudo bem, siga em frente.")
        
        
######################################################################################################

#terceira lista
l1 = []
l2 = []

while True:
    e1 = int(input("Digite um valor para a primeira lista (0 para sair): "))
    if e1 == 0:
        break
    l1.append(e1)
while True:
    e2 = int(input("Digite um valor para a segunda lista (0 para sair): "))
    if e2 == 0:
        break
    l2.append(e2)

l3 = l1[:]
l3.extend(l2)

print("\nTerceira lista:", l3)
    

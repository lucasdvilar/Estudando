#6.3
l1 = []
l2 = []

while True:
    n1 = int(input("Digite um número para a lista 1 (digite 0 para ir à lista 2: "))
    if n1 == 0:
        break
    l1.append(n1)

while True:
    n2 = int(input("Digite um número para a lista 2 (digite 0 para sair): "))
    if n2 == 0:
        break
    l2.append(n2)

l3 = []
juncao = l1[:]
juncao.extend(l2)

#voltar aqui

print(f"Primeira lista: {l1}")
print(f"Segunda lista: {l2}")
print(f"Junção: {l3}")
        

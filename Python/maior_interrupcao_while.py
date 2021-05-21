maior = 0
while True:
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
    v = input("Deseja continuar (S/N)? ")
    if v == 'S' or v == 's':
        continue
    elif v == 'N' or v == 'n':
        break
    else:
        print("Caractere inválido!")

print("O maior número foi %d." %maior)

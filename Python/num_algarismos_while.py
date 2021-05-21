num = int(input("Digite um número: "))

cont = 0
if num == 0:
    cont = 1
else:
    while num != 0:
        cont += 1
        num = num // 10

print("O número de algarismos é %d." %cont)


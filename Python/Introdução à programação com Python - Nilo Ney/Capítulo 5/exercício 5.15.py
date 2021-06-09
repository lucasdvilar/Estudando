#exercício 5.15
preco = 0
total = 0

while True:
    cod = int(input("Digite o código do produto: "))
    if cod == 0:
        break
    elif cod == 1:
        preco = 0.5
    elif cod == 2:
        preco = 1
    elif cod == 3:
        preco = 4
    elif cod == 5:
        preco = 7
    elif cod == 9:
        preco = 8
    else:
        print("Código inválido!")
    if preco != 0:
        qtd = int(input("Quantidade comprada: "))
        total = total + (preco * qtd)

print("Total a pagar: R$%.2f." %total)

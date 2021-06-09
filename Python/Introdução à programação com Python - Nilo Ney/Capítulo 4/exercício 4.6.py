#exercício 4.6
distancia = float(input("Digite a distância em km: "))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print("O preço é R$%.2f." %preco)

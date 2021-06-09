#exercício 3.14
qtd_km = float(input("Digite a quantidade de km percorridos: "))
qtd_dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))

preco_dia = qtd_dias * 60
preco_km = qtd_km * 0.15
preco_total = preco_dia + preco_km

print("O preço a pagar é R$%.2f." %preco_total)

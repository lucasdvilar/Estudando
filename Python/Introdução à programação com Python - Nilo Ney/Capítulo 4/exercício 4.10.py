#exercício 4.10
qtd_kwh = int(input("Quantidade kWh consumida: "))
instalacao = input("Tipo de instalação (R, C ou I): ")

if instalacao == 'R':
    if qtd_kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif instalacao == 'C':
    if qtd_kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.6
elif instalacao == 'I':
    if qtd_kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6

if instalacao == 'R' or instalacao == 'C' or instalacao == 'I':
    custo = qtd_kwh * preco
    print("O valor a pagar é R$%.2f." %custo)
else:
    print("Tipo de instalação inválido!")

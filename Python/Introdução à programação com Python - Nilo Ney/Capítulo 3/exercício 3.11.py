#exercício 3.11
valor = float(input("Digite o valor da mercadoria: "))
perc_desconto = float(input("Digite o percentual de desconto: "))

desconto = valor * perc_desconto / 100
a_pagar = valor - desconto

print("A mercadoria teve R$%.2f de desconto." %desconto)
print("O preço a pagar é R$%.2f." %a_pagar)

#exercício 4.9
valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite a quantidade de anos a pagar: "))

meses = anos * 12
prestacao = valor / meses

if prestacao <= salario * 0.3:
    print("A prestação será de R$%.2f." %prestacao)
else:
    print("O valor da prestação é superior a 30% do salário.")

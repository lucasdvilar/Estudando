#exercício 4.4
salario = float(input("Digite seu salário: "))

aumento = salario * 0.15
if salario > 1250:
    aumento = salario * 0.1
    
print("O aumento será de R$%.2f." %aumento)

#só a porc. na condição; dois ifs

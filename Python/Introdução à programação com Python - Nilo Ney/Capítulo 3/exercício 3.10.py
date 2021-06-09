#exercício 3.10
salario = float(input("Digite seu salário: "))
porcentagem = float(input("Digite a porcentagem do aumento: "))

aumento = salario * porcentagem / 100
novo_salario = salario + aumento

print("O aumento foi de R$%.1f." %aumento)
print("O novo salário é R$%.2f." %novo_salario)
                            

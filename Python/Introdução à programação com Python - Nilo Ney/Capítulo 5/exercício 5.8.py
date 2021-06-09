#exercício 5.8
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

cont = 1
soma = 0
while cont <= n2:
    soma = soma + n1
    cont = cont + 1
print("%d x %d = %d" %(n1, n2, soma))
    
    

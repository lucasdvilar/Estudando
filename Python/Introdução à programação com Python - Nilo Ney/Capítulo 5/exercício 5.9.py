#exercício 5.9
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

q = 0
x = n1
while x >= n2:
    x = x - n2
    q = q + 1
resto = x
    
print("%d / %d = %d. Resto = %d" %(n1, n2, q, resto))

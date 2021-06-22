#5.26
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

atual = n1
while atual >= n2:
    atual = atual - n2

print(f"O resto de {n1} dividido por {n2} é {atual}.")
#para verificar:
print(n1 % n2)

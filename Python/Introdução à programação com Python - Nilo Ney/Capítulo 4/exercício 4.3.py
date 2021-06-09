#exercício 4.3
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

maior = 0
if a > b and a > c:
    maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = 0
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print("O maior número é %d." %maior)
print("O menor número é %d." %menor)


#exercício 5.14
soma = 0
qtd_num = 0

while True:
    x = int(input("Digite um número inteiro: "))
    if x == 0:
        break
    qtd_num += 1
    soma = soma + x
media = soma / qtd_num

print("A quantidade de números digitados é %d.\nA soma é %d.\nA média é %.2f." %(qtd_num, soma, media))

#exercício 5.7
n = int(input("Tabuada de: "))
inicio = int(input("Início da tabuada: "))
fim = int(input("Fim da tabuada: "))

while inicio <= fim:
    print("%d x %d = %d" %(n, inicio, inicio * n))
    inicio += 1

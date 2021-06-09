#exercício 4.2
velocidade = float(input("Digite sua velocidade em km/h: "))

valor = (velocidade - 80) * 5

if velocidade > 80:
    print("Você foi multado!")
    print("O valor da multa foi R$%.2f." %valor)
    

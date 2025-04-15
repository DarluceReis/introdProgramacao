numeroInicial = int(input("Digite o primeiro número inteiro: "))
numeroFinal = int(input("Digite o segundo número inteiro, para mostrar o range: "))

#é uma boa prática que o contador tenha uma variável própria
numero = numeroInicial

while numero <= numeroFinal:
    print(numero) 
    numero += 1

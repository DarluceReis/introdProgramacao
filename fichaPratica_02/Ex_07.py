#pedir o numero ao usuario
numero = int(input("Digite um número: "))
contador = 0
numeroMenor = numero - 5

#subtrair 5 e mostrar 1 a 1 e somar 5 e mostrar 1 a 1
while contador <= 10:
    if numeroMenor != numero:
        print(numeroMenor)
    numeroMenor += 1
    contador += 1

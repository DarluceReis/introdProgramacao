#solicitar o número que limita o fim do laço e o número que define o salto
limite = float(input("Informe o número limite: "))
salto = float(input("Informe o número que define o salto: "))
incremento = 0

#quero fazer salto + salto + salto ... até o limite
while salto <= limite:
    if incremento <= limite:
        print(incremento)
        incremento += salto



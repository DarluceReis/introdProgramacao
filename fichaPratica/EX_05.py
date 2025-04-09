numero1 = float(input("Vamos calcular a média aritmética e ponderada usando os pesos de 20, 30 e 50 por cento! Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

mediaA= (numero1 + numero2 + numero3) / 3
mediaP= ((numero1 * 0.20) + (numero2 * 0.30) + (numero3 * 0.50))
        

print("A média aritmética é: ", mediaA)
print("A média ponderada é: ", mediaP)
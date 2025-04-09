num1 = float(input("Digite o primeiro número real: "))
num2 = float(input("Digite o segundo número real: "))
operador = str(input("Qual operação aritmética deseja utilizar? (+, -, * ou /)"))

if operador == "+":
    resultado = num1 + num2

elif operador == "-":
    resultado = num1 - num2

elif operador == "*":
    resultado = num1 * num2

elif operador == "/":
    resultado = num1 / num2

else:
    print("Operador inválido. Tente digitar +, -, / ou *")

print(f"O resultado da operação  {num1} {operador} {num2} é: {resultado}")
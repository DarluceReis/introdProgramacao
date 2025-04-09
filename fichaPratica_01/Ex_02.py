salario = float(input("Vamos descobrir quanto imposto você vai pagar. Para isto, digite o seu salário: "))

if salario <= 15000:
    imposto = salario * 0.20

else:
    imposto = salario * 0.30

print(f"O valor do imposto é: {imposto}")    
salario = float(input("Digite o salário: "))

if salario <= 15000:
    imposto = salario * 0.20

elif salario <= 20000:
 imposto = salario * 0.30

elif salario <= 25000:
   imposto = salario * 0.35

else:
   imposto = salario * 0.40


print(f"O imposto sobre o seu salário é: {imposto}€")
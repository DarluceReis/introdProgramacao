numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 < numero2 and numero1 < numero3:
    menor = numero1

elif numero2 < numero1 and numero1 < numero3:
    menor = numero2

else:
    menor = numero3

print(f"O número menor é {menor}")
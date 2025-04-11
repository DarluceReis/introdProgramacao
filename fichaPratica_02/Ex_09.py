numero = int(input("Digite um número maior que 2 e diremos se ele é par: "))
pares = 0

if numero <= 2:
    print("Informe um número MAIOR que 2")

else:

    while pares != numero and numero > 2:
        if pares % 2 == 0:
            print (pares)
        pares += 1

print(f"O número digitado foi: {numero}")


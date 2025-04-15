numero = int(input("Informe um número: "))
pares = 0

if numero <= 2:
    print("Informe um número MAIOR que 2")

else:

    while pares != numero and numero > 2:
        if pares % 2 == 0 and pares != 0:
            print (pares)
        pares += 1

if numero % 2 == 0:
    print(f"O número digitado foi: {numero} e é par!")

else:
    print(f"O número digitado foi: {numero} e é impar")


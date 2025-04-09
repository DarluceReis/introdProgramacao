numero1 = int(input("Vamos descobrir qual número é maior e qual é menor! Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número:"))

if numero1 > numero2:
    maior = numero1
    menor = numero2
    print(f"O maior número é = {maior} e o menor número é = {menor}")

elif numero1 == numero2:
    print("Os números são iguais. Digite números diferentes.")

else:
    maior = numero2
    menor = numero1

    print(f"O maior número é = {maior} e o menor número é = {menor}")
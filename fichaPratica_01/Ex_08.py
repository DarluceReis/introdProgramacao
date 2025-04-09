nota1 = float(input("Vamos conferir se você foi aprovado. Digite as suas 3 notas consecutivamente de 0 a 20. Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))
nota3 = float(input("Digite a Nota 3: "))

mediaP = (nota1 * 0.25) + (nota2 * 0.35) + (nota3 * 0.40)

if mediaP >= 9.5:
    print(f"Parabéns! Você foi aprovado com a média {mediaP}")

else:
    print(f"Não foi dessa vez! Você foi reprovado com a média {mediaP}")
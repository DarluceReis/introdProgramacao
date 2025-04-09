numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 < numero2 and numero1 < numero3:
    primeiro = numero1
    if numero2 < numero3:
        segundo = numero2
        terceiro = numero3
    
elif numero2 < numero1 and numero2 < numero3:
    primeiro = numero2
    if numero1 < numero3:
        segundo = numero1
        terceiro = numero3
        
elif numero3 < numero1 and numero3 < numero2:
    primeiro = numero3
    if numero2 < numero1:
        segundo = numero2
        terceiro = numero1
        
else:
    print("Digitos inválidos")

print(f"A ordem correta é: 1º: {primeiro}, 2º: {segundo}, 3º: {terceiro}")
    
    

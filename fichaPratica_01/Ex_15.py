numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
ordem = str(input("Qual ordem deseja visualizar os números digitados? crescente / descrescente: "))

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
        
if ordem == "crescente":
    print(f"A ordem crescente é: 1º lugar: {primeiro}, 2º lugar: {segundo}, 3º lugar: {terceiro}")

elif ordem == "decrescente":
   print(f"A ordem decrescente é: 1º lugar: {terceiro}, 2º lugar: {segundo}, 3º lugar: {primeiro}") 
   
else:
    print("Dígitos inválidos")
    
    

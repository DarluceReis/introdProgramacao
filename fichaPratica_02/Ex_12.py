# Ler dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
 
# Descobrir o menor e o maior (para funcionar em qualquer ordem)
inicio = min(num1, num2)
fim = max(num1, num2)
 
print(f"Múltiplos de 5 entre {inicio} e {fim}:")
 
# Usar while para percorrer do menor até o maior
while inicio <= fim:
    if inicio % 5 == 0:
        print(inicio)
    inicio += 1
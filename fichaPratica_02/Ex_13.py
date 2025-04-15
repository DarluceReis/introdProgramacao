vezes = int(input("Quantos números deseja inserir? "))
contador = 1
anterior = int(input("Digite o 1º número: "))
crescente = True
 
while contador < vezes:
    atual = int(input(f"Digite o {contador + 1}º número: "))
   
    if atual < anterior:
        crescente = False
   
    anterior = atual
    contador += 1
 
if crescente:
    print("Os números estão em ordem crescente.")
else:
    print("Os números NÃO estão em ordem crescente.")
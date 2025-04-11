#inicio 2 variaveis. Uma pra soma dos números inseridos e uma pro contador. soma / contador = media
numero = int(input("Digite os números e descubra a média deles. Para parar o programa, digite -1. "))
soma = 0
contador = 0

while numero != -1:
    soma += numero
    contador += 1
    numero = int(input("Digite o próximo número e descubra a média dele somado ao(s) anterior(es). Para parar o programa, digite -1. "))

#se o contador for menor que zero, ou seja, se já tiver iniciado, fazer a conta da média
if contador > 0:
    media = soma / contador
    print(f"Média dos números inseridos: {media}")
else:
    print("Nenhum número foi inserido.")
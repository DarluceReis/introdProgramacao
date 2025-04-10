numero = int(input("Digite um número: "))
#pra fazer a primeira continha
temporario = -5

#basicamente, enquanto -5 for maior que -5 (ou seja, sempre) e -5 for menor que 5 ou seja somar mais 1 até dar 5
while temporario >= -5 and temporario <= 5:
# não aparecer o número que foi inserido pelo usuário
    if temporario != 0:
#printar o numero mais -5 -4 -3 -2...
        print(numero + temporario)
#incrementar 1 a cada vez que rodar o laço
    temporario += 1

posicaoFinal = int(input("Digite a sua posição final: "))

if posicaoFinal == 1:
    pontos = 10

elif posicaoFinal == 2:
    pontos = 8

elif posicaoFinal == 3:
    pontos = 6

elif posicaoFinal == 4:
    pontos = 5

elif posicaoFinal == 5:
    pontos = 4

elif posicaoFinal == 6:
    pontos = 3

elif posicaoFinal == 7:
    pontos = 2

elif posicaoFinal == 8:
    pontos = 1

else:
    pontos = 0

print(f"Você ficou na posição {posicaoFinal} e ganhou {pontos} pontos!")
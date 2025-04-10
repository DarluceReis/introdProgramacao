valor = int(input("Insira um valor multiplo de 5: "))
#confirmacao que o numero é multiplo de 5, se nao for já de descartado. se o resto do numero for diferente de 0, já era.
if valor % 5 != 0:
    print("O valor inserido não é multiplo de 5, insira novamente!")
# // divide e mostra o valor inteiro
# % para mostrar quanto de cada nota cabe dentro do valor
else:
    nota200 = valor // 200
    valor = valor % 200
 
    nota100 = valor // 100
    valor = valor % 100
 
    nota50 = valor // 50
    valor = valor % 50
 
    nota20 = valor // 20
    valor = valor % 20
 
    nota10 = valor // 10
    valor = valor % 10
 
    nota5 = valor // 5
    valor = valor % 5
 
    print("Notas:")
    if nota200 > 0:
        print(nota200, "nota(s) de 200 euros")
    if nota100 > 0:
        print(nota100, "nota(s) de 100 euros")
    if nota50 > 0:
        print(nota50, "nota(s) de 50 euros")
    if nota20 > 0:
        print(nota20, "nota(s) de 20 euros")
    if nota10 > 0:
        print(nota10, "nota(s) de 10 euros")
    if nota5 > 0:
        print(nota5, "nota(s) de 5 euros")
 
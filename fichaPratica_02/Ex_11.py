# ranges
contador_0_25 = 0
contador_26_50 = 0
contador_51_75 = 0
contador_76_100 = 0


while True:
    numIntervalo = int(input("Insira um número positivo e inteiro: "))
    if numIntervalo < 0:
        break
    if 0 <= numIntervalo <= 25:
        contador_0_25 += 1
    elif 26 <= numIntervalo <= 50:
        contador_26_50 +=1
    elif 51 <= numIntervalo <= 75:
        contador_51_75 +=1
    elif 76 <= numIntervalo <= 100:
        contador_76_100 +=1

print("[0, 25]", contador_0_25)
print("[26, 50]", contador_26_50)
print("[51, 75]", contador_51_75)
print("[76, 100]", contador_76_100)
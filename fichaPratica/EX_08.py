# iniciando a variável
total_segundos = 0

# repetir o laço 5 vezes, 1 pra cada msc
for i in range(5):
    print(f"Música {i + 1}:")
    
# Pegando os minutos e segundos da música
    min = int(input(" Digite os minutos: "))
    seg = int(input("  Digite os segundos: "))

# Transformamos tudo em segundos e somamos ao total
    total_segundos += min * 60 + seg

# converter os segundos totais para horas, minutos e segundos
horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

# Mostramos o resultado formatado bonitinho
print(f"\nDuração total do álbum: {horas:02d}:{minutos:02d}:{segundos:02d}")

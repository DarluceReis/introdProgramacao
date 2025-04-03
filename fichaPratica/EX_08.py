faixa1_min, faixa1_seg = 5, 45
faixa2_min, faixa2_seg = 3, 49
faixa3_min, faixa3_seg = 2, 59
faixa4_min, faixa4_seg = 3, 50
faixa5_min, faixa5_seg = 2, 40

total_minutos = faixa1_min + faixa2_min + faixa3_min + faixa4_min + faixa5_min
total_segundos = faixa1_seg + faixa2_seg + faixa3_seg + faixa4_seg + faixa5_seg

total_minutos += total_segundos // 60 
total_segundos = total_segundos % 60 

horas = total_minutos // 60
minutos = total_minutos % 60

print(f"Duração total: {horas}h {minutos}m {total_segundos}s")

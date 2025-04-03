produto1 = float(input("Vamos sobrar 3 produtos e mostrar o resultado com 10 por cento de desconto! Informe o valor do produto 1: "))
produto2 = float(input("Informe o valor do produto 2: "))
produto3 = float(input("Informe o valo do produto 3: "))

desconto = (produto1 + produto2 + produto3) * 0.10
total = (produto1 + produto2 + produto3) - desconto

print("O valor da soma dos 3 produtos com 10 por cento de desconto é: ", total)
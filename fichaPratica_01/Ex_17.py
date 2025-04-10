saldoMed = float(input("Para analisarmos o seu crédito, por favor nos informe o seu saldo medio: "))
 
if saldoMed <= 1999:
    print ("De acordo com o seu saldo medio, não nos é possivel atribuir nenhum credito")
 
elif saldoMed <= 3999:
    saldoMed = saldoMed * 0.20
    print ("O credito disponivel é de:",  saldoMed, "€")
 
elif saldoMed <= 5999:
    saldoMed = saldoMed * 0.30
    print ("O credito disponivel é de: ", saldoMed, "€")
 
else:
    saldoMed >= 6000
    saldoMed = saldoMed * 0.40
    print ("O credito disponivel é de: ", saldoMed, "€")
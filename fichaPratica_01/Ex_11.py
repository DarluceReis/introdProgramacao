saldoInicial = float(input("Digite o seu saldo inicial do banco: "))
valorM = float(input("Digite o valor que deseja movimentar: "))
operacao = str(input("Qual operação deseja realizar? Digite sacar ou depositar. "))

if operacao == "sacar":
    saldoFinal = saldoInicial - valorM
    
elif operacao == "depositar":
    saldoFinal = saldoInicial + valorM

print(f"Saldo atual: {saldoFinal}")

if saldoFinal < 0:
    print(f"O saldo final está negativo!")

else:
    print(f"O saldo final está positivo!")
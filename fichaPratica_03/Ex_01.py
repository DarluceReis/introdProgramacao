# Número máximo de tentativas (limitar o uso do 'for')
max_repeticoes = 10
 
for i in range(max_repeticoes):
    # Solicita os dois valores e a operação
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                print("Erro: Divisão por zero não permitida!")
                continue
            resultado = num1 / num2
        else:
            print("Operação inválida. Tente novamente.")
            continue

        print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")

        repetir = input("Deseja realizar outra operação? (s/n): ").lower()
        if repetir != 's':
            print("Encerrando a calculadora. Até logo!")
            break
    except ValueError:
        print("Entrada inválida! Por favor, digite números válidos.")

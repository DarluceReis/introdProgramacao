opcao = int(input("Selecione a opção desejada: \n 1 - Criar \n 2 - Atualizar \n 3 - Eliminar \n 4 - Sair \n"))

if opcao == 1:
    nome = str(input("Vamos criar o seu cadastro! Informe o seu nome: "))
    print(f"Nome criado! Seja bem vinde {nome}")

elif opcao == 2:
    nome = str(input("Informe o nome atualizado para o cadastro: "))
    print(f"Cadastro atualizado, {nome}")

elif opcao == 3:
    nome = "desconhecido"
    print(f"o nome cadastrado foi eliminado! O seu nome é {nome}")

elif opcao == 4:
    print("Bem vinde a página inicial!")

else:
    print ("ERRO! Informe um número referente ao menu informado anteriormente")
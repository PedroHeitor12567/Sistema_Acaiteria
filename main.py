from lib import *
from tabulate import tabulate

while True:
    dados = [
        ["Escolha uma das opções para começar: \n1 --> Cadastrar cliente \n2 --> Entrar na conta \n3 --> Esqueci a senha \n4 --> Sair"]
    ]
    tabela = tabulate(dados, headers=["Bem-vindo ao sistema do Açaí Família!"], tablefmt="grid")
    print(tabela)

    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        
        cadastar_cliente()
    elif opcao == "2":
        dados_login = entrar_na_conta()
        if not dados_login:
            continue
        verif_conta = dados_login[-1]

        if verif_conta == "Normal":
            while True:
                apelido = dados_login[3]
                dados = [
                    ["1 --> Fazer pedido \n2 --> Consultar histórico de pedidos \n3 --> Consultar meus dados \n4 --> Editar dados \n5 --> Entrar em contato \n6 --> Voltar para o menu"]
                ]
                tabela = tabulate(dados, headers=[f"Bem vindo à sua conta, {apelido}!"], tablefmt="grid")
                print(tabela)
                opcao = input("Escolha uma das opções para prosseguir: ")
                if opcao == "1":
                    print()
                elif opcao == "2":
                    print()
                elif opcao == "3":
                    aces = dados_login[:4]
                    print(acessar_dados_normal(*aces))
                elif opcao == "4":
                    editar_dados_normal()
                elif opcao == "5":
                    print()
                elif opcao == "6":
                    sair = "Voltando para o menu"
                    carregamento(sair)
                    break
                
    elif opcao == "3":        
        esqueci_senha()
    elif opcao == "4":
        sair = "Saindo do sistema"
        carregamento(sair)
        break
    else:
        print("Opção inválida! Tente novamente.")
        continue
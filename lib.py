from email_validator import validate_email, EmailNotValidError
import os 
import csv
from datetime import datetime
import time
from tabulate import tabulate


arquivo_csv = "cadastro_clientes.csv"
arquivo_csv_menor = "cadrasto_clientes_menores.csv" 

def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")

def check_email(email):
    try:
        v = validate_email(email)
        if email == v.email:
            print("E-mail válido!")
    except EmailNotValidError:
        print("E-mail inválido!")
        return cadastar_cliente()

def carregamento(linha):
    print(linha, end="", flush=True)
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1)

def cadastar_cliente(arquivo="cadastro_clientes.csv"):
    print("Comece a se cadastrar!")
    email = input("Digite o seu e-mail: ").strip()
    check_email(email)
    while True:
        senha = input("Digite a sua senha: ").strip()
        senha_comfirmar = input("Confirme a sua senha: ").strip()
        if senha == senha_comfirmar:
            print("Senha cadastrada com sucesso!")
            break
        else:
            print("As senhas não coincidem. Tente novamente.")
            continue
    apelido = input("Digite o nome na qual deseja ser chamado (Se o apelido for desrespeitoso ou ofensivo, a conta será suspensa): ")
    while True:
        data_nascimento = input("Digite a sua data de nascimento (DD/MM/AAAA): ").strip()
        try:
            verif_data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
            hoje = datetime.today()
            idade = hoje.year - verif_data_nascimento.year - ((hoje.month, hoje.day) < (verif_data_nascimento.month, verif_data_nascimento.day))
            if idade < 18:
                print("Você precisa ter pelo menos 18 anos para se cadastrar. \nDigite o E-mail do responsável para poder prosseguir, o responsável já deve possuir uma conta no sistema.")
                while True:
                    email_responsavel = input("Digite o e-mail do seu responsável: ").strip()
                    check_email(email_responsavel)
                    senha_responsavel = input("Digite a senha do seu responsável: ").strip()
                    vef = "Verificando se a conta está no sistema"
                    carregamento(vef)
                    responsavel = False
                    try:
                        with open(arquivo_csv, mode="r", newline="", encoding="utf-8") as arquivo:
                            leitor = csv.reader(arquivo)
                            for linha in leitor:
                                if len(linha) == 4:
                                    email_salvo, senha_salva, _, apelido_salvo = linha
                                    if email_responsavel == email_salvo.strip() and senha_responsavel == senha_salva.strip():
                                        responsavel = True
                                        break
                        if responsavel:
                            print(f"\nResponsável encontrado: {apelido_salvo}. Cadastro permitido!")
                            if not os.path.exists(arquivo_csv_menor):
                                with open(arquivo_csv_menor, "w", newline="", encoding="utf-8") as arquivo_menor:
                                    escrever_menor = csv.writer(arquivo_menor)
                                    escrever_menor.writerow(["E-mail", "Senha", "Data de Nascimento", "Apelido", "Apelido do Responsável", "Senha Responsável"])
                            with open(arquivo_csv_menor, "a", newline="", encoding="utf-8") as arquivo_menor:
                                escrever_menor = csv.writer(arquivo_menor)
                                escrever_menor.writerow([email, senha, data_nascimento, apelido, apelido_salvo, senha_salva])
                            print("Cadrasto realizado com sucesso!")
                            return True
                        else:
                            print("E-mail ou senha incorretos.")

                    except FileNotFoundError:
                        print("Erro: O arquivo de usuários não foi encontrado.")
                        return False
            else:
                print("Idade confirmada! Cadastro permitido.")
                break
        except ValueError:
            print("Formato inválido! Use DD/MM/AAAA.")

    if not os.path.exists(arquivo):
        with open(arquivo_csv, "w", newline="", encoding="utf-8") as arquivo:
            escrever = csv.writer(arquivo)
            escrever.writerow(["E-mail", "Senha", "Data de Nascimento", "Apelido"])
    with open(arquivo_csv, "a", newline="", encoding="utf-8") as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerow([email, senha, data_nascimento, apelido])

    print("Cadastro realizado com sucesso!")

import csv

def entrar_na_conta(arquivo="cadastro_clientes.csv", arquivo_menor="cadastro_clientes_kid.csv"):
    while True:  
        email = input("Digite seu e-mail: ").strip()
        senha = input("Digite sua senha: ").strip()

        try:
            with open(arquivo, mode="r", newline="", encoding="utf-8") as arquivo_normal:
                leitor = csv.reader(arquivo_normal)
                for linha in leitor:
                    if len(linha) == 4:
                        email_salvo, senha_salva, data_nascimento, apelido = linha
                        if email == email_salvo and senha == senha_salva:
                            print(f"✅ Bem-vindo(a), {apelido}!")
                            return email_salvo, senha_salva, data_nascimento, apelido, "Normal"

            with open(arquivo_menor, mode="r", newline="", encoding="utf-8") as arquivo_kid:
                leitor = csv.reader(arquivo_kid)
                next(leitor, None)  
                for linha in leitor:
                    if len(linha) == 6:
                        email_salvo, senha_salva, data_nascimento, apelido, apelido_responsavel, senha_responsavel = linha
                        if email == email_salvo and senha == senha_salva:
                            print(f"✅ Bem-vindo(a), {apelido}! Responsável: {apelido_responsavel}")
                            return email_salvo, senha_salva, data_nascimento, apelido, apelido_responsavel, "Conta_kid"
            
            print("❌ E-mail ou senha incorretos. Tente novamente.")

        except FileNotFoundError:
            print("❌ Erro: O arquivo de usuários não foi encontrado.")
            return False  

    
def lista_recheios():
    from tabulate import tabulate

    dados = [
        ["1 --> Granulado De Chocolate\n2 --> Tubet's Tradicional\n3 --> Cereal De Chocolate\n4 --> Castanha Triturado\n5 --> Amendoim Em Banda\n6 --> Abacaxi Ao Vinho\n7 --> Choco Leitinho\n8 --> Creme De Paçoca\n9 --> Aveia Em Flocos\n10 --> Creme De Valsa\n", "11 --> Creme De Avelã\n12 --> Choco Waffer\n13 --> Marshmallow\n14 --> Bis Original\n15 --> Chocotrufa\n16 --> Coco Ralado\n17 --> Morango\n18 --> Paçoca\n19 --> Jujuba\n20 --> Óreo\n21 --> Kiwi\n", "22 --> Amendoim Triturado\n23 --> Granulado Colorido\n24 --> Granulado Em Flocos\n25 --> Recheio De Morango\n26 --> Tubet's Recheado\n27 --> Choco Bueníssimo\n28 --> Chocolate Branco\n29 --> Choco Pão De Mel\n30 --> Farinha Láctea\n31 --> Flocos De Arroz\n32 --> Ovomaltine\n", "33 --> Chocotine\n34 --> Leite Em Pó\n35 --> BisBranco\n36 --> OroNegro\n37 --> Granola\n38 --> Confete\n39 --> Banana\n40 --> Cereal\n41 --> Cereja\n42 --> Uva\n"]
    ]

    tabela = tabulate(dados, headers=["Recheios", "Recheios", "Recheios", "Recheios"], tablefmt="grid")

    return tabela

def esqueci_senha():
    email = input("Digite seu e-mail corretamente para a recuperar sua senha: ")
    try:
        with open(arquivo_csv, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if len(linha) == 4:
                    email_salvo, senha_salva, _, _ = linha
                    if email == email_salvo.strip():
                        print(f"E-mail correto! Sua senha é: {senha_salva}")
                        return True

        with open(arquivo_csv_menor, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if len(linha) == 6:
                    email_salvo, senha_salva, _, _, apelido_responsavel_salvo, senha_responsavel_salva = linha
                    if email.strip() == email_salvo.strip():
                        print(f"Você está tentando recuperar a senha de uma conta (kid).")
                        senha_responsavel = input(f"O usuário responsável {apelido_responsavel_salvo} precisa digitar a senha: ")
                        if senha_responsavel == senha_responsavel_salva:
                            print("Senha confirmada!")
                            print(f"A senha da conta kid é: {senha_salva}")
                            return True
                        else:
                            print("Senha do responsável incorreta.")
                            return False
                
        print("E-mail não encontrado.")
        return False
    except FileNotFoundError:
        print("Erro: O arquivo de usuários não foi encontrado.")
        return False

def acessar_dados_normal(email_salvo, senha_salva, data_nascimento, apelido):
    dados = [
        [f"E-mail: {email_salvo} \nSenha: {senha_salva} \nD.Nascimento: {data_nascimento} \nApelido: {apelido}"]
    ]
    tabela = tabulate(dados, headers=[f"Seus dados pessoais!"], tablefmt="grid")
    return tabela

def editar_dados_normal():
    dados = [
        ["1 --> E-mail \n2 --> Senha \n3 --> Apelido"]
    ]

    tabela = tabulate(dados, headers=[f"Escolha o que você deseja editar!"])
    print(tabela)
    opcao = input("Digite qual elemento você vai modificar: ")

    if opcao == "1":
        email_novo = input("Digite seu novo e-mail: ")
        email_antigo = dados_login[0]
        check_email(email_novo)
        linhas_editadas = []
        with open(arquivo_csv, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if linha[0] == email_antigo:
                    linha[0] = email_novo
                linhas_editadas.append(linha)
        with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerows(linhas_editadas)
        print("E-mail atualizado com sucesso")
                 

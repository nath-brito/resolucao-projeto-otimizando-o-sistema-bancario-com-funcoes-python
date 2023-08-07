#Resolução do desafio

saldo = 0
saque = 0
deposito = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUE = 500
usuarios = []
contas = []
cpf = 0
jacadastrado = []
menu ="""
Seja bem vindo! O que deseja realizar hoje?
[1]Criar usuário
[2]Criar conta corrente
[3]Saque
[4]Depósito
[5]Consultar extrato
[6]Sair
"""
opcao = 0

def criarusuario():
    global cpf
    global jacadastrado
    cpf = input("Insira seu CPF")
    jacadastrado = usuariojacadastrado(cpf)
    if jacadastrado:    
        print("Erro na operação. Usuário já cadastrado no sistema")
    else:
        nome = input("insira seu nome completo") 
        datadenascimento = input("insira sua data de nascimento (dd-mm-aaaa)")
        endereco = input("insirta seu endereço (logradouro, número - bairro - cidade/sigla do estado)")

        usuarios.append({"nome": nome, "data de nascimento": datadenascimento, "cpf": cpf, "endereço": endereco})
        print("Seu usuário foi criado com sucesso!")
        
def usuariojacadastrado(self):
    global jacadastrado
    jacadastrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return True if jacadastrado else None

def criarcc(agencia, numconta, usuario):
    global cpf
    global jacadastrado
    cpf = input("Insira seu CPF")
    jacadastrado = usuariojacadastrado(cpf)
    if jacadastrado: 
        contas.append({"agencia": agencia,"número da conta": numconta,"usuário": usuario})
        print("Parabéns! A sua conta foi criada com sucesso")  

    else:
        print("CPF não encontrado no sistema, por favor crie uma conta")
    

def saque():
    saque = int(input("qual valor você deseja sacar?"))
    if saque <= saldo and saque <= 500 and saque > 0: 
             print("saque de realizado com sucesso!")
             numero_saques += 1
             saldo -= saque
             extrato.append(f"Saque de ------- R${saque}")
    elif saque > saldo:
             print("saldo insuficiente")
    elif saque <= 0:
             print("valor inválido")         
    elif saque > 500:
             print("o limite máximo para o saque é de R$500, tente novamente")

def deposito():
    deposito = int(input("informe o valor do depósito"))
    if deposito > 0:
         saldo += deposito
         extrato.append((f"Depósito de ---- R${deposito}"))
    elif deposito <= 0:
         print("valor inválido")

def extrato():
    extrato_print = '\n'.join(extrato)
    print(extrato_print)
    print(f"seu saldo atual é R${saldo}")


while True:
     opcao = int(input(menu))
     #criar usuário
     if opcao == 1:
         criarusuario()
     #criar conta corrente
     elif opcao == 2:
         agencia = input("agencia")
         numconta = input("número da conta")
         usuario = input("usuário")
         criarcc(agencia, numconta, usuario)
     #saque
     elif opcao == 3 and numero_saques < 3:
         saque()
     #saque após o limite diário ser excedido
     elif opcao == 3 and numero_saques == 3:
         print("o seu limite diário de saques foi atingido")   
     #depósito
     elif opcao == 4:
         deposito()
     #extrato
     elif opcao == 5:
         extrato()
     #encerramento do programa
     elif opcao == 6:
         break
     #opção inválida
     else:
         print("operação inválida")

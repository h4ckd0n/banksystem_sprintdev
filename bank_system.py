# Constantes
LIMITE_DIARIO = 1500  # limite de saque diário
LIMITE_SAQUES = 4  # limite de saques por dia

# Variáveis
saldo = 0
extrato = ""
numero_saques = 0
saque_diario = 0  # valor total sacado hoje

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação não concluída! O valor inválido.")

def sacar(valor):
    global saldo, extrato, numero_saques, saque_diario
    if valor > 0:
        if valor > saldo:
            print("Operação não concluída! Saldo insuficiente.")
        elif saque_diario + valor > LIMITE_DIARIO:
            print("Operação não concluída! Valor para saque excede o limite diário.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação não concluída! Número de saques excede o limite diário.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            saque_diario += valor
    else:
        print("Operação não concluída! O valor informado é inválido.")

def poupanca_investimento(valor):
    global saldo, extrato
    if valor > 0:
        if valor > saldo:
            print("Operação não concluída! Saldo insuficiente.")
        else:
            saldo -= valor
            extrato += f"Poupança/Investimento: R$ {valor:.2f}\n"
            print("Operação realizada com sucesso!")
    else:
        print("Operação não concluída! O valor informado é inválido.")

def exibir_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================================")

# Menu: aqui além dos parâmetros do projeto em questão incluí a opção de 'poupança/investimento' como item complementar.
menu = """
================ BANCO PYTHON SPRINTDEV ================

Selecione uma opção:

[d] Depositar
[s] Sacar
[e] Extrato
[p] Poupança/Investimento
[q] Sair

========================================================
>>> """

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)
    elif opcao == "e":
        exibir_extrato()
    elif opcao == "p":
        print("Opção de poupança/investimento selecionada.")
        valor = float(input("Informe o valor para poupança/investimento: "))
        poupanca_investimento(valor)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
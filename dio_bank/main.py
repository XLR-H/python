menu = '''BEM VINDO AO BANCO XL
SERVIÇOS:

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR

SELECIONE O SERVIÇO DESEJADO:'''

saldo = 0
limite = 500
transacoes = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    #DEPOSITO
    if opcao == "1":
        valor = float(input('Digite o valor do depósito:R$ '))
        if valor >0:
            saldo += valor
            transacoes.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido! Digite um valor positivo:")

    #SAQUE
    elif opcao == "2":
        if numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques diários atingido!")
        else:
            valor = float(input("Digite o valor do saque: R$ "))
            if valor > saldo:
                print("Saldo INSUFICIENTE!")
            elif valor > limite:
                print(f"O limite por saque é de R$ {valor:.2f}")
            elif valor >0:
                saldo -= valor
                transacoes.append(f"Saque: R$ {valor:.2f}")
                numero_saques += 1
                print("Saque realizado com sucesso!")
            else:
                print("Valor inválido! Apenas valores positivos são permitidos.")

    #EXTRATO
    elif opcao == "3":
        print("/n*** EXTRATO ***")
        if not transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in transacoes:
                print(transacao)
        print(f"\nSaldo atual: R$ {saldo:.2f}")


    #SAIR
    elif opcao == '4':
        print("Obrigado por usar o BANCO XL")
        break

    else:
        print('OPERAÇÃO INVALIDA!')


#if __name__ == "__main__":
#3
# main()


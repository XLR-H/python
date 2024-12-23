import textwrap


def menu():
    menu = '''\n
    **************** MENU ****************
    [1]\tDEPOSITO
    [2]\tSAQUE
    [3]\tEXTRATO
    [4]\tNOVA CONTA
    [5]\tLISTAR CONTAS
    [6]\tNOVO USUÁRIO
    [0]\tSAIR
    => '''
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'DEPOSITO:\tR$ {valor:.2f}\n'
    else:
        print('\n!!! ERRO! O VALOR INFORMADO É INVALIDO !!!')

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('\n!!! ERRO! SALDO INSUFICIENTE !!!')

    elif excedeu_limite:
        print('\n!!! ERRO! VALOR ACIMA DO LIMITE POR SAQUE !!!')

    elif excedeu_saques:
        print('\n!!! ERRO! NUMERO DE SAQUES EXCEDIDO !!!')

    elif valor > 0:
        saldo -= valor
        extrato += f'SAQUE:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n*** SAQUE REALIZADO COM SUCESSO! ***')

    else:
        print('\n!!! ERRO! O VALOR INFORMADO É INVALIDO !!!')

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('\n*************** EXTRATO ***************')
    print('NÃO FORAM REALIZADAS MOVIMENTAÇÕES' if not extrato else extrato)
    print(f'\nSALDO:\t\tR$ {saldo:.2f}')
    print('*****************************************')


def criar_usuario(usuarios):
    cpf = input('INFORME O CPF (SOMENTE NUMEROS): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n!!! JÁ EXISTE USUÁRIO COM ESTE CPF !!!')
        return

    nome = input('INFORME O NOME COMPLETO: ')
    data_nascimento = input('INFORME A DATA DE NASCIMENTO (DD-MM-AAAA): ')
    endereco = input('INFORME O ENDEREÇO ( RUA, NUM - BAIRRO - CIDADE - ESTADO): ')

    usuarios.append({'nome' : nome , 'data_nascimento' : data_nascimento , 'cpf' : cpf , 'endereco' : endereco})

    print('*** USUÁRIO CADASTRADO COM SUCESSO ***')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('INFORME O CPF DO USUARIO: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n*** CONTA CRIADA COM SUCESSO! ***')
        return {'agencia' : agencia , 'numero_conta' : numero_conta , 'usuario' : usuario}

    print('\n!!! ERRO! USUARIO NÃO ENCONTRADO !!!')


def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            AGENCIA:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            TITULAR:\t{conta['usuario']['nome']}
        '''
        print('*' * 100)
        print(textwrap.dedent(linha))


def main():
    print('***** BEM VINDO(A) AO XL-BANK *****')
    limite_saques = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input('INFORME O VALOR DO DEPOSITO: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input('INFORME O VALOR DO SAQUE: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "0":
            print('***** OBRIGADO POR USAR O XL-BANK *****')
            break

        else:
            print("!!! OPERAÇÃO INVÁLIDA! DIGITE A OPÇÃO DESEJADA !!!")


main()

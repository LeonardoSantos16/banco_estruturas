import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    d - Depositar
    s - Sacar
    e - Extrato
    n - Nova conta
    c - Novo usuário
    q - Sair
    => """
    return input(textwrap.dedent(menu))


def CadastrarUsuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nUsuário já cadastrado")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def CadastrarConta(conta, agencia, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": conta, "usuario": usuario}

    print("\nUsuário não encontrado")


def sacar(*, valor, saldo, extrato, numero_saques):
    if valor < saldo and valor <= 500 and numero_saques < 3:
        saldo -= valor
        extrato += f'valor sacado - {valor} \n'
        numero_saques += 1
        print("Saque realizado")
    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'valor adicionado + {valor} \n'
    else:
        print("Não é possivél adicionar valor negativo")
    return saldo, extrato


def Extrato(saldo, /, *, extrato):
    if len(extrato) == 0:
        print("Não foram realizados movimentações")
    else:
        extrato += f'R$ {saldo:.2f}'
        print(extrato)


def main():
    AGENCIA = "0001"
    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                numero_saques=numero_saques,
            )

        elif opcao == "e":
            Extrato(saldo, extrato=extrato)

        elif opcao == "c":
            CadastrarUsuario(usuarios)

        elif opcao == "n":
            numero_conta = len(contas) + 1
            conta = CadastrarConta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
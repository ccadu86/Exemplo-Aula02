from Classe import *

def main():

    sistema = SistemaBancario()

    while True:
        print("---- Menu ----")
        print("1. Cadastrar cliente")
        print("2. Atualizar cadastro")
        print("3. Excluir cliente")
        print("4. Realizar depósito")
        print("5. Realizar saque")
        print("6. Realizar transferência")
        print("7. Listar clientes cadastrados")
        print("0. Sair")
        print("----------------")
        
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            cliente = Cliente(nome, cpf)
            sistema.cadastrar_cliente(cliente)
        elif opcao == "2":
            cpf = input("Digite o CPF do cliente a ser atualizado: ")
            cliente = sistema.buscar_cliente(cpf)
            if cliente:
                novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
                novo_cpf = input("Digite o novo CPF (ou pressione Enter para manter o atual): ")
                cliente.atualizar_cadastro(novo_nome, novo_cpf)
        elif opcao == "3":
            cpf = input("Digite o CPF do cliente a ser excluído: ")
            cliente = sistema.buscar_cliente(cpf)
            if cliente:
                cliente.excluir_cliente()
        elif opcao == "4":
            cpf = input("Digite o CPF do cliente: ")
            cliente = sistema.buscar_cliente(cpf)
            if cliente:
                valor = float(input("Digite o valor do depósito: "))
                cliente.deposito(valor)
        elif opcao == "5":
            cpf = input("Digite o CPF do cliente: ")
            cliente = sistema.buscar_cliente(cpf)
            if cliente:
                valor = float(input("Digite o valor do saque: "))
                cliente.saque(valor)
        elif opcao == "6":
            cpf_origem = input("Digite o CPF do cliente de origem: ")
            cliente_origem = sistema.buscar_cliente(cpf_origem)
            if cliente_origem:
                cpf_destino = input("Digite o CPF do cliente de destino: ")
                cliente_destino = sistema.buscar_cliente(cpf_destino)
                if cliente_destino:
                    valor = float(input("Digite o valor da transferência: "))
                    cliente_origem.transferencia(cliente_destino, valor)
        elif opcao == "7":
            print("Clientes cadastrados:")
            for cpf, cliente in sistema.clientes.items():
                print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}, Saldo: R${cliente.saldo:.2f}")
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")
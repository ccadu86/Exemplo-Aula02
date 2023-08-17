class Cliente:
    def __init__(self, nome, cpf, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")

    def transferencia(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.deposito(valor)
            print(f"Transferência de R${valor:.2f} realizada para {destino.nome}. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para a transferência.")

    def atualizar_cadastro(self, nome=None, cpf=None):
        if nome:
            self.nome = nome
        if cpf:
            self.cpf = cpf
        print("Cadastro atualizado com sucesso.")

    def excluir_cliente(self):
        del self
        print("Cliente excluído com sucesso.")


class SistemaBancario:
    def __init__(self):
        self.clientes = {}

    def cadastrar_cliente(self, cliente):
        self.clientes[cliente.cpf] = cliente
        print(f"Cliente {cliente.nome} cadastrado com sucesso.")

    def buscar_cliente(self, cpf):
        if cpf in self.clientes:
            return self.clientes[cpf]
        else:
            print("Cliente não encontrado.")
            return None
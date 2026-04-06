class Cliente:
    def __init__(self, nome, telefone, email, id_cliente):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id_cliente = id_cliente

class Quarto:
    def __init__(self, numero, tipo, preco_diaria, disponivel=True):
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria
        self.disponivel = disponivel

class Reserva:
    def __init__(self, id_reserva, cliente, quarto, check_in, check_out, status="Ativa"):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.quarto = quarto
        self.check_in = check_in
        self.check_out = check_out
        self.status = status

class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print("Cliente adicionado com sucesso!")

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)
        print("Quarto adicionado com sucesso!")

    def verificar_disponibilidade(self, numero_quarto):
        for quarto in self.quartos:
            if quarto.numero == numero_quarto:
                if quarto.disponivel == True:
                    print("Quarto disponível")
                    return True
                else:
                    print("Quarto indisponível")
                    return False

        print("Quarto não encontrado")
        return False

    def criar_reserva(self, reserva):
        if reserva.quarto.disponivel == True:
            self.reservas.append(reserva)
            reserva.quarto.disponivel = False
            print("Reserva criada com sucesso!")
        else:
            print("Não foi possível criar a reserva, Quarto indisponível")

    def cancelar_reserva(self, id_reserva):
        for reserva in self.reservas:
            if reserva.id_reserva == id_reserva:
                reserva.status = "Cancelada"
                reserva.quarto.disponivel = True
                print("Reserva cancelada com sucesso!")
                return

        print("Reserva não encontrada")

    def modificar_reserva(self, id_reserva, novo_check_in, novo_check_out):
        for reserva in self.reservas:
            if reserva.id_reserva == id_reserva:
                if reserva.status == "Ativa":
                    reserva.check_in = novo_check_in
                    reserva.check_out = novo_check_out
                    print("Reserva modificada com sucesso!")
                    return
                else:
                    print("Não é possível modificar uma reserva cancelada")
                    return

        print("Reserva não encontrada.")

    def listar_reservas(self):
        if len(self.reservas) == 0:
            print("Não há reservas cadastradas.")
        else:
            for reserva in self.reservas:
                print("ID da reserva:", reserva.id_reserva)
                print("Cliente:", reserva.cliente.nome)
                print("Quarto:", reserva.quarto.numero)
                print("Check-in:", reserva.check_in)
                print("Check-out:", reserva.check_out)
                print("Status:", reserva.status)
                print("-------------------------")

    def listar_clientes(self):
        if len(self.clientes) == 0:
            print("Não há clientes cadastrados.")
        else:
            for cliente in self.clientes:
                print("ID:", cliente.id_cliente)
                print("Nome:", cliente.nome)
                print("Telefone:", cliente.telefone)
                print("Email:", cliente.email)
                print("-------------------------")
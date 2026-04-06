from clientesModel import inserir_cliente, listar_clientes
from quartosModel import inserir_quarto, listar_quartos, verificar_disponibilidade
from reservasModel import inserir_reserva, listar_reservas, cancelar_reserva, modificar_reserva


class GerenciadorDeReservas:
    def adicionar_cliente(self, cliente):
        print(inserir_cliente(cliente))

    def adicionar_quarto(self, quarto):
        print(inserir_quarto(quarto))

    def verificar_disponibilidade(self, numero_quarto):
        print(verificar_disponibilidade(numero_quarto))

    def criar_reserva(self, reserva):
        print(inserir_reserva(reserva))

    def cancelar_reserva(self, id_reserva):
        print(cancelar_reserva(id_reserva))

    def modificar_reserva(self, id_reserva, novo_check_in, novo_check_out):
        print(modificar_reserva(id_reserva, novo_check_in, novo_check_out))

    def listar_reservas(self):
        reservas = listar_reservas()

        if len(reservas) == 0:
            print("Não há reservas cadastradas.")
        else:
            for reserva in reservas:
                print("ID da reserva:", reserva["id_reserva"])
                print("Cliente:", reserva["cliente"])
                print("Quarto:", reserva["quarto"])
                print("Check-in:", reserva["check_in"])
                print("Check-out:", reserva["check_out"])
                print("Status:", reserva["status"])
                print("-------------------------")

    def listar_clientes(self):
        clientes = listar_clientes()

        if len(clientes) == 0:
            print("Não há clientes cadastrados.")
        else:
            for cliente in clientes:
                print("ID:", cliente["id_cliente"])
                print("Nome:", cliente["nome"])
                print("Telefone:", cliente["telefone"])
                print("Email:", cliente["email"])
                print("-------------------------")
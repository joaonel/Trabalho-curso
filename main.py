from classes import Cliente, Quarto, Reserva
from gerenciador import GerenciadorDeReservas

gerenciador = GerenciadorDeReservas()

cliente1 = Cliente("Tifanny", "85999999999", "tifanny@gmail.com", 1)
quarto1 = Quarto(101, "suite", 250.00)

gerenciador.adicionar_cliente(cliente1)
gerenciador.adicionar_quarto(quarto1)

reserva1 = Reserva(1, cliente1, quarto1, "2026-04-10", "2026-04-15")
gerenciador.criar_reserva(reserva1)

gerenciador.listar_clientes()
gerenciador.listar_reservas()
gerenciador.verificar_disponibilidade(101)
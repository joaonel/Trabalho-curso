import streamlit as st
from classes import Cliente, Quarto, Reserva
from gerenciador import GerenciadorDeReservas

gerenciador = GerenciadorDeReservas()

st.title("Sistema de Hospedagem")

opcao = st.sidebar.selectbox(
    "Escolha uma opção",
    [
        "Cadastrar Cliente",
        "Cadastrar Quarto",
        "Criar Reserva",
        "Verificar Disponibilidade",
        "Cancelar Reserva",
        "Modificar Reserva",
        "Listar Clientes",
        "Listar Reservas"
    ]
)

if opcao == "Cadastrar Cliente":
    st.header("Cadastrar Cliente")

    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone")
    email = st.text_input("Email")
    id_cliente = st.number_input("ID do Cliente", min_value=1, step=1)

    if st.button("Cadastrar Cliente"):
        cliente = Cliente(nome, telefone, email, id_cliente)
        gerenciador.adicionar_cliente(cliente)
        st.success("Cliente cadastrado com sucesso!")

elif opcao == "Cadastrar Quarto":
    st.header("Cadastrar Quarto")

    numero = st.number_input("Número do quarto", min_value=1, step=1)
    tipo = st.selectbox("Tipo do quarto", ["single", "double", "suite"])
    preco_diaria = st.number_input("Preço da diária", min_value=0.0, step=0.5)

    if st.button("Cadastrar Quarto"):
        quarto = Quarto(numero, tipo, preco_diaria, True)
        gerenciador.adicionar_quarto(quarto)
        st.success("Quarto cadastrado com sucesso!")

elif opcao == "Criar Reserva":
    st.header("Criar Reserva")

    id_reserva = st.number_input("ID da reserva", min_value=1, step=1)
    id_cliente = st.number_input("ID do cliente", min_value=1, step=1)
    numero_quarto = st.number_input("Número do quarto", min_value=1, step=1)
    check_in = st.text_input("Check-in (AAAA-MM-DD)")
    check_out = st.text_input("Check-out (AAAA-MM-DD)")

    if st.button("Criar Reserva"):
        cliente = Cliente("", "", "", id_cliente)
        quarto = Quarto(numero_quarto, "", 0, True)
        reserva = Reserva(id_reserva, cliente, quarto, check_in, check_out)
        gerenciador.criar_reserva(reserva)
        st.success("Tentativa de reserva realizada!")

elif opcao == "Verificar Disponibilidade":
    st.header("Verificar Disponibilidade")

    numero_quarto = st.number_input("Número do quarto", min_value=1, step=1)

    if st.button("Verificar"):
        gerenciador.verificar_disponibilidade(numero_quarto)

elif opcao == "Cancelar Reserva":
    st.header("Cancelar Reserva")

    id_reserva = st.number_input("ID da reserva", min_value=1, step=1)

    if st.button("Cancelar Reserva"):
        gerenciador.cancelar_reserva(id_reserva)
        st.success("Operação realizada!")

elif opcao == "Modificar Reserva":
    st.header("Modificar Reserva")

    id_reserva = st.number_input("ID da reserva", min_value=1, step=1)
    novo_check_in = st.text_input("Novo check-in (AAAA-MM-DD)")
    novo_check_out = st.text_input("Novo check-out (AAAA-MM-DD)")

    if st.button("Modificar Reserva"):
        gerenciador.modificar_reserva(id_reserva, novo_check_in, novo_check_out)
        st.success("Operação realizada!")

elif opcao == "Listar Clientes":
    st.header("Clientes cadastrados")
    gerenciador.listar_clientes()

elif opcao == "Listar Reservas":
    st.header("Reservas cadastradas")
    gerenciador.listar_reservas()
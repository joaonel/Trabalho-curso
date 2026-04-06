from db import conectar

def inserir_reserva(reserva):
    conexao = conectar()
    cursor = conexao.cursor()

    sql_verificar = "SELECT disponivel FROM quartos WHERE numero = %s"
    cursor.execute(sql_verificar, (reserva.quarto.numero,))
    quarto = cursor.fetchone()

    if quarto is None:
        cursor.close()
        conexao.close()
        return "Quarto não encontrado."

    if quarto[0] == 0:
        cursor.close()
        conexao.close()
        return "Quarto indisponível."

    sql = """
    INSERT INTO reservas (id_reserva, id_cliente, numero_quarto, check_in, check_out, status)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        reserva.id_reserva,
        reserva.cliente.id_cliente,
        reserva.quarto.numero,
        reserva.check_in,
        reserva.check_out,
        reserva.status
    )

    cursor.execute(sql, valores)

    sql_update = "UPDATE quartos SET disponivel = %s WHERE numero = %s"
    cursor.execute(sql_update, (False, reserva.quarto.numero))

    conexao.commit()
    cursor.close()
    conexao.close()

    return "Reserva criada com sucesso!"


def listar_reservas():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
    SELECT 
        r.id_reserva,
        c.nome AS cliente,
        q.numero AS quarto,
        r.check_in,
        r.check_out,
        r.status
    FROM reservas r
    INNER JOIN clientes c ON r.id_cliente = c.id_cliente
    INNER JOIN quartos q ON r.numero_quarto = q.numero
    """

    cursor.execute(sql)
    reservas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return reservas


def cancelar_reserva(id_reserva):
    conexao = conectar()
    cursor = conexao.cursor()

    sql_busca = "SELECT numero_quarto FROM reservas WHERE id_reserva = %s"
    cursor.execute(sql_busca, (id_reserva,))
    reserva = cursor.fetchone()

    if reserva is None:
        cursor.close()
        conexao.close()
        return "Reserva não encontrada."

    numero_quarto = reserva[0]

    sql_cancelar = "UPDATE reservas SET status = %s WHERE id_reserva = %s"
    cursor.execute(sql_cancelar, ("Cancelada", id_reserva))

    sql_liberar = "UPDATE quartos SET disponivel = %s WHERE numero = %s"
    cursor.execute(sql_liberar, (True, numero_quarto))

    conexao.commit()
    cursor.close()
    conexao.close()

    return "Reserva cancelada com sucesso!"


def modificar_reserva(id_reserva, novo_check_in, novo_check_out):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE reservas
    SET check_in = %s, check_out = %s
    WHERE id_reserva = %s AND status = %s
    """

    cursor.execute(sql, (novo_check_in, novo_check_out, id_reserva, "Ativa"))
    conexao.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conexao.close()
        return "Reserva não encontrada ou cancelada."

    cursor.close()
    conexao.close()

    return "Reserva modificada com sucesso!"
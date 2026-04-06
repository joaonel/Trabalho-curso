from db import conectar

def inserir_quarto(quarto):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO quartos (numero, tipo, preco_diaria, disponivel) VALUES (%s, %s, %s, %s)"
    valores = (quarto.numero, quarto.tipo, quarto.preco_diaria, quarto.disponivel)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    return "Quarto cadastrado com sucesso!"


def listar_quartos():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM quartos")
    quartos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return quartos


def verificar_disponibilidade(numero_quarto):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = "SELECT disponivel FROM quartos WHERE numero = %s"
    cursor.execute(sql, (numero_quarto,))
    quarto = cursor.fetchone()

    cursor.close()
    conexao.close()

    if quarto is None:
        return "Quarto não encontrado."

    if quarto["disponivel"]:
        return "Quarto disponível."
    else:
        return "Quarto indisponível."
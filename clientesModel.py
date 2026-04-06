from db import conectar

def inserir_cliente(cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO clientes (id_cliente, nome, telefone, email) VALUES (%s, %s, %s, %s)"
    valores = (cliente.id_cliente, cliente.nome, cliente.telefone, cliente.email)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    return "Cliente cadastrado com sucesso!"


def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    cursor.close()
    conexao.close()

    return clientes
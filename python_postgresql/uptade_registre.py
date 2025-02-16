import connect

def update_reg(teléfono_cliente, nombre_cliente):
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_update = '''
    UPDATE clientes
    SET teléfono_cliente = %s
    WHERE nombre_cliente = %s
    '''

    cursor.execute(sql_update, (teléfono_cliente, nombre_cliente))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Update successfully"}
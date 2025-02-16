import connect

def read_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_read = "SELECT * FROM clientes"

    cursor.execute(sql_read)
    conn.commit()

    results = cursor.fetchall()  # Obtenim els resultats


    cursor.close()
    conn.close()  # Cerrar la conexión

    return results  # Asegurar que la función devuelve algo
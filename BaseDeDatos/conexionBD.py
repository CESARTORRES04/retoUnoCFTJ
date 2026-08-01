import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "kafka",
        password = "kafka123",
        database = "tienda_meta"
    )


if __name__ == "__main__":
    conn = get_connection()
    print("Conexión exitosa", conn.is_connected)
    conn.close()
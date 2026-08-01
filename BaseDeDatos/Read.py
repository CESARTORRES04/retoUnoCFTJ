from conexionBD import get_connection

def listar_productos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")

    for producto in cursor.fetchall():
        print(producto)

    cursor.close()
    conn.close()

def listar_productos_categoria_computacion(categoria):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos where categoria = %s", (categoria,))

    for producto in cursor.fetchall():
        print(producto)

    cursor.close()
    conn.close()

def listar_productos_precio_mayor_5000():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT nombre, precio FROM productos where precio > 5000")

    for producto in cursor.fetchall():
        print(producto)

    cursor.close()
    conn.close()



if __name__ == "__main__":
    print("Listar productos precio \n")
    listar_productos_precio_mayor_5000()
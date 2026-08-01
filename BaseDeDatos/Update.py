from conexionBD import get_connection
from Read import listar_productos




def actualizar_stock(id_producto, nuevo_stock):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("UPDATE productos SET stock = %s where id = %s", (nuevo_stock, id_producto))
    conn.commit()
    print(f"Filas afectadas: {cursor.rowcount}")
    cursor.close()
    conn.close()


if __name__ == "__main__":
    actualizar_stock(20,10)
    print("Listar productos\n")
    listar_productos()
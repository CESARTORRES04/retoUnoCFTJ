from conexionBD import get_connection
from Read import listar_productos




def eliminar_producto(id_producto):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM productos where id = %s", (id_producto,))
    conn.commit()
    print(f"Filas afectadas: {cursor.rowcount}")
    cursor.close()
    conn.close()


if __name__ == "__main__":
    eliminar_producto(13)
    print("Listar productos\n")
    listar_productos()
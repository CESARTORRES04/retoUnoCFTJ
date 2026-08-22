from conexionBD import get_connection

def insertar_pedido(producto_id,cantidad, fecha):
    conn = get_connection()
    cursor = conn.cursor()
    consulta = "insert into pedidos (producto_id, cantidad, fecha) values (%s,%s,%s)"
    cursor.execute(consulta,(producto_id,cantidad, fecha))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    print("Insertar pedidos \n")
    insertar_pedido(7,1,"2026-08-08")
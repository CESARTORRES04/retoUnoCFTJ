usuarios = []





def log_evento(nivel: str, *mensajes:str,**contexto):   
    texto_informativo_mensajes = " ".join(str(mensaje) for mensaje in mensajes)

    formato_nivel= f"[{nivel}]".ljust(9)

    if contexto:
        ctx = " ".join(
            f"{k}={v}"
            for k , v in contexto.items()
        )
        print(f" {formato_nivel} {texto_informativo_mensajes} | {ctx}")
    

def agregar_usuario(nombre,numeroControl):
    usuario = {
        "nombre":nombre,
        "numeroControl":numeroControl
    }
    usuarios.append(usuario)
    log_evento("INFO","Usuario agregado", "Usuario Caragado", modulo = "Modulo Ventas")


agregar_usuario("Antonio","123243")


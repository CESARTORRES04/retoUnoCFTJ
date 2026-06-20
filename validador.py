def validar_datos(datos):
    if not datos['nombre'].strip():
        raise ValueError('Valor valido requerido')
    
    if '@' not in datos['email'].strip():
        raise ValueError('Correo es incorrecto, falta arroba')
    

def valida_nombre(valor):



    

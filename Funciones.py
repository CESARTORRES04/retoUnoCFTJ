#Funciones
#Basica
def saludar(grupo):
    print(f"Bienvenido al curso grupo {grupo}")

saludar("Middle")
#Retorno
def sumar(a , b):
    return a + b

resultado = sumar(400,345)

print(resultado)


#Parámetros por defecto
#Basica
def crear_usuario(nombre, rol="Lector"):
    return {
    "nombre": nombre,
    "rol":rol
    }

print(crear_usuario("Julio"))

print(crear_usuario("Maria","Editor"))


#*args
def sumar_todo(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    
    return total

print(sumar_todo(678, 43, 57, 23))


#**kwargs

def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(clave , ":", valor)


mostrar_datos(username="cesar160450",password="fjsjfn",controlNumber = "1242434323")





    


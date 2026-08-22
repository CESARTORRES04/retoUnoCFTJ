def calcular(a,op,b):

    operaciones = {
        '+': lambda x, y : x + y,
        '-': lambda x, y : x - y,
        '*': lambda x, y : x * y,
        '/': lambda x, y : x / y,
    }
    
    if op not in operaciones:
        print(f"El operador '{op}' no es reconocido")
        return None
    
    try:
        return operaciones[op] (a,b)
    
    except TypeError as e:
        print(f"Tipo de dato incorrecto: {e}")

    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        print("Operación terminada")
        #rollback


def leer_numero(numero):
    while True:
        try:
            return float(input(numero))
        except ValueError:
            print("Ingresa un número valido")


def main():
    print("***Calculadora***")
    a = leer_numero("Ingrese el valor de a: ")
    op = input('Operador + - * /')
    b = leer_numero("Ingrese el valor de b: ")

    print(calcular(a,op,b))


main()


#Happy path
#Casos de error


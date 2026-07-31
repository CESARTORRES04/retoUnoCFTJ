import csv
import os
ARCHIVO = 'contactos.csv'
COLUMNAS = ['nombre', 'telefono', 'email']

def cargar_csv(archivo):
    if not os.path.exists(archivo):
        return []
    with open(archivo, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)


def guardar_csv(archivo, datos):
    with open(archivo, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNAS)
        writer.writeheader()
        writer.writerows(datos)


def mostrar(contactos):
    if not contactos:
        print('No hay contactos.')
        return
    for c in contactos:
        print(f"- {c['nombre']} | {c['telefono']} | {c['email']}")

def agregar(contactos):
    nombre = input('Nombre: ')
    telefono = input('Teléfono: ')
    email = input('Email: ')
    contactos.append({'nombre': nombre, 'telefono': telefono, 'email': email})

def eliminar(contactos):
    nombre = input('Nombre a eliminar: ')
    for c in contactos:
        if c['nombre'].lower() == nombre.lower():
            contactos.remove(c)
            print('Eliminado.')
            return
    print('No se encontró ese contacto.')

def menu():
    contactos = cargar_csv(ARCHIVO)
    while True:
        print('\n1. Ver 2. Agregar 3. Eliminar 4. Salir')
        opcion = input('Opción: ')
        match opcion:
            case '1':
                mostrar(contactos)
            case '2':
                agregar(contactos)
                guardar_csv(ARCHIVO, contactos)
            case '3':
                eliminar(contactos)
                guardar_csv(ARCHIVO, contactos)
            case '4':
                print('¡Hasta luego!')
                break
            case _:
                print('Opción no válida.')

def agregar_producto(productos):

    nombre = input('Nombre del producto: ')
    precio = float(input('Precio: '))
    stock = int(input('Stock inicial: '))
    
    if precio < 0 or stock < 0:
        print('El precio y el stock no pueden ser negativos.')
        return
    productos.append({
    'id': siguiente_id(productos),
    'nombre': nombre,
    'precio': precio,
    'stock': stock
    })
    print('Producto agregado.')


menu()
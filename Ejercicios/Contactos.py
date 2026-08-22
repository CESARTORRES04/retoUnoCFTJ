import json

def cargar_json(archivo):
    try:
        with open(archivo,'r',encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Archivo corrupto")
    return []

def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos.")
        return
    print("Lista de contactos")
    for contacto in contactos:
        print(f"- {contacto['nombre']}  | {contacto['email']} ")
        for telefono in contacto['telefonos']:
            print(f' Tel: {telefono}')


def agregar_contacto(contactos): 
    nombre = input('Nombre: ')
    email = input('Email: ')

    telefonos = []

    while True:
        telefono = input('Telefono: ')
        telefonos.append(telefono)
        otro = input("Desea agregar otro telefono: (s/n) ")
        if otro.lower() != 's':
            break
    
    contactos.append({'id':generar_id(contactos),'nombre':nombre, 'telefonos':telefonos, 'email':email})
    print("Contacto agregado")

def eliminar_contacto(contactos):
    nombre = input('Nombre del contacto que desea eliminar: ')
    for contacto in contactos:
        if contacto['nombre'].lower() == nombre.lower():
            contactos.remove(contacto)
            print("Contacto eliminado")
            return
    print("Sin resultados")

def guardar_json(archivo, contactos):
    with open(archivo,'w',encoding='utf-8') as file:
        return json.dump(contactos,file, ensure_ascii=False, indent=2)


def generar_id(contactos):
    if not contactos:
        return 1
    return max(contacto['id'] for contacto in contactos) + 1

def menu_contactos():
    archivo = "C:/Users/cesar/Downloads/contactos.json"
    contactos = cargar_json(archivo)
    while True:
        print('\nAgenda \n1.- Agregar \n 2.- Ver \n 3.- Eliminar \n4.- Salir')

        opcion = input('Opción: ')

        match opcion:
            case '1':
                agregar_contacto(contactos)
                guardar_json(archivo,contactos)

            case '2':
                mostrar_contactos(contactos)

            case '3':
                eliminar_contacto(contactos)
                guardar_json(archivo,contactos)
            
            case '4':
                print('Hasta luego')
                break

            case _:
                print('Opción incorrecta')


menu_contactos()



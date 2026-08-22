import csv

def leer_archivo(ruta):
    archivo = None
    try:
        archivo = open(ruta,'r',encoding='utf-8')
        lector = csv.DictReader(archivo)
        return list[lector]
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}")
        return []
    except PermissionError:
        print(f"Sin permiso para leer: {ruta}")
    finally:
        print("Operación terminada")
        if archivo:
            archivo.close()
    #read
    #write
    


leer_archivo('datos.csv')

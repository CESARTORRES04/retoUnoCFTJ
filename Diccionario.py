#Diccionarios -> Clave - Valor
empleado = {
    "nombre": "Ricardo",
    "edad":28,
    "activo":True
}


print(empleado.get("nombre"),empleado.get("edad"))

for clave, valor in empleado.items():
    print(clave , ":", valor)

print(empleado.keys())

print(empleado.values())
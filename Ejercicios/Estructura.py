#Listas

usuarios = ["Ana","Luis","Pedro","Cesar"]

print(usuarios)

for usuario in usuarios:
    print(usuario)

usuarios.append("Jorge")
usuarios.append("Roberto")
print(usuarios)

ultimo = usuarios.pop()

print(ultimo)
#usuarios.remove("Mayra")
print(len(usuarios))

usuarios.sort()

print(usuarios)


#Comprensión lista
print("****************************************************")
numeros = [1 , 2 , 3 , 4, 5, 6]


#Transformación
pares = [numero for numero in numeros if numero % 2  == 0]

dobles = [numero * 2 for numero in numeros]



print(numeros)
print(pares)
print(dobles)




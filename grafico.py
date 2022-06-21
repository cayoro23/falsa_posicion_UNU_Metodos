import pandas as pd

cantidad = int(input("Ingrese la cantidad de datos: "))

array1 = []

for x in range(cantidad):
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    lista = [nombre, edad]
    array1.append(lista)

print(array1)

data = pd.DataFrame(array1, columns=['EJE X', 'EJE Y'])

print(data)

n = int(input("Ingrese en la cantidad de datos de su lista: "))
lista = []

for i in range(1, n+1):
    lista.append(i**2)
    
print(f"La lista con los cuadrados es: {lista}")
    
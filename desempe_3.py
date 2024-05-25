lista = ['gato','perro','almohada','raton','casa','gato','casa','casa','rojo']
name = input('Ingrese la palabra que desea encontrar en la lista: ')
posiciones = []  # Lista para almacenar las posiciones

for i, palabra in enumerate(lista):
    if palabra == name:
        posiciones.append(i)  # Agregar la posición a la lista

if posiciones:  # Si se encontraron coincidencias
    print(f"La palabra '{name}' se encuentra en las posiciones:", posiciones)
else:
    print(f"La palabra '{name}' no se encuentra en la lista.")

        
        


class lista():
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
c = int(input("Ingrese la cantidad de productos que desea comprar:"))    
   
productos = []
total = 0

for i in range(c):
    print(f"Producto {i+1}")
    n = str(input("Nombre del producto: "))
    vr = int(input("Valor del producto: "))
    cant = int(input("Cantidad del producto: "))
    p = lista(n, vr, cant)
    productos.append(p)
    
    # Calcular y acumular el total
    p_neto = vr * cant
    total += p_neto

print("------LISTADO DE PRODUCTOS--------")
for j in range(len(productos)):
    print(f"Nombre:{productos[j].nombre}")
    print(f"Precio:{productos[j].precio}")
    print(f"Cantidad:{productos[j].cantidad}")
    print(f"Neto: {(productos[j].cantidad)*(productos[j].precio)}")
    
print(f"Total a pagar:{total}")
print("---------------------------------------")
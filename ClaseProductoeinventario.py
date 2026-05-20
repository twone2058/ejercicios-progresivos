class Producto:

    def __init__(self, nombre, precio, cantidad):
        self.nombre   = nombre
        self.precio   = precio
        self.cantidad = cantidad

    def valor_total(self):
        # cuanto vale todo el stock de este producto
        return self.precio * self.cantidad

    def __str__(self):
        # se llama automaticamente cuando haces print(objeto)
        return (
            f"[{self.nombre}]"
            f"  precio: ${self.precio:,.0f}"
            f"  stock: {self.cantidad}"
        )


# funciones auxiliares — trabajan con listas de objetos Producto

def mostrar_inventario(lista):
    print("--- Inventario ---")
    for p in lista:
        print(p)  # llama a __str__ de cada producto

def producto_mas_caro(lista):
    # key=lambda indica por que campo comparar al buscar el maximo
    return max(lista, key=lambda p: p.precio)

def valor_inventario(lista):
    # generador: calcula valor_total() de cada uno y los acumula
    return sum(p.valor_total() for p in lista)


# prueba
catalogo = [
    Producto("Auriculares", 120_000, 10),
    Producto("Webcam",      85_000,  7),
    Producto("Mousepad XL", 28_000,  25),
]

mostrar_inventario(catalogo)

mas_caro = producto_mas_caro(catalogo)
print(f"El mas caro es: {mas_caro.nombre}")

total = valor_inventario(catalogo)
print(f"Valor total del inventario: ${total:,.0f}")
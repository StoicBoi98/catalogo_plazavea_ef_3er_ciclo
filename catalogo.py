def mostrar_menu():
    print("\n=== SISTEMA DE CATALOGO - PLAZA VEA ===")
    print("1. Registrar producto")
    print("2. Mostrar catalogo")
    print("3. Salir")

def buscar_codigo(catalogo, codigo_buscado):
    for i in range(len(catalogo)):
        if catalogo[i][0] == codigo_buscado:
            return i
    return -1

def registrar_producto(catalogo):
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = input("Código de producto (ej. PV001): ").strip().replace(" ","").upper()
    
    if buscar_codigo(catalogo, codigo) != -1:
        print(f"Error: el código '{codigo}' ya existe en el catálogo.")
        return
    
    descripcion = input("Descripción: ").strip()
    cantidad = int(input("Cantidad disponible: "))
    precio = float(input("Precio de venta (S/): "))
    
    producto = [codigo, descripcion, cantidad, precio]
    catalogo.append(producto)
    print("Producto registrado correctamente.")

def mostrar_catalogo(catalogo):
    print("\n--- CATALOGO DE PRODUCTOS ---")
    if len(catalogo) == 0:
        print("No hay productos registrados aún.")
        return
    
    for producto in catalogo:
        print(f"Código: {producto[0]} | Descripción: {producto[1]} | Stock: {producto[2]} | Precio: S/ {producto[3]:.2f}")
         
def main():
    catalogo = []
    
    while True:
        mostrar_menu()
        opcion = input("Elija una opción del 1 al 3: ").strip()
       
        if opcion == "1":
            registrar_producto(catalogo)
        elif opcion == "2":
            mostrar_catalogo(catalogo)
        elif opcion == "3":
            print("Saliendo del sistema, espere...")
            break
        else:
            print("Opción inválida. Igrese 1, 2 o 3: ")

main()

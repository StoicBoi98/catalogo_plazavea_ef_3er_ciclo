def mostrar_menu():
    print("\n=== SISTEMA DE CATALOGO - PLAZA VEA ===")
    print("1. Registrar producto")
    print("2. Mostrar catalogo")
    print("3. Buscar producto por código")
    print("4. Actualizar stock y precio")
    print("5. Salir")

def buscar_codigo(catalogo, codigo_buscado):
    for i in range(len(catalogo)):
        if catalogo[i][0] == codigo_buscado:
            return i
    return -1

def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Error: este campo no puede quedar vacío.")
        elif "|" in texto:
            print("Error: no se permite usar el símbolo '|'.")
        else:
            return texto

def leer_cantidad(mensaje):
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor < 0:
                print("Error: la cantidad no puede ser negativa.")
            else:
                return valor
        except ValueError:
            print("Error: ingrese un número entero válido.")

def leer_precio(mensaje):
    while True:
        entrada = input(mensaje).strip()
        try:
             valor = float(entrada)
             if valor <= 0:
                 print("Error: el precio debe ser mayor a 0. No se regala.") 
             else:
                 return valor
        except ValueError:
            print("Error: ingrese un precio númerico válido (ej. 12.50).")
                         
def registrar_producto(catalogo):
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = leer_texto("Código de producto (ej. PV001): ").replace(" ","").upper()
    
    if buscar_codigo(catalogo, codigo) != -1:
        print(f"Error: el código '{codigo}' ya existe en el catálogo.")
        return
    
    descripcion = leer_texto("Descripción: ")
    cantidad = leer_cantidad("Cantidad disponible: ")
    precio = leer_precio("Precio de venta (S/): ")
    
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

def buscar_producto(catalogo):
    print("\n--- BUSCAR PRODUCTO ---")
    if len(catalogo) == 0:
        print("No hay productos registrados aún.")
        return
    
    codigo = leer_texto("Ingrese el código a buscar: ").replace(" ","").upper()
    indice = buscar_codigo(catalogo, codigo)
    
    if indice == -1:
        print(f"No se encontró ningún producto con el código '{codigo}'.")
    else:
        producto = catalogo[indice]
        print(f"Código: {producto[0]} | Descripción: {producto[1]} | Stock: {producto[2]} | Precio: S/ {producto[3]:.2f}")

def actualizar_producto(catalogo):
    print("\n--- ACTUALIZAR STOCK Y PRECIO ---")
    if len(catalogo) == 0:
        print("No hay productos registrados aún.")
        return
    
    codigo = leer_texto("Ingrese el código del producto a actualizar: ").replace(" ","").upper()
    indice = buscar_codigo(catalogo, codigo)
    
    if indice == -1:
        print(f"No se encontró ningún producto con el código '{codigo}'.")
        return
    
    producto = catalogo[indice]
    print(f"Producto actual: {producto[1]} | Stock: {producto[2]} | Precio: S/ {producto[3]:.2f}")
    
    nueva_cantidad = leer_cantidad("Nueva cantidad disponible: ")
    nuevo_precio = leer_precio("Nuevo precio de venta (S/): ")
    
    catalogo[indice][2] = nueva_cantidad
    catalogo[indice][3] = nuevo_precio
    print("Producto actualizado correctamente.")
                   
def main():
    catalogo = []
    
    while True:
        mostrar_menu()
        opcion = input("Elija una opción del 1 al 5: ").strip()
       
        if opcion == "1":
            registrar_producto(catalogo)
        elif opcion == "2":
            mostrar_catalogo(catalogo)
        elif opcion == "3":
            buscar_producto(catalogo)
        elif opcion == "4":
            actualizar_producto(catalogo)
        elif opcion == "5":
            print("Saliendo del sistema, espere...")
            break
        else:
            print("Opción inválida. Igrese 1, 2, 3, 4 o 5: ")

main()

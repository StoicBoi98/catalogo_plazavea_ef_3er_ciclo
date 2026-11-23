def mostrar_menu():
    print("\n=== SISTEMA DE CATALOGO - PLAZA VEA ===")
    print("1. Registrar producto")
    print("2. Mostrar catalogo")
    print("3. Salir")
    
def main():
    catalogo = []
    
    while True:
        mostrar_menu()
        opcion = input("Elija una opción del 1 al 3: ").strip()
       
        if opcion == "1":
            print("Elegiste registrar")
        elif opcion == "2":
            print("Elegiste mostrar")
        elif opcion == "3":
            print("Saliendo del sistema, espere...")
            break
        else:
            print("Opción inválida. Igrese 1, 2 o 3: ")
main()

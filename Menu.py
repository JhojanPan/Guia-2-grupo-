#Aquí va el menú 
from Funciones import suma, resta, multiplicar, dividir

def mostrar_menu():
    while True:
        print("\n--- CALCULADORA ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = suma(a, b)
            print(f"El resultado de la suma es: {resultado}")

        elif opcion == "2":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = resta(a, b)
            print(f"El resultado de la resta es: {resultado}")

        elif opcion == "3":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = multiplicar(a, b)
            print(f"El resultado de la multiplicación es: {resultado}")

        elif opcion == "4":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = dividir(a, b)
            print(f"El resultado de la división es: {resultado}")

        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
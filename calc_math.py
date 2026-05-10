import sys
import traceback

# Configuración
MODO_DEBUG = False

def main():
    print("--- Calculadora de Terminal ---")
    while True:
        try:
            print("\n" + "-"*30)
            num1 = float(input("Ingresa num1: "))
            operacion = input("Ingresa la operacion (+, -, *, /): ")
            num2 = float(input("Ingresa num2: "))

            resultado = 0
            if operacion == '+':
                resultado = num1 + num2
            elif operacion == '-':
                resultado = num1 - num2
            elif operacion == '*':
                resultado = num1 * num2
            elif operacion == '/':
                if num2 == 0:
                    print("\033[91m[ERROR] Operación inválida: No se puede dividir por cero.\033[0m")
                    # Usamos continue para que no se cierre y vuelva a preguntar
                    continue 
                resultado = num1 / num2
            else:
                print("\033[91m[ERROR] Operación no reconocida.\033[0m")
                continue

            # Imprimir resultado en azul
            print(f"\033[94m> El resultado de la operación es: {resultado}\033[0m")

        except Exception as e:
            if MODO_DEBUG:
                print("\033[93m[TRAZA TÉCNICA ACTIVADA]\033[0m")
                traceback.print_exc()
            else:
                print("\033[91m[ERROR] Ocurrió un error inesperado. Revisa los datos ingresados.\033[0m")
        
        # Pregunta de control para reiniciar o salir
        continuar = input("\n¿Deseas realizar otra operación? (s/n): ").strip().lower()
        if continuar != 's':
            print("¡Hasta luego!")
            break # Rompe el bucle y cierra el programa

if __name__ == "__main__":
    main()
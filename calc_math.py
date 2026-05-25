import sys
import traceback
from typing import Union

# Configuración
MODO_DEBUG = False

# Códigos ANSI para colores
COLOR_RESET = "\033[0m"
COLOR_ERROR = "\033[91m"
COLOR_RESULTADO = "\033[94m"
COLOR_DEBUG = "\033[93m"


def calculate(num1: float, operacion: str, num2: float) -> float:
    """
    Realiza una operación matemática entre dos números.
    
    Args:
        num1: Primer número
        operacion: Operación a realizar (+, -, *, /)
        num2: Segundo número
        
    Returns:
        El resultado de la operación
        
    Raises:
        ValueError: Si la operación no es válida o hay división por cero
    """
    operaciones = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else (_ for _ in ()).throw(
            ValueError("No se puede dividir por cero")
        )
    }
    
    if operacion not in operaciones:
        raise ValueError("Operación no reconocida")
    
    return operaciones[operacion](num1, num2)


def obtener_numero(prompt: str) -> float:
    """
    Obtiene un número válido del usuario con validación.
    
    Args:
        prompt: Mensaje a mostrar al usuario
        
    Returns:
        Número flotante ingresado por el usuario
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"{COLOR_ERROR}[ERROR] Por favor ingresa un número válido.{COLOR_RESET}")


def obtener_operacion() -> str:
    """
    Obtiene una operación válida del usuario.
    
    Returns:
        Operación válida (+, -, *, /)
    """
    operaciones_validas = ['+', '-', '*', '/']
    while True:
        operacion = input("Ingresa la operación (+, -, *, /): ").strip()
        if operacion in operaciones_validas:
            return operacion
        print(f"{COLOR_ERROR}[ERROR] Operación no válida. Usa: +, -, *, /{COLOR_RESET}")


def main() -> None:
    """
    Función principal de la calculadora.
    Mantiene un bucle que permite realizar múltiples operaciones.
    """
    print("--- Calculadora de Terminal ---")
    
    while True:
        try:
            print("\n" + "-" * 30)
            num1 = obtener_numero("Ingresa num1: ")
            operacion = obtener_operacion()
            num2 = obtener_numero("Ingresa num2: ")
            
            resultado = calculate(num1, operacion, num2)
            print(f"{COLOR_RESULTADO}> El resultado de la operación es: {resultado}{COLOR_RESET}")
            
        except ValueError as e:
            print(f"{COLOR_ERROR}[ERROR] {e}{COLOR_RESET}")
        except Exception as e:
            if MODO_DEBUG:
                print(f"{COLOR_DEBUG}[TRAZA TÉCNICA ACTIVADA]{COLOR_RESET}")
                traceback.print_exc()
            else:
                print(f"{COLOR_ERROR}[ERROR] Ocurrió un error inesperado.{COLOR_RESET}")
        
        # Pregunta de control para reiniciar o salir
        continuar = input("\n¿Deseas realizar otra operación? (s/n): ").strip().lower()
        if continuar != 's':
            print("¡Hasta luego!")
            break


if __name__ == "__main__":
    main()

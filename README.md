🧮 Calculadora de Terminal
Módulo de código libre para operaciones matemáticas básicas, ideal para tareas de primaria.

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![License](https://img.shields.io/badge/license-GPL%20v3-green) ![Status](https://img.shields.io/badge/status-active-brightgreen) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

📋 Descripción
calc-terminal-python es una calculadora de línea de comandos desarrollada en Python. Permite realizar operaciones aritméticas básicas directamente desde la terminal, mostrando los resultados con formato visual en color.

Licencia: GNU GPL v3
Repositorio: github.com/yospinamurillo/calc-terminal-python
⚙️ Requisitos
Dependencia	Versión mínima	Notas
Pitón	3.8 o superior	No se requieren librerías adicionales
⚠️Si la versión de Python instalada es inferior a 3.8, el programa no funcionará correctamente.

🚀 Instalación y ejecución
1. Clonar el repositorio
git clone https://github.com/yospinamurillo/CalculadoraTerminal.git
cd calc-terminal-python
2. Ejecutar la aplicación
python calc_math.py
🖥️ Uso
El programa solicita los datos de entrada en el siguiente orden:

num1— Primer número (admite decimales)
operacion— Operador a utilizar: +, -, *,/
num2— Segundo número (admite decimales)
Ejemplo de uso
Ingrese num1: 10
Ingrese operacion: *
Ingrese num2: 5
Salida esperada (en color azul) :

> El resultado de la operación es: 50.0
🛡️ Manejo de errores
El sistema incluye validación de errores para evitar errores inesperados:

Caso	Mensaje mostrado
División por cero	[ERROR] Operación inválida: No se puede dividir por cero
El programa no se interrumpirá ante estos errores; muestra el mensaje y continúa en ejecución.

🔧 Configuración avanzada
Dentro del archivo calc_math.pyexiste una variable de configuración interna:

Variable	Valor por defecto	Descripción
MODO_DEBUG	False	Si se cambia a True, muestra la traza técnica completa de los errores en consola
Activar modo debug
# En calc_math.py, cambiar la siguiente línea:
MODO_DEBUG = True
💡 Útil para diagnóstico y desarrollo. Se recomienda mantener en Falseproducción.

📁 Estructura del proyecto
calc-terminal-python/
└── calc_math.py    # Archivo principal — contiene toda la lógica de la calculadora

📋 Documentación de Módulos
El software se compone de los siguientes componentes principales:

- **calc_math.py**: Módulo principal que implementa la lógica de la calculadora. Incluye funciones para realizar operaciones aritméticas básicas (suma, resta, multiplicación, división), validación de entradas, manejo de errores y configuración de modo debug. Utiliza el módulo estándar de Python para entrada/salida y formateo de colores en terminal.

🧪 Tests
Para asegurar la calidad del código, se incluyen pruebas unitarias que verifican el correcto funcionamiento de las operaciones matemáticas y el manejo de errores.

Ejecutar tests:
python -m unittest discover

Pruebas realizadas:
- **Operaciones básicas**: Verifica que las funciones de suma, resta, multiplicación y división devuelvan resultados correctos para números enteros y decimales. Resultados esperados: valores numéricos precisos sin errores de redondeo.
- **Manejo de errores**: Prueba casos como división por cero, entradas no numéricas y operadores inválidos. Resultados esperados: mensajes de error específicos sin interrupción del programa.
- **Modo debug**: Confirma que al activar MODO_DEBUG, se muestre la traza completa de excepciones. Resultados esperados: salida detallada en consola para debugging.

📄 Licencia
Este proyecto se distribuye bajo la licencia GNU General Public License v3.0 .
Consulte el archivo LICENSEpara más detalles o visite gnu.org/licenses/gpl-3.0 .


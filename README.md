# 🧮 Calculadora de Terminal

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Version](https://img.shields.io/badge/Version-1.0.0-informational)

Módulo de código libre para operaciones matemáticas básicas, ideal para tareas de primaria.

## 👥 Integrantes

- **Juan Carlos Arteaga**
- **Karol Marquez Rodriguez**
- ** Yesit Ospina Murillo**
- **Nicol Alejandra Correa Vasco**

## 📋 Descripción

`calc-terminal-python` es una calculadora de línea de comandos desarrollada en Python. Permite realizar operaciones aritméticas básicas directamente desde la terminal, mostrando los resultados [...]

**Licencia:** GNU GPL v3  
**Repositorio:** github.com/yospinamurillo/calc-terminal-python

## ⚙️ Requisitos

| Dependencia | Versión mínima | Notas |
|---|---|---|
| Python | 3.8 o superior | No se requieren librerías adicionales |

⚠️ **Nota:** Si la versión de Python instalada es inferior a 3.8, el programa no funcionará correctamente.

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/yospinamurillo/CalculadoraTerminal.git
cd CalculadoraTerminal
```

### 2. Ejecutar la aplicación

```bash
python calc_math.py
```

## 🖥️ Uso

El programa solicita los datos de entrada en el siguiente orden:

- **num1** — Primer número (admite decimales)
- **operacion** — Operador a utilizar: `+`, `-`, `*`, `/`
- **num2** — Segundo número (admite decimales)

### Ejemplo de uso

```
Ingrese num1: 10
Ingrese operacion: *
Ingrese num2: 5
```

**Salida esperada (en color azul):**
```
> El resultado de la operación es: 50.0
```

## 🛡️ Manejo de errores

El sistema incluye validación de errores para evitar errores inesperados:

| Caso | Mensaje mostrado |
|---|---|
| División por cero | `[ERROR] Operación inválida: No se puede dividir por cero` |
| Entrada no numérica | `[ERROR] Entrada inválida: El valor debe ser un número` |
| Operador inválido | `[ERROR] Operador no reconocido` |

El programa no se interrumpirá ante estos errores; muestra el mensaje y continúa en ejecución.

## 🔧 Configuración avanzada

Dentro del archivo `calc_math.py` existe una variable de configuración interna:

| Variable | Valor por defecto | Descripción |
|---|---|---|
| `MODO_DEBUG` | `False` | Si se cambia a `True`, muestra la traza técnica completa de los errores en consola |

### Activar modo debug

```python
# En calc_math.py, cambiar la siguiente línea:
MODO_DEBUG = True
```

💡 **Útil para diagnóstico y desarrollo.** Se recomienda mantener en `False` en producción.

## 📁 Estructura del proyecto

```
CalculadoraTerminal/
├── calc_math.py          # Archivo principal — contiene toda la lógica
├── tests/                # Pruebas unitarias
├── docs/
│   ├── diagrams/         # Diagramas PlantUML (NUEVO)
│   └── README_DIAGRAMAS.md  # Documentación de diagramas (NUEVO)
└── README.md             # Este archivo
```

## 📋 Documentación de Módulos

El software se compone de los siguientes componentes principales:

**calc_math.py:** Módulo principal que implementa la lógica de la calculadora. Incluye funciones para realizar operaciones aritméticas básicas (suma, resta, multiplicación, división) y vali[...]

## 📊 Diagramas de Arquitectura (NUEVO)

Consulta la documentación completa de diagramas en `docs/README_DIAGRAMAS.md`

### Otras vistas disponibles:

- **Arquitectura General** - Componentes y sus interacciones
- **Estructura de Componentes** - Clases, métodos y atributos
- **Casos de Uso** - Perspectiva del usuario

Estos diagramas se renderizan automáticamente en GitHub. Para visualizarlos:

1. Abre cualquier archivo `.puml` en el directorio `docs/diagrams/`
2. O consulta `docs/README_DIAGRAMAS.md` para más opciones de visualización

## 🧪 Tests

Para asegurar la calidad del código, se incluyen pruebas unitarias que verifican el correcto funcionamiento de las operaciones matemáticas y el manejo de errores.

### Ejecutar tests:

```bash
python -m unittest discover
```

### Pruebas realizadas:

- **Operaciones básicas:** Verifica que las funciones de suma, resta, multiplicación y división devuelvan resultados correctos para números enteros y decimales.
- **Manejo de errores:** Prueba casos como división por cero, entradas no numéricas y operadores inválidos.
- **Modo debug:** Confirma que al activar `MODO_DEBUG`, se muestre la traza completa de excepciones.

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **GNU General Public License v3.0**. Consulte el archivo `LICENSE` para más detalles o visite [gnu.org/licenses/gpl-3.0](https://www.gnu.org/licenses[...]

## ✨ Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request.

## 📞 Contacto

Para preguntas o sugerencias, abre un issue en el repositorio.

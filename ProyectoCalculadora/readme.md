# 🧮 Calculadora de Terminal

> Módulo de código libre para operaciones matemáticas básicas, ideal para tareas de primaria.

---

## 📋 Descripción

**calc-terminal-python** es una calculadora de línea de comandos desarrollada en Python. Permite realizar operaciones aritméticas básicas directamente desde la terminal, mostrando los resultados con formato visual en color.

- **Licencia:** GNU GPL v3
- **Repositorio:** [github.com/xxxxx/calc-terminal-python](https://github.com/xxxxx/calc-terminal-python.git)

---

## ⚙️ Requisitos

| Dependencia | Versión mínima | Notas |
|-------------|----------------|-------|
| Python      | 3.8 o superior | No se requieren librerías adicionales |

> ⚠️ Si la versión de Python instalada es inferior a 3.8, el programa no funcionará correctamente.

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/xxxxx/calc-terminal-python.git
cd calc-terminal-python
```

### 2. Ejecutar la aplicación

```bash
python calc_math.py
```

---

## 🖥️ Uso

El programa solicita los datos de entrada en el siguiente orden:

1. **`num1`** — Primer número (admite decimales)
2. **`operacion`** — Operador a utilizar: `+`, `-`, `*`, `/`
3. **`num2`** — Segundo número (admite decimales)

### Ejemplo de uso

```
Ingrese num1: 10
Ingrese operacion: *
Ingrese num2: 5
```

**Salida esperada** *(en color azul)*:

```
> El resultado de la operación es: 50.0
```

---

## 🛡️ Manejo de errores

El sistema incluye validación de errores para evitar fallos inesperados:

| Caso | Mensaje mostrado |
|------|-----------------|
| División por cero | `[ERROR] Operación inválida: No se puede dividir por cero` |

El programa **no se interrumpe** ante estos errores; muestra el mensaje y continúa en ejecución.

---

## 🔧 Configuración avanzada

Dentro del archivo `calc_math.py` existe una variable de configuración interna:

| Variable | Valor por defecto | Descripción |
|----------|-------------------|-------------|
| `MODO_DEBUG` | `False` | Si se cambia a `True`, muestra la traza técnica completa de los errores en consola |

### Activar modo debug

```python
# En calc_math.py, cambiar la siguiente línea:
MODO_DEBUG = True
```

> 💡 Útil para diagnóstico y desarrollo. Se recomienda mantener en `False` en producción.

---

## 📁 Estructura del proyecto

```
calc-terminal-python/
└── calc_math.py    # Archivo principal — contiene toda la lógica de la calculadora
```

---

## 📄 Licencia

Este proyecto está distribuido bajo la licencia **GNU General Public License v3.0**.  
Consulta el archivo `LICENSE` para más detalles o visita [gnu.org/licenses/gpl-3.0](https://www.gnu.org/licenses/gpl-3.0.html).

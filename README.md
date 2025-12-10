# 🚕 Taxímetro en Python

Este proyecto es un simulador de taxímetro desarrollado en Python. La aplicación, controlada por la línea de comandos, no solo calcula la tarifa de un viaje en tiempo real, sino que también incluye un sistema de **logs**, **tests unitarios**, un **historial de trayectos** y **tarifas configurables**. El programa guía al usuario desde el inicio, permite gestionar múltiples trayectos y guarda un registro persistente de cada viaje.


---

## 🛠️ Entorno de Desarrollo y Tecnologías

Este proyecto se ha desarrollado con el siguiente conjunto de herramientas y tecnologías.

*   **Lenguaje**: [**Python 3.13.5**](https://www.python.org/ )
*   **Gestor de Entorno**: [**Anaconda**](https://www.anaconda.com/ ) fue utilizado para gestionar las dependencias y el entorno virtual.
*   **Editor de Código**: El desarrollo se realizó en [**Visual Studio Code**](https://code.visualstudio.com/ ).
*   **Librerías Principales**:
    *   `time`: Para la gestión del tiempo y el cálculo de las tarifas.
    *   `logging`: Usado para rastrear los eventos que ocurren cuando se ejecuta el programa.
    *   `datetime`: El módulo datetime proporciona clases para manipular fechas y horas.
    *   `pytest`: Usado para la escritura de pruebas pequeñas y legibles, aunque puede permitir pruebas funcionales complejas para aplicaciones y bibliotecas.

---

## ⚙️ Instalación y Funcionamiento

Sigue estos pasos para poner en marcha el proyecto en tu máquina local.

### 1. Clona el Repositorio

```bash
git clone https://github.com/Bootcamp-IA-P6/Proyecto1_Jonathan_Brasales.git
cd C:\Users\under\Documents\F5\projects\taximetro\main.py
```

### 2. Configura el Entorno Virtual

Tienes dos opciones para instalar las dependencias. Elige la que prefieras.

#### Opción A: Usando conda (Recomendado)

Este método utiliza el archivo **environment.yml** para recrear el entorno de desarrollo exacto.

```bash
# Crea el entorno a partir del archivo
conda env create -f environment.yml

# Activa el nuevo entorno
conda activate vTaxi
```
#### Opción B: Usando pip y venv

Este es el método estándar de Python si no usas Anaconda.

```bash
# Crea un entorno virtual
python -m venv venv

# Actívalo
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instala las dependencias
pip install -r requirements.txt
```

### 3. ¡Ejecuta el Programa! ▶️

Una vez que el entorno esté activado y las dependencias instaladas, puedes iniciar el taxímetro con el siguiente comando:
```python
python main.py
```

## ✨ Características Principales

*   **Cálculo de Tarifas Dinámico**: Calcula automáticamente la tarifa diferenciando entre el tiempo en movimiento y el tiempo en parada.
*   **Tarifas Configurables**: Permite ajustar los precios por segundo para adaptarse a diferentes condiciones o tarifas.
*   **Gestión de Múltiples Trayectos**: Inicia un nuevo viaje inmediatamente después de finalizar uno, sin necesidad de reiniciar el programa.
*   **Historial de Viajes**: Guarda un registro detallado de todos los trayectos finalizados en un archivo de texto.
*   **Sistema de Logs**: Incorpora un sistema de logging para facilitar la depuración y la trazabilidad de las operaciones.
*   **Tests Unitarios**: Incluye una suite de pruebas para garantizar la precisión de los cálculos y el correcto funcionamiento del sistema.
*   **Interfaz de Comandos Clara**: Guía al usuario con instrucciones claras sobre cómo operar el taxímetro.

---

## 🚀 Guía de Uso

Una vez que el programa está en ejecución, te dará la bienvenida y mostrará los comandos disponibles. El flujo de operación es el siguiente:

1.  **Iniciar un Viaje (`start`)**: Comienza un nuevo trayecto. El taxímetro empezará a contar el tiempo en estado "parado".
2.  **Poner en Movimiento (`move`)**: Cambia al estado "en movimiento" para aplicar la tarifa correspondiente.
3.  **Detener el Taxi (`stop`)**: Vuelve al estado "parado". Puedes alternar entre `move` y `stop` tantas veces como sea necesario.
4.  **Finalizar el Viaje (`finish`)**: Termina el trayecto, calcula la tarifa total y la muestra en pantalla. El viaje se guardará en el historial.
5.  **Salir del Programa (`exit`)**: Cierra la aplicación.

---
## 🐛 Bugs Conocidos y Posibles Mejoras

### Bugs Conocidos
*   Actualmente, no hay bugs conocidos. ¡Si encuentras alguno, no dudes en reportarlo!

### Posibles Mejoras
*   **Interfaz Gráfica de Usuario (GUI)**: Desarrollar una interfaz visual (usando `Tkinter` , `PyQt` o `Streamlit`) para que el uso del taxímetro sea más intuitivo.
*   **Exportar Recibos Individuales**: Añadir una función para guardar el resumen de un viaje específico en un archivo PDF o de texto como si fuera un recibo.

---
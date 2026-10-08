Calculadora de Resistencias
Una aplicación de escritorio moderna e interactiva desarrollada en Python con Tkinter para la identificación y cálculo de valores de resistencias, tanto para código de colores como para componentes de montaje superficial (SMD).

🚀 Características
Cálculo por Bandas de Colores:

Soporte para resistencias de 4, 5 y 6 bandas.
Visualización gráfica dinámica interactiva que dibuja la resistencia y sus colores en tiempo real.
Cálculo del valor de resistencia (
Ω
,
K
Ω
,
M
Ω
), tolerancia () y coeficiente térmico (
ppm/
∘
C
).
Interfaz gráfica responsiva y redimensionable.
Cálculo de Código SMD:

Decodificación de códigos de 3 dígitos (ej. 472 
→
4.7
 K
Ω
).
Decodificación de códigos de 4 dígitos (ej. 4702 
→
47
 K
Ω
).
Soporte para el estándar EIA-96 (ej. 01C 
→
10
 K
Ω
).
Interpretación de notación con letra R (ej. 4R7 
→
4.7
Ω
).
🛠️ Requisitos e Instalación
Requisitos previos
Este proyecto utiliza únicamente librerías estándar de Python, por lo que no se requiere la instalación de módulos externos a través de pip.

Únicamente necesitas tener instalado Python 3.x y el módulo gráfico Tkinter.

Nota para usuarios de Linux (Ubuntu/Debian):
En algunos sistemas Linux, Tkinter no viene preinstalado con Python. Puedes instalarlo con:

sudo apt-get install python3-tk
📂 Estructura del Repositorio
.
├── resistenciasfinal.py   # Código fuente principal de la aplicación
├── requirements.txt       # Archivo de especificación de dependencias
└── README.md              # Documentación del proyecto
💻 Ejecución
Para iniciar la aplicación, ejecuta en tu terminal:

python resistenciasfinal.py
O bien, en sistemas donde se diferencien las versiones de Python:

python3 resistenciasfinal.py
📄 Licencia
Este proyecto está bajo la Licencia MIT. Siéntete libre de modificarlo y distribuirlo.

## 🚀 Cómo ejecutar en Windows

### Requisitos previos
1. Tener instalado **Python 3** (descárgalo desde [python.org](https://www.python.org/)). 
   > ⚠️ **Importante:** Durante la instalación, marca la casilla que dice **"Add Python to PATH"** (Agregar Python al PATH).
2. Tkinter viene incluido por defecto con la instalación oficial de Python en Windows, por lo que no requiere descargas adicionales.

### Pasos de ejecución

1. Abre la terminal de Windows (**Símbolo del sistema / CMD** o **PowerShell**).
2. Navega hasta la carpeta donde descargaste o clonaste el proyecto:
   ```cmd
   cd ruta\a\la\carpeta\calculadora-resistencias
   Ejecuta el programa con el siguiente comando:
python resistenciasfinal.py
(Si el comando python no funciona, prueba con py resistenciasfinal.py).

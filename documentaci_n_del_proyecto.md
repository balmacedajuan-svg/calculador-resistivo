# Calculadora de Resistencias

Una aplicación de escritorio moderna e interactiva desarrollada en Python con **Tkinter** para la identificación y cálculo de valores de resistencias, tanto para código de colores como para componentes de montaje superficial (**SMD**).

---

## 🚀 Características

- **Cálculo por Bandas de Colores:**
  - Soporte para resistencias de **4, 5 y 6 bandas**.
  - Visualización gráfica dinámica interactiva que dibuja la resistencia y sus colores en tiempo real.
  - Cálculo del valor de resistencia ($\Omega, K\Omega, M\Omega$), tolerancia ($\%$) y coeficiente térmico ($\text{ppm/}^\circ\text{C}$).
  - Interfaz gráfica responsiva y redimensionable.

- **Cálculo de Código SMD:**
  - Decodificación de códigos de **3 dígitos** (ej. `472` $\rightarrow 4.7\text{ K}\Omega$).
  - Decodificación de códigos de **4 dígitos** (ej. `4702` $\rightarrow 47\text{ K}\Omega$).
  - Soporte para el estándar **EIA-96** (ej. `01C` $\rightarrow 10\text{ K}\Omega$).
  - Interpretación de notación con letra **R** (ej. `4R7` $\rightarrow 4.7\Omega$).

---

## 🛠️ Requisitos e Instalación

### Requisitos previos

Este proyecto utiliza únicamente librerías estándar de Python, por lo que **no se requiere la instalación de módulos externos a través de `pip`**. 

Únicamente necesitas tener instalado **Python 3.x** y el módulo gráfico **Tkinter**.

> **Nota para usuarios de Linux (Ubuntu/Debian):**  
> En algunos sistemas Linux, Tkinter no viene preinstalado con Python. Puedes instalarlo con:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## 📂 Estructura del Repositorio

```text
.
├── resistenciasfinal.py   # Código fuente principal de la aplicación
├── requirements.txt       # Archivo de especificación de dependencias
└── README.md              # Documentación del proyecto
```

---

## 💻 Ejecución

Para iniciar la aplicación, ejecuta en tu terminal:

```bash
python resistenciasfinal.py
```

O bien, en sistemas donde se diferencien las versiones de Python:

```bash
python3 resistenciasfinal.py
```

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Siéntete libre de modificarlo y distribuirlo.
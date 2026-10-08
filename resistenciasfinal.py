#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox
import math

# ============================================
# DATOS DE RESISTENCIAS
# ============================================

COLORES = {
    'negro': 0, 'marrón': 1, 'rojo': 2, 'naranja': 3, 'amarillo': 4,
    'verde': 5, 'azul': 6, 'violeta': 7, 'gris': 8, 'blanco': 9
}

MULTIPLICADOR = {
    'negro': 1, 'marrón': 10, 'rojo': 100, 'naranja': 1000, 'amarillo': 10000,
    'verde': 100000, 'azul': 1000000, 'violeta': 10000000, 'gris': 100000000,
    'blanco': 1000000000, 'dorado': 0.1, 'plateado': 0.01
}

TOLERANCIAS = {
    'marrón': 1, 'rojo': 2, 'verde': 0.5, 'azul': 0.25, 'violeta': 0.1,
    'gris': 0.05, 'dorado': 5, 'plateado': 10, 'ninguno': 20
}

TERMICO = {
    'marrón': 100, 'rojo': 50, 'naranja': 15, 'amarillo': 25, 'azul': 10,
    'violeta': 5, 'negro': 250
}

EIA96_BASE = {
    '01': 100, '02': 102, '03': 105, '04': 107, '05': 110, '06': 113,
    '07': 115, '08': 118, '09': 121, '10': 124, '11': 127, '12': 130,
    '13': 133, '14': 137, '15': 140, '16': 143, '17': 147, '18': 150,
    '19': 154, '20': 158, '21': 162, '22': 165, '23': 169, '24': 174,
    '25': 178, '26': 182, '27': 187, '28': 191, '29': 196, '30': 200,
    '31': 205, '32': 210, '33': 215, '34': 221, '35': 226, '36': 232,
    '37': 237, '38': 243, '39': 249, '40': 255, '41': 261, '42': 267,
    '43': 274, '44': 280, '45': 287, '46': 294, '47': 301, '48': 309,
    '49': 316, '50': 324, '51': 332, '52': 340, '53': 348, '54': 357,
    '55': 365, '56': 374, '57': 383, '58': 392, '59': 402, '60': 412,
    '61': 422, '62': 432, '63': 442, '64': 453, '65': 464, '66': 475,
    '67': 487, '68': 499, '69': 511, '70': 523, '71': 536, '72': 549,
    '73': 562, '74': 576, '75': 590, '76': 604, '77': 619, '78': 634,
    '79': 649, '80': 665, '81': 681, '82': 698, '83': 715, '84': 732,
    '85': 750, '86': 768, '87': 787, '88': 806, '89': 825, '90': 845,
    '91': 866, '92': 887, '93': 909, '94': 931, '95': 953, '96': 976
}

EIA96_MULT = {
    'Z': 0.001, 'Y': 0.01, 'X': 0.1, 'A': 1, 'B': 10, 'C': 100,
    'D': 1000, 'E': 10000, 'F': 100000, 'G': 1000000, 'H': 10000000
}

COLOR_RGB = {
    'negro': '#1a1a1a',
    'marrón': '#8B4513',
    'rojo': '#CC0000',
    'naranja': '#FF8C00',
    'amarillo': '#FFD700',
    'verde': '#006600',
    'azul': '#0033CC',
    'violeta': '#8B00FF',
    'gris': '#888888',
    'blanco': '#F0F0F0',
    'dorado': '#DAA520',
    'plateado': '#C0C0C0',
    'ninguno': '#F0F0F0'
}

# ============================================
# FUNCIONES DE CÁLCULO
# ============================================

def formatear_valor(ohmios):
    if ohmios >= 1_000_000:
        return f"{ohmios/1_000_000:.3f} MΩ"
    elif ohmios >= 1000:
        return f"{ohmios/1000:.2f} KΩ"
    else:
        return f"{ohmios:.2f} Ω"

def calcular_bandas(colores):
    n = len(colores)
    
    if n == 4:
        dig1 = COLORES.get(colores[0])
        dig2 = COLORES.get(colores[1])
        mult = MULTIPLICADOR.get(colores[2], 1)
        tol = TOLERANCIAS.get(colores[3], 20)
        valor = (dig1 * 10 + dig2) * mult
        return valor, tol, None
    
    elif n == 5:
        dig1 = COLORES.get(colores[0])
        dig2 = COLORES.get(colores[1])
        dig3 = COLORES.get(colores[2])
        mult = MULTIPLICADOR.get(colores[3], 1)
        tol = TOLERANCIAS.get(colores[4], 20)
        valor = (dig1 * 100 + dig2 * 10 + dig3) * mult
        return valor, tol, None
    
    elif n == 6:
        dig1 = COLORES.get(colores[0])
        dig2 = COLORES.get(colores[1])
        dig3 = COLORES.get(colores[2])
        mult = MULTIPLICADOR.get(colores[3], 1)
        tol = TOLERANCIAS.get(colores[4], 20)
        term = TERMICO.get(colores[5], None)
        valor = (dig1 * 100 + dig2 * 10 + dig3) * mult
        return valor, tol, term
    
    else:
        return None, None, None

def calcular_smd(codigo):
    codigo = codigo.upper().strip()
    
    if len(codigo) == 3 and codigo[0].isdigit() and codigo[1].isdigit() and codigo[2].isalpha():
        base = EIA96_BASE.get(codigo[:2])
        mult = EIA96_MULT.get(codigo[2])
        if base is not None and mult is not None:
            valor = base * mult
            return valor, "EIA-96"
    
    if len(codigo) == 3 and codigo.isdigit():
        dig1 = int(codigo[0])
        dig2 = int(codigo[1])
        mult = int(codigo[2])
        valor = (dig1 * 10 + dig2) * (10 ** mult)
        return valor, "3 dígitos"
    
    if len(codigo) == 4 and codigo.isdigit():
        dig1 = int(codigo[0])
        dig2 = int(codigo[1])
        dig3 = int(codigo[2])
        mult = int(codigo[3])
        valor = (dig1 * 100 + dig2 * 10 + dig3) * (10 ** mult)
        return valor, "4 dígitos"
    
    if 'R' in codigo:
        if codigo.startswith('R'):
            valor = float('0.' + codigo[1:])
        else:
            partes = codigo.split('R')
            if len(partes) == 2:
                valor = float(partes[0] + '.' + partes[1])
        return valor, "con R"
    
    return None, None

# ============================================
# DIBUJO DE RESISTENCIA MEJORADO (CORREGIDO)
# ============================================

class DibujoResistencia:
    def __init__(self, canvas, width=500, height=200):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.colores_bandas = ['negro'] * 6
        self.num_bandas = 4
        
    def dibujar(self):
        self.canvas.delete('all')
        
        w = self.width
        h = self.height
        
        # ===== TERMINALES (ALAMBRES) =====
        # Terminal izquierdo
        self.canvas.create_line(10, h//2, 50, h//2, width=3, fill='#A0A0A0', capstyle='round')
        self.canvas.create_oval(6, h//2 - 5, 16, h//2 + 5, fill='#B0B0B0', outline='#888')
        
        # Terminal derecho
        self.canvas.create_line(w - 50, h//2, w - 10, h//2, width=3, fill='#A0A0A0', capstyle='round')
        self.canvas.create_oval(w - 16, h//2 - 5, w - 6, h//2 + 5, fill='#B0B0B0', outline='#888')
        
        # ===== CUERPO DE LA RESISTENCIA (CILÍNDRICO) =====
        x1, y1 = 50, h//2 - 45
        x2, y2 = w - 50, h//2 + 45
        
        # Sombra inferior (efecto 3D) - CORREGIDO: color sólido
        self.canvas.create_rectangle(x1, y1 + 3, x2, y2 + 3, 
                                    fill='#CCCCCC', outline='')
        
        # Gradiente de luz (efecto cilíndrico) - CORREGIDO
        pasos = 15
        for i in range(pasos):
            t = i / pasos
            # Simular luz desde arriba
            brillo = int(200 - 60 * abs(t - 0.5) * 2)  # Más brillo en el centro
            color = f'#{brillo:02x}{brillo-20:02x}{brillo-40:02x}'
            
            y_actual = y1 + i * (y2 - y1) // pasos
            y_siguiente = y1 + (i + 1) * (y2 - y1) // pasos
            self.canvas.create_rectangle(x1, y_actual, x2, y_siguiente, 
                                        fill=color, outline='')
        
        # Borde del cuerpo
        self.canvas.create_rectangle(x1, y1, x2, y2, outline='#8B7355', width=1.5)
        
        # ===== BANDAS DE COLOR =====
        self._dibujar_bandas(x1, y1, x2, y2)
        
        # ===== ETIQUETAS =====
        self.canvas.create_text(w//2, 28, text=f"Resistencia de {self.num_bandas} bandas", 
                               font=('Arial', 11, 'bold'), fill='#333')
        
        # Indicadores decorativos
        self.canvas.create_text(25, h//2 - 20, text="◄", font=('Arial', 14), fill='#999')
        self.canvas.create_text(w - 25, h//2 - 20, text="►", font=('Arial', 14), fill='#999')
    
    def _dibujar_bandas(self, x1, y1, x2, y2):
        if self.num_bandas == 0:
            return
        
        # Espacio disponible para bandas
        margen = 35
        ancho_cuerpo = x2 - x1 - 2 * margen
        ancho_banda = min(ancho_cuerpo / (self.num_bandas * 1.3), 35)
        separacion = ancho_cuerpo / (self.num_bandas + 1)
        inicio = x1 + margen + separacion
        
        for i in range(self.num_bandas):
            if i < len(self.colores_bandas):
                color = self.colores_bandas[i]
                color_hex = COLOR_RGB.get(color, '#CCCCCC')
                
                bx1 = inicio + i * separacion - ancho_banda/2
                bx2 = inicio + i * separacion + ancho_banda/2
                
                # Si es última banda y hay 4+, es tolerancia (más angosta)
                if i == self.num_bandas - 1 and self.num_bandas >= 4:
                    bx1 = inicio + i * separacion - ancho_banda/2.8
                    bx2 = inicio + i * separacion + ancho_banda/2.8
                
                # Banda principal
                self.canvas.create_rectangle(bx1, y1 + 3, bx2, y2 - 3, 
                                           fill=color_hex, outline=color_hex, width=1)
                
                # Sombra de la banda (efecto 3D) - CORREGIDO
                self.canvas.create_rectangle(bx1 + 1, y1 + 5, bx2 - 1, y1 + 8, 
                                           fill='#666666', outline='')
                
                # Etiqueta del color debajo
                self.canvas.create_text((bx1 + bx2)//2, y2 + 18, 
                                       text=color, font=('Arial', 8), fill='#555')
    
    def actualizar_bandas(self, colores):
        self.colores_bandas = colores
        self.num_bandas = len(colores)
        self.dibujar()

# ============================================
# INTERFAZ PRINCIPAL (REDIMENSIONABLE)
# ============================================

class AppResistencias:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Resistencias - Versión Definitiva")
        self.root.geometry("780x720")
        self.root.minsize(700, 650)
        self.root.resizable(True, True)
        
        # Configurar grid
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        self.notebook = ttk.Notebook(root)
        self.notebook.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        
        self.tab_bandas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_bandas, text="🎨 Bandas de colores")
        self.crear_tab_bandas()
        
        self.tab_smd = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_smd, text="🔢 SMD")
        self.crear_tab_smd()
        
        # Vincular evento de redimension
        self.root.bind('<Configure>', self.on_resize)
    
    def on_resize(self, event):
        """Redibuja el gráfico cuando se redimensiona la ventana"""
        if hasattr(self, 'canvas') and self.canvas:
            ancho = self.canvas.winfo_width()
            alto = self.canvas.winfo_height()
            if ancho > 100 and alto > 100:
                self.dibujo.width = ancho
                self.dibujo.height = alto
                self.dibujo.dibujar()
    
    # ========== PESTAÑA BANDAS ==========
    def crear_tab_bandas(self):
        frame = self.tab_bandas
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        
        # ===== GRÁFICO =====
        canvas_frame = ttk.Frame(frame)
        canvas_frame.grid(row=0, column=0, sticky='ew', pady=8, padx=10)
        canvas_frame.grid_columnconfigure(0, weight=1)
        
        self.canvas = tk.Canvas(canvas_frame, height=230, bg='#FAFAFA', 
                                highlightthickness=1, highlightbackground='#ccc')
        self.canvas.grid(row=0, column=0, sticky='ew')
        
        self.dibujo = DibujoResistencia(self.canvas, 550, 200)
        self.dibujo.dibujar()
        
        # ===== SELECTOR =====
        top_frame = ttk.Frame(frame)
        top_frame.grid(row=1, column=0, pady=5)
        
        ttk.Label(top_frame, text="Número de bandas:", font=('Arial', 10)).pack(side='left', padx=5)
        self.num_bandas = tk.StringVar(value="4")
        combo = ttk.Combobox(top_frame, textvariable=self.num_bandas, values=["4", "5", "6"], 
                            state="readonly", width=5)
        combo.pack(side='left', padx=5)
        combo.bind('<<ComboboxSelected>>', self.actualizar_bandas)
        
        # ===== COMBOS =====
        self.frame_colores = ttk.Frame(frame)
        self.frame_colores.grid(row=2, column=0, pady=10)
        
        self.lista_colores = list(COLORES.keys()) + ['dorado', 'plateado', 'ninguno']
        self.combos_colores = []
        
        self.crear_combos(4)
        
        # ===== BOTÓN =====
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=3, column=0, pady=8)
        ttk.Button(btn_frame, text="Calcular Resistencia", command=self.calcular_bandas, 
                  width=30).pack()
        
        # ===== RESULTADO =====
        result_frame = ttk.LabelFrame(frame, text="📊 Resultado", padding=10)
        result_frame.grid(row=4, column=0, sticky='ew', padx=20, pady=8)
        
        self.resultado_bandas = tk.StringVar(value="")
        ttk.Label(result_frame, textvariable=self.resultado_bandas, 
                 font=('Arial', 14, 'bold'), foreground='#0066CC').pack(pady=5)
        
        self.detalle_bandas = tk.StringVar(value="")
        ttk.Label(result_frame, textvariable=self.detalle_bandas, 
                 font=('Arial', 10), foreground='#666').pack(pady=2)
    
    def crear_combos(self, n):
        # Limpiar
        for widget in self.frame_colores.winfo_children():
            widget.destroy()
        self.combos_colores = []
        
        # Crear combos en 2 columnas
        for i in range(n):
            row = i // 2
            col = (i % 2) * 2
            
            ttk.Label(self.frame_colores, text=f"Banda {i+1}:", font=('Arial', 10)).grid(
                row=row, column=col, padx=8, pady=6, sticky='e')
            
            combo = ttk.Combobox(self.frame_colores, values=self.lista_colores, 
                                 state="readonly", width=14, font=('Arial', 10))
            combo.grid(row=row, column=col+1, padx=8, pady=6, sticky='w')
            combo.set('negro')
            combo.bind('<<ComboboxSelected>>', lambda e: self.actualizar_grafico())
            self.combos_colores.append(combo)
        
        ttk.Label(self.frame_colores, text="").grid(row=(n//2)+1, column=0, pady=5)
        self.actualizar_grafico()
    
    def actualizar_bandas(self, event=None):
        n = int(self.num_bandas.get())
        self.crear_combos(n)
        self.resultado_bandas.set("")
        self.detalle_bandas.set("")
    
    def actualizar_grafico(self):
        colores = [combo.get() for combo in self.combos_colores]
        self.dibujo.actualizar_bandas(colores)
    
    def calcular_bandas(self):
        if not self.combos_colores:
            return
            
        colores = [combo.get() for combo in self.combos_colores]
        
        for c in colores:
            if c not in self.lista_colores:
                messagebox.showerror("Error", f"Color '{c}' no válido")
                return
        
        valor, tolerancia, termico = calcular_bandas(colores)
        
        if valor is None:
            messagebox.showerror("Error", "No se pudo calcular. Verifica los colores.")
            return
        
        texto = f"Valor: {formatear_valor(valor)}"
        if tolerancia is not None:
            texto += f" ±{tolerancia}%"
        if termico is not None:
            texto += f" | Coef. térmico: {termico} ppm/°C"
        
        self.resultado_bandas.set(texto)
        
        detalle = " | ".join([f"{i+1}: {c}" for i, c in enumerate(colores)])
        self.detalle_bandas.set(f"Bandas: {detalle}")
    
    # ========== PESTAÑA SMD ==========
    def crear_tab_smd(self):
        frame = self.tab_smd
        frame.grid_columnconfigure(0, weight=1)
        
        input_frame = ttk.Frame(frame)
        input_frame.grid(row=0, column=0, pady=30)
        
        ttk.Label(input_frame, text="Código SMD:", font=('Arial', 12)).pack(side='left', padx=10)
        self.entry_smd = ttk.Entry(input_frame, width=20, font=('Arial', 14))
        self.entry_smd.pack(side='left', padx=10)
        self.entry_smd.focus()
        
        ttk.Button(input_frame, text="Calcular", command=self.calcular_smd, width=15).pack(side='left', padx=10)
        
        ejemplos_frame = ttk.LabelFrame(frame, text="📚 Ejemplos de códigos SMD", padding=10)
        ejemplos_frame.grid(row=1, column=0, pady=10, padx=20, sticky='ew')
        
        ejemplos = [
            "• 3 dígitos: 472 = 4.7KΩ",
            "• 4 dígitos: 4702 = 47KΩ",
            "• EIA-96: 01C = 10KΩ, 88A = 806Ω",
            "• Con R: 4R7 = 4.7Ω, R100 = 0.1Ω"
        ]
        
        for ej in ejemplos:
            ttk.Label(ejemplos_frame, text=ej, font=('Arial', 10)).pack(anchor='w', pady=2)
        
        result_frame = ttk.LabelFrame(frame, text="📊 Resultado", padding=10)
        result_frame.grid(row=2, column=0, pady=20, padx=20, sticky='ew')
        
        self.resultado_smd = tk.StringVar(value="")
        ttk.Label(result_frame, textvariable=self.resultado_smd, 
                 font=('Arial', 16, 'bold'), foreground='#006600').pack(pady=5)
        
        self.tipo_smd = tk.StringVar(value="")
        ttk.Label(result_frame, textvariable=self.tipo_smd, 
                 font=('Arial', 11), foreground='#666').pack(pady=2)
        
        self.entry_smd.bind('<Return>', lambda e: self.calcular_smd())
    
    def calcular_smd(self):
        codigo = self.entry_smd.get().strip()
        if not codigo:
            messagebox.showwarning("Atención", "Ingresa un código SMD")
            return
        
        valor, tipo = calcular_smd(codigo)
        
        if valor is None:
            self.resultado_smd.set("❌ Código no válido")
            self.tipo_smd.set("")
            return
        
        self.resultado_smd.set(f"{formatear_valor(valor)}")
        self.tipo_smd.set(f"Tipo: {tipo} | Código: {codigo}")

# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    root = tk.Tk()
    app = AppResistencias(root)
    root.mainloop()
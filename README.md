# 🧮 Biblioteca de Métodos Numéricos

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Tkinter](https://img.shields.io/badge/UI-Tkinter%2FTTK-orange.svg)

Una aplicación de escritorio desarrollada en **Python** con interfaz gráfica (**Tkinter / TTK**) para resolver problemas matemáticos mediante **Métodos Numéricos**. La herramienta permite visualizar procedimientos, analizar iteraciones y calcular resultados precisos para diversas áreas del análisis numérico.

---

## 📋 Tabla de Contenidos
- [Características](#-características)
- [Métodos Incluidos](#-métodos-incluidos)

---

## ✨ Características

- 🖥️ **Interfaz Gráfica Intuitiva:** Desarrollada con Tkinter/TTK bajo una arquitectura orientada a objetos.
- 📊 **Tablas de Iteraciones:** Visualización clara de los pasos y convergencia usando `ttk.Treeview`.
- ⚠️ **Manejo de Errores:** Validación de entradas, división por cero y detección de no convergencia mediante cuadros de diálogo emergentes.
- 📌 **Soporte Dinámico:** Introducción interactiva de funciones matemáticas y parámetros iniciales (tolerancia, máximo de iteraciones, intervalos).

---

## 🔬 Métodos Incluidos

El proyecto abarca las siguientes áreas principales del análisis numérico:

* **Programa punto flotante:** Realiza la coversion entre valores decimales a binarios segun la IEEPS (8,16 y 64 bits) o viceversa.

### 1. Solución de Ecuaciones No Lineales
* **Método de Bisección:** Búsqueda en intervalos cerrados por partición binaria.
* **Método de Regula Falsi (Falsa Posición):** Interpolación lineal en intervalos cerrados.
* **Método de Punto Fijo:** Método de iteración funcional de una sola variable ($x = g(x)$).
* **Método de Newton-Raphson:** Aproximación abierta mediante derivadas.
* **Método de la Secante:** Aproximación por diferencias finitas sin requerir derivada explícita.
* **Método de Steffensen:** Aceleración de la convergencia del método de punto fijo sin usar derivadas secundarias.
* **Método de Müller:** Extensión del método de la secante que utiliza interpolación cuadrática para encontrar raíces reales y complejas.
* **Aceleración Delta-Square de Aitken:** Técnica para acelerar la velocidad de convergencia de secuencias de iteración lineal.

### 2. Algoritmos y Deflación de Polinomios
* **Método de Horner:** Evaluación eficiente de polinomios y sus derivadas, utilizado también para la división sintética.
* **Deflación Polinomial:** Reducción del grado de un polinomio tras encontrar una de sus raíces.
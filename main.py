import time
import math
import random
from datetime import datetime
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# Frases motivacionales por signo
# -----------------------------
frases_por_signo = {
    "Aries": "La energía que tienes rompe cualquier límite.",
    "Taurus": "Tu constancia construye futuros sólidos.",
    "Gemini": "Tu curiosidad te lleva por caminos fascinantes.",
    "Cancer": "Tu sensibilidad es tu mayor fuerza.",
    "Leo": "Naciste para brillar, no lo olvides.",
    "Virgo": "El orden que traes al mundo es vital.",
    "Libra": "Tu equilibrio inspira a otros.",
    "Scorpio": "Tu intensidad transforma realidades.",
    "Sagittarius": "Tu espíritu libre ilumina nuevos caminos.",
    "Capricorn": "Tu disciplina logra lo imposible.",
    "Aquarius": "Tu originalidad cambia el mundo.",
    "Pisces": "Sueñas con fuerza y eso te hace imparable."
}

# -----------------------------
# Funciones auxiliares de fecha y astrología básica
# -----------------------------
def validar_fecha(anio, mes, dia):
    try:
        datetime(anio, mes, dia)
        return True
    except ValueError:
        return False

def calcular_signo_solar(dt):
    mes, dia = dt.month, dt.day
    signos = [
        ("Capricorn", 20), ("Aquarius", 19), ("Pisces", 20), ("Aries", 20),
        ("Taurus", 21), ("Gemini", 21), ("Cancer", 23), ("Leo", 23),
        ("Virgo", 23), ("Libra", 23), ("Scorpio", 23), ("Sagittarius", 22), ("Capricorn", 31)
    ]
    return signos[mes - 1][0] if dia < signos[mes - 1][1] else signos[mes][0]

def calcular_ascendente(dt, lat, lon):
    return random.choice(list(frases_por_signo.keys()))  # Simulación aleatoria

# -----------------------------
# Funciones de esperanza de vida
# -----------------------------
def calcular_esperanza_vida(sexo):
    sexo = sexo.lower()
    if sexo.startswith("h"):
        return 75
    elif sexo.startswith("m"):
        return 81
    return 78

def contar_vida_restante(anios):
    for i in range(anios, -1, -1):
        print(f"[Te quedan: {i} años...]")
        time.sleep(0.3)
    print("[Disfruta cada instante]")

# -----------------------------
# Gráficos usando matplotlib
# -----------------------------
def mostrar_grafico_barras(edad_actual, esperanza_total):
    edades = list(range(0, 101, 5))
    barras = [max(esperanza_total - edad, 0) for edad in edades]

    colores = ['#1f77b4' if edad != (edad_actual // 5) * 5 else '#ff7f0e' for edad in edades]

    plt.figure(figsize=(10, 5))
    plt.bar(edades, barras, width=4, color=colores)
    plt.xlabel("Edad")
    plt.ylabel("Vida restante estimada")
    plt.title("Gráfico de Barras: Esperanza de Vida")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def mostrar_grafico_pastel(edad, restante):
    total = edad + restante
    porciones = [edad, restante]
    etiquetas = ['Años vividos', 'Esperanza restante']
    colores = ['#66c2a5', '#fc8d62']

    plt.figure(figsize=(6, 6))
    plt.pie(porciones, labels=etiquetas, autopct='%1.1f%%', colors=colores, startangle=90)
    plt.title("Gráfico de Pastel: Porcentaje de Vida")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

# -----------------------------
# GUI sencilla con Tkinter
# -----------------------------
def ejecutar_gui():
    def calcular():
        try:
            dia = int(entry_dia.get())
            mes = int(entry_mes.get())
            anio = int(entry_anio.get())
            sexo = combo_sexo.get()

            if not validar_fecha(anio, mes, dia):
                messagebox.showerror("Error", "Fecha inválida")
                return

            edad = datetime.now().year - anio
            esperanza = calcular_esperanza_vida(sexo)
            restante = max(esperanza - edad, 0)

            dt = datetime(anio, mes, dia, 12, 0)
            signo = calcular_signo_solar(dt)
            ascendente = calcular_ascendente(dt, 4.6097, -74.0817)
            frase = frases_por_signo.get(signo, "Tu signo es único y especial.")

            resultado.set(
                f"Edad: {edad}\nSigno Solar: {signo}\nAscendente: {ascendente}\n"
                f"Esperanza de vida: {esperanza} años\nRestante: {restante} años\n"
                f"Frase: {frase}"
            )

            mostrar_grafico_barras(edad, esperanza)
            mostrar_grafico_pastel(edad, restante)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("Astrología y Vida")

    tk.Label(root, text="Día de nacimiento:").grid(row=0, column=0)
    entry_dia = tk.Entry(root)
    entry_dia.grid(row=0, column=1)

    tk.Label(root, text="Mes de nacimiento:").grid(row=1, column=0)
    entry_mes = tk.Entry(root)
    entry_mes.grid(row=1, column=1)

    tk.Label(root, text="Año de nacimiento:").grid(row=2, column=0)
    entry_anio = tk.Entry(root)
    entry_anio.grid(row=2, column=1)

    tk.Label(root, text="Sexo:").grid(row=3, column=0)
    combo_sexo = ttk.Combobox(root, values=["Hombre", "Mujer"])
    combo_sexo.grid(row=3, column=1)

    resultado = tk.StringVar()
    tk.Label(root, textvariable=resultado, justify="left").grid(row=5, column=0, columnspan=2, pady=10)

    tk.Button(root, text="Calcular", command=calcular).grid(row=4, column=0, columnspan=2, pady=5)

    root.mainloop()

# -----------------------------
# Menú principal
# -----------------------------
def ejecutar_aplicacion():
    print("¡Bienvenido al Sistema de Astrología y Esperanza de Vida!")
    while True:
        print("\n===============================================")
        print("  SISTEMA INTEGRADO DE ASTROLOGÍA Y VIDA")
        print("===============================================")
        print("1. GUI con Tkinter")
        print("2. Salir")
        print("===============================================")
        opcion = input("Elige una opción (1-2): ")

        if opcion == "1":
            ejecutar_gui()
        elif opcion == "2":
            print("¡Gracias por usar el sistema! Que tengas un buen día.")
            break
        else:
            print("Opción no válida. Elige entre 1 y 2.")

        input("\nPresiona Enter para continuar...")

# -----------------------------
# Punto de entrada del programa
# -----------------------------
if __name__ == "__main__":
    ejecutar_aplicacion()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

def click(boton):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + boton)

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        messagebox.showerror("Error", "Expresion invalida")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")
ventana.resizable(False, False)

entrada = tk.Entry(ventana, font=("Arial", 20), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

fila = 1
col = 0
for boton in botones:
    if boton == '=':
        btn = tk.Button(ventana, text=boton, width=5, height=2, command=calcular)
    else:
        btn = tk.Button(ventana, text=boton, width=5, height=2,
                        command=lambda b=boton: click(b))
    btn.grid(row=fila, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        fila += 1

btn_limpiar = tk.Button(ventana, text="C", width=5, height=2, command=limpiar)
btn_limpiar.grid(row=fila, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

btn_salir = tk.Button(ventana, text="Salir", width=5, height=2, command=ventana.quit)
btn_salir.grid(row=fila, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

ventana.mainloop()

""" Día 84: GUI usando Tkinter
Cree una aplicación de calculadora con una GUI usando Tkinter. """

import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Simple")

        self.expression = ""

        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(root, text=button, width=4, height=2, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Expresión inválida")
                self.entry.delete(0, tk.END)
                self.expression = ""
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

# Ejemplo de uso:
# Ejecuta el script y usa la GUI para realizar cálculos.
# Resultado esperado:
# Una ventana de calculadora que permite realizar operaciones básicas.
# El objetivo de esta actividad es introducir clases, métodos y funciones, 
# así como algunas de las consideraciones a tener en cuenta a la hora de
# decidir qué incluir en las clases.
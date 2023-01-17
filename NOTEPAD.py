from cgitb import text
from tkinter import LEFT, Tk
from tkinter.filedialog import *
import tkinter as tk

canvas: Tk = tk.Tk()
canvas.geometry("400x600")
canvas.title("NotePad")
canvas.config(bg="white")
top = tk.Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = 'nw')

b1 = tk.Button(canvas, text="0pen", bg = "white")
b1.pack(in_ = top, side = LEFT)

b2 = tk.Button(canvas, text="Save", bg = "white")
b2.pack(in_ = top, side = LEFT)

b3 = tk.Button(canvas, text="Clear", bg = "white")
b3.pack(in_ = top, side = LEFT)

b4 = tk.Button(canvas, text="Exit", bg = "white")
b4.pack(in_ = top, side = LEFT)

entry = tk.Text(canvas, bg ="#F9DDA4", font = ("poppins", 15))
entry.pack(padx = 10, pady = 5)

canvas.mainloop()

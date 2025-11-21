import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("700x500")
root.resizable(False,False)
root.title("Hi")

def on_button_click():
    print("I got clicked!")





label = tk.Label(root, text = "Hi")
label.pack(pady = 20)

button = tk.Button(root, text = "hi", command=on_button_click)
button.pack(pady=20)

framey1 = Frame(root, bg = "#5080B2", height = 200, width = 1000)
framey1.pack(pady = 20)


root.mainloop()


import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("300x300")
root.resizable(False,False)
root.title("Hi")

times_clicked = 0

def on_button_click():
    global times_clicked
    times_clicked += 1
    print("I got clicked!")
    print(times_clicked)
    if times_clicked ==10:
        print("Youre so cool")



label = tk.Label(root, text = "Hi")
label.pack(pady = 20)

button = tk.Button(root, text = "hi", command=on_button_click)
button.pack(pady=20)

# if times_clicked > 10:
    # print("You got a super click")

root.mainloop()

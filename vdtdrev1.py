import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)

def on_button_click():
    print("print")

def run_command():
    # Just a dummy example: echo input in text_output
    user_input = entry.get()
    if user_input.strip():
        text_output.insert(tk.END, f"> {user_input}\n")  # Show input as if typed in console
        entry.delete(0, tk.END)  # Clear input field
    else:
        text_output.insert(tk.END, "Please enter something.\n")

root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("400x500")
root.configure(bg="#3B9A9D")


label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

time_label = tk.Label(root, text="--:--:--", font=("Helvetica", 24))
time_label.pack(pady=20)

button_print = tk.Button(root, text="Print to Console", command=on_button_click)
button_print.pack(pady=10)

# Entry widget for command-line style input
entry = tk.Entry(root, width=50,bg = "red")
entry.pack(pady=5)
entry.focus()  # Focus on startup

# Bind Enter key to submit input
entry.bind('<Return>', lambda event: run_command())

# Button to submit input
button_run = tk.Button(root, text="Submit Input", command=run_command)
button_run.pack(pady=5)

# Text widget to show output
text_output = tk.Text(root, height=15, width=50)
text_output.pack(pady=10)

update_time()
root.mainloop()

import tkinter as tk
from datetime import datetime


button_click_counter = 0

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)

def on_button_click():
    print("print")

def on_2button_click():
    global button_click_counter
    button_click_counter += 1
    good_tk_def()



def run_command():
    # Just a dummy example: echo input in text_output
    user_input = entry.get()
    if user_input.strip():
        text_output.insert(tk.END, f"> {user_input}\n")  # Show input as if typed in console
        entry.delete(0, tk.END)  # Clear input field
    else:
        text_output.insert(tk.END, "Please enter something.\n")

def good_tk_def():
    if button_click_counter > 1000:
        print("Why are you still doing this? :sob: ")
    elif button_click_counter > 100:
        print("Wow thats a bit of dedication for a 74 line python program.. ")
    elif button_click_counter > 5:
        print("youve clicked five times.. how.. inspiring")


root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("1000x700")
root.configure(bg="#285385")


label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

time_label = tk.Label(root, text="--:--:--", font=("Helvetica", 24))
time_label.pack(pady=20)

button = tk.Button(root, text="Mini-Game", command=on_2button_click)
button.pack(pady=5)

button_print = tk.Button(root, text="Print to Console", command=on_button_click)
button_print.pack(pady=10)



# Entry widget for command-line style input
entry = tk.Entry(root, width=50,bg = "#0A3A70")
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
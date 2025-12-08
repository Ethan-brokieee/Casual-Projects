import tkinter as tk

def collect_pollen():
    global pollen, magnet_owned

    if magnet_owned == 1:
        pollen += 2
    elif magnet_owned == 0:
        pollen += 1
    print("You collected one pollen")
    print("Pollen:", pollen)

def upgrade_dipper():
    global pollen, magnet_owned
    if pollen >= 100:
        pollen -= 100
        magnet_owned += 1
        print("Upgrade bought!")
        print("Magnets:", magnet_owned)
        print("Pollen left:", pollen)
    else:
        print("Not enough pollen!")

magnet_owned = 0
pollen = 0
honey = 0
material = 0

root = tk.Tk()
root.geometry("300x300")
root.title("BSS makeshift game")
root.maxsize(200, 200)
root.minsize(100, 100)

tk.Button(root, text="Collect Pollen", command=collect_pollen).pack()
tk.Button(root, text="Upgrade Dipper (100 pollen)", command=upgrade_dipper).pack()

root.mainloop()

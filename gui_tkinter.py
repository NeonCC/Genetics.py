import tkinter as tk

def holi(event):
    father, mother = fatheri.get(), motheri.get()
    print(father, "\n", mother)

def deletef(event):
    if len(fatheri.get()) == 61:
        fatheri.delete(0, "end")
        fatheri.insert(0, '')
        fatheri.config(fg="black")

def putf(event):
    if fatheri.get() == '':
        fatheri.insert(0, "Introduce el genotipo del padre, por ejemplo AaBbCcDdEeFfGg: ")
        fatheri.config(fg="grey")

def deletem(event):
    if len(motheri.get()) == 63:
        motheri.delete(0, "end")
        motheri.insert(0, '')
        motheri.config(fg="black")

def putm(event):
    if motheri.get() == '':
        motheri.insert(0, "Introduce el genotipo de la madre, por ejemplo AaBbCcDdEeFfGg: ")
        motheri.config(fg="grey")

root = tk.Tk()
root.configure(background="dim gray")

fatheri = tk.Entry(root, width=70)
motheri = tk.Entry(root, width=70)

fatheri.grid(row=0, column=0, padx=10, pady=10, ipady=5, sticky="N S E W")
motheri.grid(row=1, column=0, padx=10, pady=10, ipady=5, sticky="N S E W")

fatheri.insert(0, "Introduce el genotipo del padre, por ejemplo AaBbCcDdEeFfGg: ")
motheri.insert(0, "Introduce el genotipo de la madre, por ejemplo AaBbCcDdEeFfGg: ")

calcular = tk.Button(root, text="Calcular", bg="light slate grey")
calcular.bind("<Button>", holi)
calcular.grid(row=2)

fatheri.config(fg="gray")
motheri.config(fg="gray")

fatheri.bind("<FocusIn>", deletef)
fatheri.bind("<FocusOut>", putf)
motheri.bind("<FocusIn>", deletem)
motheri.bind("<FocusOut>", putm)

root.mainloop()
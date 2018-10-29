# coding=utf-8
import time
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font
from tkinter.messagebox import *
import sys
from os import path

class Genetics():
    def __init__(self):
        self.genes_number = 0
        self.father_combinations = []
        self.mother_combinations = []
        self.punnett = []
        self.father = ''
        self.mother = ''

    def validate(self):
        if self.father == "autor" or self.father == "author" or self.father == "autoría" or self.father == "autoria" or self.mother == "autor" or self.mother == "author" or self.mother == "autoría" or self.mother == "autoria":
            message = "Realizado por Benjamín Antonio Velasco Guzmán"
            showinfo(title="Autoría", message=message)
            return False
        if len(self.father) % 2 != 0:
            showwarning(title="Error",
                        message="Debes proporcionar un número de alelos pares. Por característica pueden haber 2 alelos: dominante (A) y recesivo (a).")
            return False
        if self.father == "Introduce el genotipo del padre, por ejemplo AaBbCcDdEeFfGg" or self.mother == "Introduce el genotipo de la madre, por ejemplo AaBbCcDdEeFfGg":
            message = "Debes escribir un genotipo, por ejemplo AaBb"
            showwarning(title="Error", message=message)
            return False
        if len(self.father) == 0 or len(self.mother) == 0:
            showwarning(title="Error", message="Ingresa el genotipo del padre y el genotipo de la madre")
            return False
        if len(self.father) < 4 or len(self.mother) < 4:
            showwarning(title="Error",
                        message="Ejemplos de genotipos: AaBb hasta AaBbCcDdEeFfGg (no tienen que ser esos)")
            return False
        if len(self.father) != len(self.mother):
            message = "El número de caracteres de " + self.father + " debe ser igual al de " + self.mother
            showerror(title="Error", message=message)
            return False
        elif (len(self.father) or len(self.mother)) > 14:
            message = "Ups!! No podemos calcular más allá de 7 características"
            showwarning(title="Error", message=message)
            return False
        return True

    def make_combinations(self, x, y):
        self.genes_number = len(x) // 2
        for i in range(2):
            self.father_combinations.append(x[i] + x[2])
            self.father_combinations.append(x[i] + x[3])
            self.mother_combinations.append(y[i] + y[2])
            self.mother_combinations.append(y[i] + y[3])

        # TODO: optimizar esto
        # creo que es lo mas optimizado posible, ya que si los genes son 7, los if anteriores si sirven
        if self.genes_number >= 3:
            for i in range(4):  # 0 a 4 que son los que actualmente están en self.father_combinations
                for a in range(4, 6):  # de 4 a 6, que son los 2 últimos caracteres de self.father
                    self.father_combinations.append(self.father_combinations[i] + x[a])
                    self.mother_combinations.append(self.mother_combinations[i] + y[a])
            self.father_combinations[:4], self.mother_combinations[:4] = [], []
        if self.genes_number >= 4:
            for i in range(8):  # en 4 empieza la primera combinación del de arriba ya acaba en 11 3->ab 4->ABC
                for j in range(6, 8):
                    self.father_combinations.append(self.father_combinations[i] + x[j])
                    self.mother_combinations.append(self.mother_combinations[i] + y[j])
            self.father_combinations[:8], self.mother_combinations[:8] = [], []
        if self.genes_number >= 5:
            for i in range(16):
                for j in range(8, 10):
                    self.father_combinations.append(self.father_combinations[i] + x[j])
                    self.mother_combinations.append(self.mother_combinations[i] + y[j])
            self.father_combinations[:16], self.mother_combinations[:16] = [], []
        if self.genes_number >= 6:
            for i in range(32):
                for j in range(10, 12):
                    self.father_combinations.append(self.father_combinations[i] + x[j])
                    self.mother_combinations.append(self.mother_combinations[i] + y[j])
            self.father_combinations[:32], self.mother_combinations[:32] = [], []
        if self.genes_number >= 7:
            for i in range(64):
                for j in range(12, 14):
                    self.father_combinations.append(self.father_combinations[i] + x[j])
                    self.mother_combinations.append(self.mother_combinations[i] + y[j])
            self.father_combinations[:64], self.mother_combinations[:64] = [], []

    def doEverything(self, father, mother):
        self.father = father
        self.mother = mother
        if (self.validate()):
            self.make_combinations(father, mother)
            all_combinations = self.power()
            self.gui(all_combinations)

    def power(self):
        for i in range(2**self.genes_number):
            j = 0
            while j < 2**self.genes_number:
                combination = self.mother_combinations[i]+self.father_combinations[j]
                genes = list(combination)
                genes.sort(key=lambda x: (x.upper(), x[0].islower())) # http://stackoverflow.com/questions/13954841/python-sort-upper-case-and-lower-case
                self.punnett.append(''.join(genes))
                genes[:len(self.father)] = []
                j += 1
        all_combinations, k = [], 0
        for i in range(len(self.punnett)):
            if i == len(self.father_combinations)*k:
                all_combinations.append(self.mother_combinations[k])
                k += 1
            all_combinations.append(self.punnett[i])
        print("\033[1mTodas las combinaciones: \033[0m", all_combinations)
        return all_combinations

    def gui(self, all_combinations):
        resultados = tk.Toplevel() # Tk().withdraw() esconderá root
        try:
            img = ImageTk.PhotoImage(Image.open(path.abspath("./ico/eye.ico")))
            resultados.tk.call('wm', 'iconphoto', resultados._w, img)
        except:
            print("No se ha encontrado './ico/eye.ico'")
            input()
        resultados.resizable(False, False)
        ftabla, fbutton = font.Font(family="Open Sans", size=12), font.Font(family="Dubai Light", size=12)
        frame = tk.Frame(resultados) # tal vez cursor="tcross"
        resultados.title(self.father+" con "+self.mother)
        columna, contadorcomb = 0, 0
        for i in range(len(self.father_combinations)):
            tk.Label(frame, text=self.father_combinations[i], font=ftabla).grid(row=0, column=i+1)
        for i in range(len(all_combinations)):
            if i == (len(self.father_combinations)+1)*contadorcomb:
                tk.Label(frame, text=all_combinations[i], font=ftabla).grid(row=contadorcomb+1, column=0)
                contadorcomb+=1
                columna = 0
            else:
                columna+=1
                tk.Label(frame, text=all_combinations[i], font=ftabla, relief="groove").grid(row=contadorcomb, column=columna)
        def enter_hover_genotipo(event):
            genotipo.config(bg=resultados.cget("background"), fg="black")
        def leave_hover_genotipo(event):
            genotipo.config(bg="#939393", fg="#f4f4f4")
        def enter_hover_search(event):
            busc.config(bg=resultados.cget("background"), fg="black")
        def leave_hover_search(event):
            busc.config(bg="#939393", fg="#f4f4f4")
        menu = tk.Frame(resultados)
        menu.pack(fill=tk.X)
        genotipo = tk.Button(menu, font=fbutton, text="Calcular genotipos", command=self.do_hardy_weinberg)
        genotipo.config(bg="#939393", fg="#f4f4f4", bd=0)
        genotipo.pack(padx=10, side="left")
        busc = tk.Button(menu, font=fbutton, text="Buscar determinado genotipo", command=self.search)
        busc.config(bg="#939393", fg="#f4f4f4", bd=0)
        busc.pack(padx=10, side="right")
        genotipo.bind("<Enter>", enter_hover_genotipo)
        genotipo.bind("<Leave>", leave_hover_genotipo)
        busc.bind("<Enter>", enter_hover_search)
        busc.bind("<Leave>", leave_hover_search)
        frame.pack()
        resultados.mainloop()

    def search(self):
        fuente = font.Font(family="Century Gothic", size=15)
        search = tk.Toplevel()
        try:
            img = ImageTk.PhotoImage(Image.open(path.abspath("./ico/search.ico")))
            search.tk.call('wm', 'iconphoto', search._w, img)
        except:
            print("No se encontró './ico/search.ico'")
            input()
        arriba = tk.Frame(search)
        arriba.pack(pady=10)
        search.maxsize(500, 100)
        search.minsize(450, 90)
        search_label = tk.Label(arriba, text="Elemento a buscar: ", font=fuente)
        search_entry = tk.Entry(arriba, font=fuente)
        arriba.grid_columnconfigure(index=0, weight=1)
        search_label.grid(row=0, column=0, sticky="NWSE")
        search_entry.grid(row=0, column=1, sticky="NWSE")
        search_entry.focus()
        def guardar(event):
            search_value = search_entry.get()
            self.displayResults(search_value)
        boton = tk.Button(search, text="Buscar", font=fuente)
        boton.bind("<Return>", guardar)
        boton.bind("<Button>", guardar)
        boton.pack(ipadx=2, ipady=1, pady=5)
        search.mainloop()

    def displayResults(self, search):
        count = 0
        for i in range(len(self.punnett)):
            if search == self.punnett[i]: count+=1
        if count == 0:
            mensaje = "No se ha encontrado la combinación "+search
            showinfo(title="Lo sentimos", message=mensaje)
        elif count == 1:
            tit = str(count)+" vez"
            mensaje = "Se ha encontrado "+search+" "+tit+"."
            showinfo(title="Encontrado", message=mensaje)
        else:
            tit = str(count)+" veces"
            mensaje = "Se han encontrado "+search+" "+tit+"."
            showinfo(title=tit, message=mensaje)

    def do_hardy_weinberg(self): # Hardy–Weinberg
        dominant, recessive, hybrid = [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]
        for i in range(len(self.father_combinations)):
            for k in range(len(self.mother_combinations)):
                for j in range(len(self.father_combinations[1])):
                    if self.father_combinations[i][j] == self.father_combinations[i][j].upper() and self.mother_combinations[k][j] == self.mother_combinations[k][j].upper():
                        dominant[j] += 1
                    elif self.father_combinations[i][j] != self.father_combinations[i][j].upper() and self.mother_combinations[k][j] != self.mother_combinations[k][j].upper():
                        recessive[j] += 1
        punnett_length = len(self.punnett)
        for i in range(7):
            dominant[i] = dominant[i] * 100 // punnett_length
            recessive[i] = recessive[i] * 100 // punnett_length
            hybrid[i] = 100 - recessive[i] - dominant[i]
        Hardy = tk.Toplevel()
        Hardy.resizable(False, False)
        fuente = font.Font(family="Century Gothic", size=20)
        img = ImageTk.PhotoImage(Image.open(path.abspath("./ico/genetics.ico")))
        Hardy.tk.call('wm', 'iconphoto', Hardy._w, img)
        for i in range(len(self.father)):
            if i % 2 == 0:
                dominant_percentage, hybrid_percentage, recessive_perventage = str(dominant[i//2])+"%", str(hybrid[i//2])+"%", str(recessive[i//2])+"%"
                dominant_label, hybrid_label, recessive_label = tk.Label(Hardy, text=dominant_percentage, font=fuente), tk.Label(Hardy, text=hybrid_percentage, font=fuente), tk.Label(Hardy, text=recessive_perventage, font=fuente)
                dominant_label.grid(row=i, column=0, ipady=10, ipadx=20)
                hybrid_label.grid(row=i, column=1, ipady=10, ipadx=20)
                recessive_label.grid(row=i, column=2, ipady=10, ipadx=20)
            else:
                dominant_letter, hybrid_letter, recessive_letter = self.father[i].upper()*2, self.father[i].upper()+self.father[i].lower(), self.father[i].lower()*2
                dominant_label, hybrid_label, recessive_label = tk.Label(Hardy, text=dominant_letter, font=fuente), tk.Label(Hardy, text=hybrid_letter, font=fuente), tk.Label(Hardy, text=recessive_letter, font=fuente)
                dominant_label.grid(row=i, column=0, ipady=10, ipadx=20)
                hybrid_label.grid(row=i, column=1, ipady=10, ipadx=20)
                recessive_label.grid(row=i, column=2, ipady=10, ipadx=20)

#Ventana principal
def main():
    def enviar(event):
        genetics = Genetics()
        father, mother = fatheri.get(), motheri.get()
        genetics.doEverything(father, mother)
    def deletef(event): #active father
        if len(fatheri.get()) == 59:
            fatheri.delete(0, "end")
            fatheri.insert(0, '')
            fatheri.config(fg="black")
    def putf(event): #no active father
        if fatheri.get() == '':
            fatheri.insert(0, "Introduce el genotipo del padre, por ejemplo AaBbCcDdEeFfGg")
            fatheri.config(fg="grey")
    def deletem(event): #active mother
        if len(motheri.get()) == 61:
            motheri.delete(0, "end")
            motheri.insert(0, '')
            motheri.config(fg="black")
    def putm(event): #no active mother
        if motheri.get() == '':
            motheri.insert(0, "Introduce el genotipo de la madre, por ejemplo AaBbCcDdEeFfGg")
            motheri.config(fg="grey")
    def css(event): #hover button
        calcular.configure(bg="dim gray", fg="white", borderwidth=1) #https://stackoverflow.com/questions/39416021/border-for-tkinter-label
    def css0(event): #no hover button
        calcular.configure(bg="snow4", borderwidth=0)
    root = tk.Tk()
    root.configure(background="dim gray")
    root.geometry("920x500+200+100")
    root.title("Genética")
    consolas = tk.font.Font(family="Consolas", size=30, weight="bold")
    genetics = tk.Label(root, text="Genética", bg="dim gray", fg="white", font=consolas)
    genetics.grid(row=0, pady=15)
    try:
        img = ImageTk.PhotoImage(Image.open(path.abspath("./img/genetics_resized.jpg")))
    except:
        print("No se ha encontrado la imagen './img/genetics_resized.jpg'")
        sys.exit(0)
    tk.Label(root, image=img).grid(row=1)
    root.genetics_image = img
    inputs = font.Font(family="Arial", size=20)
    fatheri = tk.Entry(root, font=inputs)
    motheri = tk.Entry(root, font=inputs)
    fatheri.grid(row=2, padx=50, pady=10, ipady=5, sticky="NWSE")
    motheri.grid(row=3, padx=50, pady=10, ipady=5, sticky="NWSE") #ponerlo al norte este sur y oeste (pa' que funcione columnconfigure)
    fatheri.insert(0, "Introduce el genotipo del padre, por ejemplo AaBbCcDdEeFfGg")
    motheri.insert(0, "Introduce el genotipo de la madre, por ejemplo AaBbCcDdEeFfGg")
    botton = font.Font(family="Century Gothic", size=20)
    calcular = tk.Button(root, text="Calcular", bg="snow4", fg="white", bd=0, font=botton, anchor="center", relief="solid")
    calcular.bind("<Enter>", css)
    calcular.bind("<Leave>", css0)
    calcular.bind("<Button>", enviar)
    calcular.bind("<Return>", enviar)
    calcular.grid(row=4, ipadx=0, ipady=0)
    root.grid_columnconfigure(index=0, weight=1) #http://effbot.org/tkinterbook/grid.htm
    fatheri.config(fg="grey")
    motheri.config(fg="grey")
    fatheri.bind("<FocusIn>", deletef)
    fatheri.bind("<FocusOut>", putf)
    motheri.bind("<FocusIn>", deletem)
    motheri.bind("<FocusOut>", putm)
    try:
        img = ImageTk.PhotoImage(Image.open(path.abspath("./ico/genetics.ico")))
        root.tk.call('wm', 'iconphoto', root._w, img)
    except:
        print("No se encontró './ico/genetics.ico'")
        sys.exit(0)
    root.mainloop()

if __name__ == '__main__':
    main()
# coding=utf-8
import sys, ctypes
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QGridLayout
from PyQt5.QtGui import QIcon, QFont
import time
import tkinter as tk
from tkinter import font
from tkinter.messagebox import *
def check(father, mother):
    if father == "autor" or father == "author" or father == "autoría" or father == "autoria" or mother == "autor" or mother=="author" or mother=="autoría" or mother=="autoria":
        message="Realizado por Benjamín Antonio Velasco Guzmán"
        showinfo(title="Autoría", message=message)
        return 0
    if len(father) % 2 != 0:
        showwarning(title="Error", message="Debes proporcionar un número de alelos pares. Por característica pueden haber 2 alelos: dominante (A) y recesivo (a).")
        return 0
    if father == "Introduce el genotipo del padre, por ejemplo AaBbCcDdEeFfGg" or mother ==  "Introduce el genotipo de la madre, por ejemplo AaBbCcDdEeFfGg":
        message="Debes escribir un genotipo, por ejemplo AaBb"
        showwarning(title="Error", message=message)
        return 0
    if len(father) == 0 or len(mother) == 0:
        showwarning(title="Error", message="Ingresa el genotipo del padre y el genotipo de la madre")
        return 0
    if len(father) < 4 or len(mother) < 4:
        showwarning(title="Error", message="Ejemplos de genotipos: AaBb hasta AaBbCcDdEeFfGg (no tienen que ser esos)")
        return 0
    if len(father) != len(mother):
        message = "El número de caracteres de "+father+" debe ser igual al de "+mother
        showerror(title="Error", message=message)
        return 0
    elif (len(father) or len(mother)) > 14:
        message="Ups!! No podemos calcular más allá de 7 características"
        showwarning(title="Error", message=message)
        return 0
    combinaciones(father, mother)
def combinaciones(x, y):
    global genes, combf, combm
    genes = len(x)//2
    combf = []
    combm = []
    for i in range(2):
        combf.append(x[i]+x[2])
        combf.append(x[i]+x[3])
        combm.append(y[i]+y[2])
        combm.append(y[i]+y[3])
    if genes >= 3:
        for i in range(4): # 0 a 4 que son los que actualmente están en combf
            for a in range(4, 6): # de 4 a 6, que son los 2 últimos caracteres de father
                combf.append(combf[i]+x[a])
                combm.append(combm[i]+y[a])
        combf[:4], combm[:4] = [], []
    if genes >= 4:
        for i in range(8): # en 4 empieza la primera combinación del de arriba ya acaba en 11 3->ab 4->ABC
            for j in range(6, 8):
                combf.append(combf[i]+x[j])
                combm.append(combm[i]+y[j])
        combf[:8], combm[:8] = [], []
    if genes >= 5:
        for i in range(16):
            for j in range(8, 10):
                combf.append(combf[i]+x[j])
                combm.append(combm[i]+y[j])
        combf[:16], combm[:16] = [], []
    if genes >= 6:
        for i in range(32):
            for j in range(10, 12):
                combf.append(combf[i]+x[j])
                combm.append(combm[i]+y[j])
        combf[:32], combm[:32] = [], []
    if genes >= 7:
        for i in range(64):
            for j in range(12, 14):
                combf.append(combf[i]+x[j])
                combm.append(combm[i]+y[j])
        combf[:64], combm[:64] = [], []
    power(combf, combm)
def power(x, y):
    global punnett
    punnett = []
    for i in range(2**genes):
        j = 0
        while j < 2**genes:
            combinación = y[i]+x[j]
            separación = list(combinación)
            separación.sort(key=lambda v: (v.upper(), v[0].islower())) # http://stackoverflow.com/questions/13954841/python-sort-upper-case-and-lower-case
            punnett.append(''.join(separación))
            separación[:len(father)] = []
            j += 1
    todo, m= [], 0
    for i in range(len(punnett)):
        if i == len(x)*m:
            todo.append(y[m])
            m+=1
        todo.append(punnett[i])
    GUI(todo)
def GUI(todo):
    app = QApplication(sys.argv)
    resultados = QTableWidget()
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    with open("Genética.qss", "r") as f:
        resultados.setStyleSheet(f.read())
    resultados.setWindowTitle(father+" con "+mother)
    if len(combf) > 5:
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        resultados.resize(ancho, alto)
    resultados.setRowCount(len(combf)+1)
    resultados.setColumnCount(len(combf)+1)
    columna, contadorcomb = 0, 0
    for i in range(len(combf)):
        resultados.setItem(0, i+1, QTableWidgetItem(combf[i]))
    for i in range(len(todo)):
        if i == (len(combf) + 1) * contadorcomb:
            resultados.setItem(contadorcomb+1, 0, QTableWidgetItem(todo[i]))
            contadorcomb += 1
            columna = 0
        else:
            columna+=1
            resultados.setItem(contadorcomb, columna, QTableWidgetItem(todo[i]))
    resultados.show()
    return app.exec_()

    """resultados = tk.Toplevel() #Tk().withdraw() esconderá root
    try: resultados.iconbitmap("The Eye.ico")
    except:
        print("No se ha encontrado 'The Eye.ico'")
        input()
    resultados.resizable(False, False)
    ftabla, fbutton = font.Font(family="Open Sans", size=12), font.Font(family="Dubai Light", size=12)
    frame = tk.Frame(resultados) # tal vez cursor="tcross"
    resultados.title(father+" con "+mother)
    columna, contadorcomb = 0, 0
    for i in range(len(combf)):
        tk.Label(frame, text=combf[i], font=ftabla).grid(row=0, column=i+1)
    for i in range(len(todo)):
        if i == (len(combf)+1)*contadorcomb:
            tk.Label(frame, text=todo[i], font=ftabla).grid(row=contadorcomb+1, column=0)
            contadorcomb+=1
            columna = 0
        else:
            columna+=1
            tk.Label(frame, text=todo[i], font=ftabla, relief="groove").grid(row=contadorcomb, column=columna)
    def hoverg(event):
        genotipo.config(bg=resultados.cget("background"), fg="black")
    def nohoverg(event):
        genotipo.config(bg="#939393", fg="#f4f4f4")
    def hoverb(event):
        busc.config(bg=resultados.cget("background"), fg="black")
    def nohoverb(event):
        busc.config(bg="#939393", fg="#f4f4f4")
    menú = tk.Frame(resultados)
    menú.pack(fill=tk.X)
    genotipo = tk.Button(menú, font=fbutton, text="Calcular genotipos", command=HW)
    genotipo.config(bg="#939393", fg="#f4f4f4", bd=0)
    genotipo.pack(padx=10, side="left")
    busc = tk.Button(menú, font=fbutton, text="Buscar determinado genotipo", command=buscar)
    busc.config(bg="#939393", fg="#f4f4f4", bd=0)
    busc.pack(padx=10, side="right")
    genotipo.bind("<Enter>", hoverg)
    genotipo.bind("<Leave>", nohoverg)
    busc.bind("<Enter>", hoverb)
    busc.bind("<Leave>", nohoverb)
    frame.pack()
    resultados.mainloop()"""
def buscar():
    fuente = font.Font(family="Century Gothic", size=15)
    busqueda = tk.Toplevel()
    try:
        busqueda.iconbitmap("buscar.ico")
    except:
        print("No se encontró 'buscar.ico'")
        input()
    arriba = tk.Frame(busqueda)
    arriba.pack(pady=10)
    busqueda.maxsize(500, 100)
    busqueda.minsize(450, 90)
    blabel = tk.Label(arriba, text="Elemento a buscar: ", font=fuente)
    querye = tk.Entry(arriba, font=fuente)
    arriba.grid_columnconfigure(index=0, weight=1)
    blabel.grid(row=0, column=0, sticky="NWSE")
    querye.grid(row=0, column=1, sticky="NWSE")
    querye.focus()
    def guardar(event):
        query = querye.get()
        orasí(query)
    boton = tk.Button(busqueda, text="Buscar", font=fuente)
    boton.bind("<Return>", guardar)
    boton.bind("<Button>", guardar)
    boton.pack(ipadx=2, ipady=1, pady=5)
    def orasí(x):
        contador = 0
        for i in range(len(punnett)):
            if x == punnett[i]: contador+=1
        if contador == 0:
            mensaje = "No se ha encontrado la combinación "+x
            showinfo(title="Lo sentimos", message=mensaje)
        elif contador == 1:
            tit = str(contador)+" vez"
            mensaje = "Se ha encontrado "+x+" "+tit+"."
            showinfo(title="Encontrado", message=mensaje)
        else:
            tit = str(contador)+" veces"
            mensaje = "Se han encontrado "+x+" "+tit+"."
            showinfo(title=tit, message=mensaje)
    busqueda.mainloop()
def HW():
    dominante, recesivo, híbrido = [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(combf)):
        for k in range(len(combm)):
            for j in range(len(combf[1])):
                if combf[i][j] == combf[i][j].upper() and combm[k][j] == combm[k][j].upper():
                    dominante[j] += 1
                elif combf[i][j] != combf[i][j].upper() and combm[k][j] != combm[k][j].upper():
                    recesivo[j] += 1
    for i in range(7):
        dominante[i] = dominante[i] * 100 // len(punnett)
        recesivo[i] = recesivo[i] * 100 // len(punnett)
        híbrido[i] = 100 - recesivo[i] - dominante[i]
    Hardy = tk.Toplevel()
    Hardy.resizable(False, False)
    fuente = font.Font(family="Century Gothic", size=20)
    Hardy.iconbitmap("Genética.ico")
    for i in range(len(father)):
        if i % 2 == 0:
            dper, hper, rper = str(dominante[i//2])+"%", str(híbrido[i//2])+"%", str(recesivo[i//2])+"%"
            DPorcentaje, HPorcentaje, RPorcentaje = tk.Label(Hardy, text=dper, font=fuente), tk.Label(Hardy, text=hper, font=fuente), tk.Label(Hardy, text=rper, font=fuente)
            DPorcentaje.grid(row=i, column=0, ipady=10, ipadx=20)
            HPorcentaje.grid(row=i, column=1, ipady=10, ipadx=20)
            RPorcentaje.grid(row=i, column=2, ipady=10, ipadx=20)
        else:
            dom, hyb, rec = father[i].upper()*2, father[i].upper()+father[i].lower(), father[i].lower()*2
            Dominante, Híbrido, Recesivo = tk.Label(Hardy, text=dom, font=fuente), tk.Label(Hardy, text=hyb, font=fuente), tk.Label(Hardy, text=rec, font=fuente)
            Dominante.grid(row=i, column=0, ipady=10, ipadx=20)
            Híbrido.grid(row=i, column=1, ipady=10, ipadx=20)
            Recesivo.grid(row=i, column=2, ipady=10, ipadx=20)
#Ventana principal
def main():
    def enviar(event):
        global father, mother
        father, mother = fatheri.get(), motheri.get()
        check(father, mother)
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
        img = tk.PhotoImage(file="Genética-resized.jpg")
    except:
        print("No se ha encontrado la imagen 'Genética-resized.jpg'")
        input()
    tk.Label(root, image=img).grid(row=1)
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
        root.iconbitmap("Genética.ico")
    except:
        print("No se encontró 'Genética.ico'")
        input()
    root.mainloop()
main()
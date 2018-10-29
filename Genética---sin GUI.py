# coding=utf-8
import time, sys, os
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
    print(todo)
    if genes == 2:
        tablados(todo, x)
    elif genes == 3:
        tablatres(todo, x)
    elif genes == 4:
        tablacuatro(todo, x)
    elif genes == 5:
        tablacinco(todo, x)
    elif genes == 6:
        tablaseis(todo, x)
    elif genes == 7:
        tablasiete(todo, x)
def tablados(todo, combf):
    print("    ", end=" ")
    contadorcomb = 0
    for i in range(len(combf)):
        print("¦ ", combf[i], end="  ")
    print("¦", end="")
    print("\n    ", "-" * 29, end="")
    for i in range(len(todo)):
        if i == (len(combf)+1)*contadorcomb:
            print("\n¦", todo[i], end=" ¦")
            contadorcomb+=1
        else:
            print("", todo[i], end=" |")
    input()
    decision()
def tablatres(todo, combf):
    print("     ", end=" ")
    contadorcomb = 0
    for i in range(len(combf)):
        print("¦  ", combf[i], end="  ")
    print("¦", end="")
    print("\n     ", "-" * 73, end="")
    for i in range(len(todo)):
        if i == (len(combf)+1)*contadorcomb:
            print("\n¦", todo[i], end=" ¦")
            contadorcomb+=1
        else:
            print("", todo[i], end=" |")
    input()
    decision()
def tablacuatro(todo, combf):
    print("     ", end="  ")
    contadorcomb = 0
    for i in range(len(combf)):
        print("¦  ", combf[i], end="   ")
    print("¦", end="")
    print("\n      ", "-" * 177, end="")
    for i in range(len(todo)):
        if i == (len(combf)+1)*contadorcomb:
            print("\n¦", todo[i], end=" ¦")
            contadorcomb+=1
        else:
            print("", todo[i], end=" |")
    input()
    decision()
def tablacinco(todo, combf):
    print("     ", end="   ")
    contadorcomb = 0
    for i in range(len(combf)):
        print("¦   ", combf[i], end="   ")
    print("¦", end="")
    print("\n       ", "-" * 417, end="")
    for i in range(len(todo)):
        if i == (len(combf)+1)*contadorcomb:
            print("\n¦", todo[i], end=" ¦")
            contadorcomb+=1
        else:
            print("", todo[i], end=" |")
    input()
    decision()
def tablaseis(todo, combf):
    print("     ", end="    ")
    contadorcomb = 0
    for i in range(len(combf)):
        print("¦   ", combf[i], end="    ")
    print("¦", end="")
    print("\n        ", "-" * 961, end="")
    for i in range(len(todo)):
        if i == (len(combf)+1)*contadorcomb:
            print("\n¦", todo[i], end=" ¦")
            contadorcomb+=1
        else:
            print("", todo[i], end=" |")
    input()
    decision()
def tablasiete(todo, combf):
    print("     ", end="     ")
    contadorcomb = 0
    for i in range(len(combf)):
        print("¦    ", combf[i], end="    ")
    print("¦", end="")
    print("\n         ", "-" * 2177, end="")
    for i in range(len(todo)):
        if i == (len(combf)+1)*contadorcomb:
            print("\n¦", todo[i], end=" ¦")
            contadorcomb+=1
        else:
            print("", todo[i], end=" |")
    input()
    decision()
def decision():
    eleccion = 0
    while eleccion != 1  or eleccion != 2 or eleccion != 3 or eleccion != 4:
        eleccion = input("\n\n1.- Probar diferentes genotipos.\n2.- Calcular probabilidad de algún genotipo.\n3.- Calcular porcentaje de cada genotipo.\n4.- Cerrar programa.\nElección: ")
        try:
            eleccion = int(eleccion)
        except:
            print("\nPresiona del 1 al 4 de acuerdo a lo que desees. ¿OK?")
            input()
            continue
        if eleccion == 1:
            main()
        elif eleccion == 2:
            lookfor()
        elif eleccion == 3:
            HW()
        elif eleccion == 4:
            sys.exit()
        else:
            print("\nPresiona del 1 al 3 de acuerdo a lo que desees. ¿OK?")
            input()
def lookfor():
    busq, cont = input("Elemento a buscar: "), 0
    for i in range(len(punnett)):
        if punnett[i] == busq: cont += 1
    if cont == 1: print("Se encontró "+busq," 1 vez.         Porcentaje: ", cont*100/len(punnett), "%         Total de probabilidades: ", len(punnett))
    elif cont == 0: print(busq, "no se encuentra dentro de las", len(punnett), "combinaciones totales.")
    else: print("Se encontró "+busq, cont, "veces.         Porcentaje: ", cont*100/len(punnett), "%         Total de probabilidades: ", len(punnett))
    input()
    eleccion = 0
    while eleccion != 1 or eleccion != 2 or eleccion != 3:
        eleccion = input("\n\n1.- Cerrar programa.\n2.- Regresar.\n3.- Probar otros genotipos.\nElección: ")
        try:
            eleccion = int(eleccion)
        except:
            print("\nPresiona del 1 al 4 de acuerdo a lo que desees. ¿OK?")
            input()
            continue
        if eleccion == 1:
            sys.exit()
        elif eleccion == 2:
            decision()
        elif eleccion == 3:
            main()
        else:
            print("Presiona del 1 al 3 de acuerdo a lo que desees.¿OK?")
            input()
def HW():
    dominante, recesivo, híbrido = [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(combf)):
        for k in range(len(combm)):
            for j in range(len(combf[1])):
                if combf[i][j] == combf[i][j].upper() and combm[k][j] == combm[k][j].upper(): dominante[j] += 1
                elif combf[i][j] != combf[i][j].upper() and combm[k][j] != combm[k][j].upper(): recesivo[j]+=1
    for i in range(7):
        dominante[i] = dominante[i]*100 // len(punnett)
        recesivo[i] = recesivo[i]*100 // len(punnett)
        híbrido[i] = 100 - recesivo[i] - dominante[i]
    for i in range(len(father)//2):
        MrRobot = 2*i
        print(father[MrRobot].upper()*2, ":", dominante[i], "%   ", father[MrRobot].upper()+father[MrRobot].lower(), ":", híbrido[i], "%   ", father[MrRobot].lower()*2, ":", recesivo[i], "%")
    eleccion = 0
    while eleccion != 1 or eleccion != 2 or eleccion != 3:
        eleccion = int(input("\n\n1.- Cerrar programa.\n2.- Regresar.\n3.- Probar otros genotipos.\nElección: "))
        if eleccion == 1:
            sys.exit()
        elif eleccion == 2:
            decision()
        elif eleccion == 3:
            main()
        else:
            print("Presiona del 1 al 3 de acuerdo a lo que desees.")
        time.sleep(3)
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    global father, mother
    father, mother = None, None
    father = input("Introduce el genotipo del padre, por ejemplo AaBb: ")
    mother = input("Introduce el genotipo de la madre, por ejemplo AaBb: ")
    if len(father) % 2 != 0:
        print("Debes proporcionar un número de alelos pares. Por característica pueden haber 2 alelos: dominante (A) y recesivo (a).")
        main()
        return 0
    if len(father) != len(mother):
        print("El número de caracteres de " + father + " debe ser igual al de " + mother)
        main()
        return 0
    elif (len(father) or len(mother)) > 14:
        print("Ups!! No es posible calcular más allá de 7 características")
        main()
        return 0
    if ((father or mother) == ("autor" or "author")):
        print("Realizado por Benjamín Antonio Velasco Guzmán")
        main()
        return 0
    if (father or mother) == None:
        print("Debes escribir un genotipo, por ejemplo AaBb")
        main()
        return 0
    combinaciones(father, mother)
main()
from cx_Freeze import setup, Executable
import time, sys, os

setup(  name = "Genética",
    version = "1.0",
    description = "Genética de poblaciones, Leyes de Mendel",
    executables = [Executable("Genética---sin GUI.py", base = None)])
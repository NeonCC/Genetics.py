import os
from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY'] = 'C:/Program Files (x86)/Python/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Program Files (x86)/Python/tcl/tk8.6'
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=['C:/Program Files (x86)/Python/DLLs/tcl86t.dll', 'C:/Program Files (x86)/Python/DLLs/tk86t.dll']
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('Genética.py', base=None)
]

setup(name='Genética',
      version = '1.0',
      description = 'Genética de poblaciones, Leyes de Mendel',
      options = dict(build_exe = buildOptions),
      executables = executables)
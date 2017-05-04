import os
os.environ['TCL_LIBRARY'] = "C:\Python\pyi-env-name\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\Python\pyi-env-name\\tcl\\tk8.6"
from cx_Freeze import setup, Executable
import sys

build_exe_options = {"packages": ["files", "tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Name",
    version="1.0",
    description="Description",
    options={"build_exe": build_exe_options},
    executables=[Executable("main2.py", base=base)],
    package_dir={'': ''},
    )
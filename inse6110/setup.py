from cx_Freeze import setup, Executable
import os
import sys

base = None    

os.environ['TCL_LIBRARY'] = r'C:\\Users\\Asif\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Users\\Asif\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6'


executables = [Executable("EncryptionUI.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
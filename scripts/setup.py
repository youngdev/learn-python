from cx_Freeze import setup, Executable

setup (
    name = "www.enalta.com",
    version = 1.0,
    description = ".py to .exe",
    executables = [Executable("enviar_dados.py")])

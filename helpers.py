import os
import re
import platform

def pausar_app():
    return input("Presione ENTER para continuar...")

def limpiar_app():
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("$ ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
        else: print(mensaje) if mensaje else None

def rut_validator(rut, lista):
    # Verificar si el RUT coincide con el patrón
    if not re.match("[0-9]{4,8}-[0-9kK]$", rut):
        print("Rut incorrecto o no soportado, debe cumplir el formato.")
        return False
    for cliente in lista:
        if cliente.rut == rut:
            print("RUT ya esta registrado!")
            return False
    return True
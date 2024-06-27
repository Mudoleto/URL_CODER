#!/usr/bin/env python
#-*- coding: utf-8 -*-

from diccionario import decodificador


if __name__ == "__main__":
    palabra_decodificar = input("Ingresa la palabra decodificar:")
    instancia = decodificador()
    clave = instancia.diccionario(palabra_decodificar)
    
    print("test%0a{}".format(clave))
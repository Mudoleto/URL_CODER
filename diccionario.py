#!/usr/bin/env python
#-*- coding: utf-8 -*-

letras_mayusculas = {
                    'A':'%41', 'B':'%42', 'C':'%43',
                    'D':'%44', 'E':'%45', 'F':'%46',
                    'G':'%47', 'H':'%48', 'I':'%49',
                    'J':'%4A', 'K':'%4B', 'L':'%4C',
                    'M':'%4D', 'N':'%4E', 'O':'%4F',
                    'P':'%50', 'Q':'%51', 'R':'%52',
                    'S':'%53', 'T':'%54', 'U':'%55',
                    'V':'%56', 'W':'%57', 'X':'%58',
                    'Y:':'%59','Z':'%5A'
                    }

letras_minusculas = {
                    'a':'%61', 'b':'%62', 'c':'%63',
                    'd':'%64', 'e':'%65', 'f':'%66',
                    'g':'%67', 'h':'%68', 'i':'%69',
                    'j':'%6a', 'k':'%6b', 'l':'%6c',
                    'm':'%6d', 'n':'%6e', 'o':'%6f',
                    'p':'%70', 'q':'%71', 'r':'%72',
                    's':'%73', 't':'%74', 'u':'%75',
                    'v':'%76', 'w':'%77', 'x':'%78',
                    'y':'%79', 'z':'%7a'
                    }

numeros = {
        '0':'%30', '1':'%31', '2':'%32', '3':'%33', 
        '4':'%34', '5':'%35', '6':'%36', '7':'%37',
        '8':'%38', '9':'%39'
        }

caracteres_especiales = {
                        ' ':'%20','!':'%21', '"':'%22', '#':'%23', '$':'%24',
                        '%':'%25', '&':'%26', "'":'%27', '(':'%28',
                        ')':'%29', '*':'%2a', '+':'%2b', ',':'%2c',
                        '-':'%2d', '.':'%2e', '/':'%2f', ':':'%3a',
                        ';':'%3b', '<':'%3c', '=':'%3d', '>':'%3e',
                        '?':'%3f', '@':'%40', '[':'%5b','\\':'%5c',
                        ']':'%5d','^':'%5e', '_':'%5f', '`':'%60', 
                        '{':'%7b', '|':'%7c', '}':'%7d', '~':'%7e'
                        }

class decodificador():

    def url_decode(self, ruta):
        self.ruta = ruta
        ruta_codificada = ''
        
        for i in ruta:
            if i in letras_mayusculas:
                ruta_codificada = ruta_codificada + letras_mayusculas[i]

                
            elif i in letras_minusculas:
                ruta_codificada = ruta_codificada + letras_minusculas[i]
                            
            elif i in caracteres_especiales:
                ruta_codificada = ruta_codificada + caracteres_especiales[i]
            
            elif i in numeros:
                ruta_codificada = ruta_codificada + numeros[i]
            
            elif i == '"':
                ruta_codificada = ruta_codificada + '%22'
            
            else:
                ruta_codificada = ruta_codificada + i
            
        return ruta_codificada 

    def diccionario(self, palabra_decodificar):
        self.palabra_decodificar = palabra_decodificar
        palabra_decodificar = self.url_decode(palabra_decodificar)
        return palabra_decodificar
        
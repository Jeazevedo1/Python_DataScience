# -*- coding: utf-8 -*-
"""Untitled33.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OzsnW9t--hiOz4kraEBKNGBkmh7Vsovs
"""

#recebe a string do usuario
nome_string= input("Digite uma string: ")

#inverte a string
nome_invertido = ""
for letra in nome_string:
  nome_invertido = letra + nome_invertido

#Exibe a string invertida
print("A string invertida é: ",nome_invertido)
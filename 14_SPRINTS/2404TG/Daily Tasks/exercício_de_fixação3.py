# -*- coding: utf-8 -*-
"""Exercício de fixação3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UUyCKsiH_VbZa8ZffZAnefwAx-QBZV-F
"""

idade = int(input("Informe a idade do nadador: "))

if idade < 5:
  print("Nadador sem classificação")
elif 5 <= idade <= 7:
  print("Nadador é Infantil A")
elif 8 <= idade <= 11:
  print("Nadador é Infantil B")
elif 12 <= idade <= 13:
  print("Nadador é Juvenil A")
elif 14 <= idade <= 17:
  print("Nadador é Juvenil B")
else:
  print("Nadador é Adulto")
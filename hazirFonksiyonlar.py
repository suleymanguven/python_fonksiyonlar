from math import *
from random import *
import datetime
import locale
locale.setlocale(locale.LC_ALL,'italian')
""""
sayi=int(input("sayı giriniz:"))
#karekok=sqrt(sayi)
print(sqrt(sayi))

print(cos(sayi))
print(sin(sayi))


z=pow(4,5)
print(z)

print(random())

print(randint(20,50))

print(randrange(60))
"""

simdi=datetime.datetime.now()
print(simdi)
#print(simdi.year)
#print(simdi.month)

suan=datetime.datetime.strftime(simdi,'%X')
print(suan)
suan1=datetime.datetime.strftime(simdi,'%A')
print(suan1)
ay=datetime.datetime.strftime(simdi,'%B')
print(ay)
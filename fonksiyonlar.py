"""""
def toplama():
    sayi1=int(input("Toplanacak 1. sayıyı giriniz: "))
    sayi2=int(input("Toplanacak 2. sayıyı giriniz: "))
    toplam=sayi1+sayi2
    print("Toplam: ",toplam)
def carpma():
    sayi1=int(input("Çarpılacak 1. sayıyı giriniz: "))
    sayi2=int(input("Çarpılacak 2. sayıyı giriniz: "))
    carpim=sayi1*sayi2
    print("Toplam: ",carpim)
tercih=input("Toplama işlemi için {T} Çarpma işlemi için {C} tuşuna basınız: ")
tercih=tercih.upper()
if tercih=='T':
    toplama()
elif tercih=='C':
    carpma()
else:
    print("Lütfen tercihinizi kontrol ediniz. İşlem yapılamadı.")
"""
def toplama(sayi1,sayi2):
    print("Toplam: ",sayi1+sayi2)
def carpma(a,b):
    print("Çarpma: ",a*b)
deger1=int(input("1. değeri giriniz: "))
deger2=int(input("2. değeri giriniz: "))
tercih=input("Toplama işlemi için {T} Çarpma işlemi için {C} tuşuna basınız:")
tercih=tercih.upper()
if tercih=='T':
    toplama(deger1,deger2)
elif tercih=='C':
    carpma(deger1,deger2)
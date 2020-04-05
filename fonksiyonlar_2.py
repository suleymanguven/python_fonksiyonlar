"""""""""
def liste(deger1,deger2,deger3,deger4):
    print("Kullanıcıdan gelecek veri1:",deger1)
    print("Kullanıcıdan gelecek veri2:", deger2)
    print("Kullanıcıdan gelecek veri3:", deger3)
    print("Kullanıcıdan gelecek veri4:", deger4)

ad=input("adınızı giriniz:")
soyad=input("soyadınızı giriniz")
il=input("ilinizi giriniz: ")
ilce=input("ilçenizi giriniz: ")
liste(ad,soyad,il,ilce)
#
#

tcKimlik=input("T.C. Kimlik no : ")
tel=input("Telefon no: ")
dyil=input("doğum yılı:")
eposta=input("eposta adresi:")
liste(tcKimlik,tel,dyil,eposta)



def listeleme(deger1):
    print("Ürünlerin satış toplam tutarı: ",deger1)
def kdvToplamTutar(deger1,deger2):
    kdvliTutar=int((deger1*(deger2/100)+deger1))
    dvergisi=kdvliTutar*0.09
    toplamTutar=kdvliTutar+dvergisi
    listeleme(toplamTutar)


urun1=int(input("1. ürünün satış tutarı: "))
urun2=int(input("2. ürünün satış tutarı: "))
urun3=int(input("3. ürünün satış tutarı: "))
kdv=int(input("kdv oranı nedir?"))
toplam=urun1+urun2+urun3
tercih=input("satış tutarını listelemek için {S} kdv'li satış tutarını listelemek için {K} tuşlayınız: ")
tercih=tercih.upper()
if tercih=='S':
    listeleme(toplam)
elif tercih=='K':
    kdvToplamTutar(toplam,kdv)

"""""
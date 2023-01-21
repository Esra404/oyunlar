print("BU BİR HESAP MAKİNASI UYGULAMASIDIR  LÜTFEN İKİ SAYI GİRİNİZ")

sayi1=print(input("Birinci sayi="))
sayi2=print(int(input("İkinci sayi=")))

def toplama(sayi1,sayi2):
    return sayi1+sayi2
    
def cikarma(sayi1,sayi2):
    return sayi1+sayi2
def carpma(sayi1,sayi2):
    return sayi1*sayi2
def bolme(sayi1,sayi2):
    return sayi1/sayi2

print(" gireceğiniz işleme göre seçim yapmalısınız  ")

print("     1-için Toplama")
print("     2-için çıkarma")
print("     3-için çarpma")
print("    4-için bölme işlemi yapılır")

print("lütfen işlem için birden dorde kadar bir sayı seçiniz")
sayi=int(input("sayınızı girinzi==="))
if (sayi==1):
    toplama(sayi1,sayi2)
elif(sayi==2):
    cikarma(sayi1,sayi2)
elif(sayi==3):
    carpma(sayi1,sayi2)
else:
    bolme(sayi1,sayi2)



print("--------------BU BİR HESAP MAKİNASI UYGULAMASIDIR  LÜTFEN İKİ SAYI GİRİNİZ--------------")



def toplama(sayi1,sayi2):
    return sayi1+sayi2
    
def cikarma(sayi1,sayi2):
    return sayi1-sayi2

def carpma(sayi1,sayi2):
    return sayi1*sayi2
def bolme(sayi1,sayi2):
    return sayi1/sayi2

print(" İŞLEM YAPILACAKTI***************************gireceğiniz işleme göre seçim yapmalısınız************************  ")

print("     1-için Toplama")
print("     2-için çıkarma")
print("     3-için çarpma")
print("    4-için bölme işlemi yapılır")


sayi1=int((input("Birinci sayi=")))
sayi2=int(input("İkinci sayi="))


print("*lütfen işlem için birden dorde kadar bir sayı seçiniz*")
sayi=int(input("sayınızı girinzi==="))
if (sayi==1):
   print(toplama(sayi1,sayi2))
elif(sayi==2):
    print(cikarma( sayi1,sayi2))
elif(sayi==3):
    print(carpma(sayi1,sayi2))
elif(sayi==4):

    print(bolme(sayi1,sayi2))



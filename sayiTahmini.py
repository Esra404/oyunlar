import random
sayi=random.randint(1,1000)

print("bu bir sayı tahmin oyunudur lütfen bir sayı tahmin ediniz doğru tahmini ederseniz size bir pide!!:)")
def sayiBulma(tahmin):
    while(True):

        tahmin=int(input("lütfen sayi gir="))
        if(tahmin==sayi):
            print("ooo doğru sayıyı tek hamlede buldun seni pideci seni")
            break 
        elif(tahmin<sayi):
            print("hay aksi tahminin sayıdan küçük biraz daha artırarak  tahmin edebilirsin yeni sayı  alalım.")
        else:
            print("hay aksi tahminin sayıdan büyük azaltarak devam edebilirsin devam edelim")







sayiBulma(1)
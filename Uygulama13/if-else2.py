import random
sayilar=[]
i=0
deger = int(input("Kaç değer istiyorsunuz : "))
while (i<deger):
    sayi = random.randint(1,100)
    sayilar.append(sayi)
    i+=1
sayilar.sort()
print(sayilar)

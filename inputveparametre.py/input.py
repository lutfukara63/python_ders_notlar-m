#input dışardan veri alır
isim=input("İsminiz nedir?")

### sayısal verileri formatlamak için
pi=3.14156
print("pi sayısı yaklaşık {:.2f}".format(pi)) # 2 basamaklı gösterir


#veri yerine yazmanın birkaçtemel yolu vardır
ad=input("Adınız nedir?")
yas=input("Yaşınız nedir?")    
print(f"merahaba,benim adım {ad} ve yaşım {yas}") # f ile yazdırma
# print("merhaba,benim adım" +ad+ "ve yaşım" +yas) # + ile yazdırma

sayı1=int(input("Birinci sayıyı giriniz:"))
sayı2=int(input("İkinci sayıyı giriniz:"))
toplam=sayı1+sayı2
print("Girdiğiniz{} ve {sayı2} sayılarının toplamı: {toplam}") # {} ile yazdırma
print("Girdiğiniz{} ve {} sayılarının toplamı: {}").format(sayı1,sayı2,toplam) # format ile yazdırma
print("Girdiğiniz" + str(sayı1) + "ve" + str(sayı2) + "sayılarının toplamı:" + str(toplam)) # + ile yazdırma


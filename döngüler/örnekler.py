 #String uzunluğunu bulma
kelime = "merhaba"
sayac = 0
for harf in kelime:
 sayac += 1
print(f"Kelimenin uzunluğu: {sayac}")


 #Bir stringi tersten yazdırma
kelime = "Python"
ters = ""
for harf in kelime:
 ters = harf + ters
print(f"Ters: {ters}")

ters = kelime[::-1]
print(f"Ters: {ters}")


def tersten_yaz(kelime):
    ters = ""
    for harf in kelime:
        ters = harf + ters
    return ters

print(tersten_yaz("OpenAI"))  # Çıktı: IAnepO



 #Stringdeki büyük ve küçük harf sayısını bulma
kelime = "Python Programlama"
buyuk_harf = 0
kucuk_harf = 0
for harf in kelime:
 if harf.isupper():
   buyuk_harf += 1
 elif harf.islower():
   ucuk_harf += 1
print(f"Büyük harf sayısı: {buyuk_harf}")
print(f"Küçük harf sayısı: {kucuk_harf}")



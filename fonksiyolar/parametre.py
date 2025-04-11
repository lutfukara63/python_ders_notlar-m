def selamla(isim):
 print(f"Merhaba, {isim}!")
selamla("Ayşe") # Çıktı: Merhaba, Ayşe!
selamla("Ali") # Çıktı: Merhaba, Ali!


def toplama(a, b):
 return a + b
sonuc = toplama(10, 20)
print(sonuc) # Çıktı: 30




def selamla(isim="Dünya"):
 print(f"Merhaba, {isim}!")
selamla() # Çıktı: Merhaba, Dünya!
selamla("Zeynep") # Çıktı: Merhaba, Zeynep!

# Bir fonksiyon, işlem sonucunu `return` anahtar kelimesi ile döndürebilir.


def carpma(a, b):
 return a * b
sonuc = carpma(5, 3)
print(sonuc) # Çıktı: 15

#Python’da küçük ve tek satırlık fonksiyonlar için `lambda` kullanılır


kare = lambda x: x ** 2
print(kare(4)) # Çıktı: 16
topla = lambda a, b: a + b
print(topla(10, 20)) # Çıktı: 30







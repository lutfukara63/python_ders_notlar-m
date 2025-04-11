'''
for Döngüsünün Genel Yapısı
for eleman in iterable:
 işlemler
• eleman: Döngü her çalıştığında, sıradaki elemanı temsil eder.
• iterable: Döngünün üzerinde işlem yapacağı veri kümesi
'''

kelime = "Python"
for harf in kelime:
 print(harf)


#range fonksiyonu ile döngü oluşturma
for i in range(5):
 print(i)
# Çıktı: 0 1 2 3 4
#range burada 0'dan başlayıp 5'e kadar olan sayıları döndürür.


# Listeye çift sayıları ekleme
cift_sayilar = []
for i in range(1, 11):
 if i % 2 == 0:
  cift_sayilar.append(i)
print(cift_sayilar)

# Her kelimenin ilk harfini büyük yazdırma
kelimeler = ["python", "programlama", "döngüler"]
for kelime in kelimeler:
 print(kelime.capitalize())

n = int(input("Kaç Fibonacci sayısı yazdırılsın: "))
a, b = 0, 1
for _ in range(n):
 print(a)
 a, b = b, a + b

  # Çarpım Tablosu
for i in range(1, 6):
 for j in range(1, 6):
  print(f"{i} x {j} = {i * j}")
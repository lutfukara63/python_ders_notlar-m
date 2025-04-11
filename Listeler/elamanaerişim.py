""" Liste Elemanlarına Aralıklarla Erişim (Dilimeleme - Slicing)
Bir listenin belli bir aralığını almak için dilimeleme (slicing) işlemi yapılabilir. Bunun için 
liste[başlangıç:bitiş:adım] formatı kullanılır."""
# Başlangıç indeksi dahil, bitiş indeksi hariç alınır. Adım ise aralıklarla almayı sağlar.
# Liste tanımı
sayilar = [10, 20, 30, 40, 50]
# İlk üç eleman
print(sayilar[:3]) # Çıktı: [10, 20, 30]
# Üçüncü elemandan sonuna kadar
print(sayilar[2:]) # Çıktı: [30, 40, 50]
# Adım atlayarak elemanları al
print(sayilar[::2]) # Çıktı: [10, 30, 50]

#Liste uzunluğunu bulma
print(len(sayilar)) # Çıktı: 5

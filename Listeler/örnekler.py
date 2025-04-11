liste1 = [10, 20, 30]
liste2 = [1, 2, 3]
# Toplamları manuel olarak hesaplayıp yeni listeye kaydediyoruz
toplamlar = [liste1[0] + liste2[0], liste1[1] + liste2[1], liste1[2] + liste2[2]]
print(toplamlar) # Çıktı: [11, 22, 33

#Bir sayı listesindeki en küçük ikinci elemanı bulun.

sayilar = [5, 1, 7, 3]
# Öncelikle listeyi sıralıyoruz
sirali = [min(sayilar), max(sayilar)] # İlk sıralama
sirali.insert(1, 3) # Küçük ikinci eleman olarak 3'ü ekledik
print(sirali[1]) # Çıktı: 3


#sayilar = [10, 20, 30, 40, 50]
# Listenin ortanca elemanını seçiyoruz
ortanca = sayilar[len(sayilar)//2] # Listenin orta indeksi
print(ortanca) # Çıktı: 30
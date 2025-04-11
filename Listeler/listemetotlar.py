#append()
#Listenin sonuna bir eleman ekler.
sayilar = [1, 2, 3]
sayilar.append(4) # Listeye 4 ekle
print(sayilar) # Çıktı: [1, 2, 3, 4]

 #clear()
#Liste içindeki tüm elemanları siler:
sayilar = [1, 2, 3]
sayilar.clear()
print(sayilar) # Çıktı: []

 #copy()
# Bir listeyi başka bir listeye kopyalar:
orijinal = [1, 2, 3]
kopya = orijinal.copy()
print(kopya) # Çıktı: [1, 2, 3]

 #count()
# Bir elemanın listede kaç kez geçtiğini bulur:
sayilar = [1, 2, 2, 3, 2]
print(sayilar.count(2)) # Çıktı: 3

 #extend()
#Bir listeye başka bir listeyi ekler:
liste1 = [1, 2]
liste2 = [3, 4]
liste1.extend(liste2)
print(liste1) # Çıktı: [1, 2, 3, 4]

 #index()
#Bir elemanın indeks numarasını döndürür:
meyveler = ["elma", "armut", "çilek"]
print(meyveler.index("armut")) # Çıktı: 1

 #insert()
# Belirtilen bir indekse yeni bir eleman ekler:
sayilar = [1, 3, 4]
sayilar.insert(1, 2) # 1. indekse 2 ekle
print(sayilar) # Çıktı: [1, 2, 3, 4]

# pop()
#Bir elemanı siler ve silinen elemanı döndürür:
sayilar = [1, 2, 3]
silinen = sayilar.pop(1) # 1. indeksteki elemanı sil
print(silinen) # Çıktı: 2
print(sayilar) # Çıktı: [1, 3]

 #remove()
#Belirtilen değeri listeden siler:
sayilar = [1, 2, 3]
sayilar.remove(2) # 2 değerini sil
print(sayilar) # Çıktı: [1, 3]

# sort()
#Liste elemanlarını sıralar:
sayilar = [3, 1, 2]
sayilar.sort()
print(sayilar) # Çıktı: [1, 2, 3]

# reverse()
#Liste elemanlarını tersine çevirir:
sayilar = [1, 2, 3]
sayilar.reverse()
print(sayilar) # Çıktı: [3, 2, 1]

#del
#Bir elemanı indeksle silmek için kullanılır:
sayilar = [1, 2, 3]
del sayilar[1] # 1. indeksteki elemanı sil
print(sayilar) # Çıktı: [1, 3]
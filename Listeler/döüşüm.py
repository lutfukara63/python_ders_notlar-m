#Farklı veri türlerini listeye çevirmek için list() fonksiyonu kullanılabilir:
# String'den listeye
string = "Python"
liste = list(string)
print(liste) # Çıktı: ['P', 'y', 't', 'h', 'o', 'n']
# Tuple'dan listeye
tuple_data = (1, 2, 3)
liste = list(tuple_data)
print(liste) # Çıktı: [1, 2, 3]
# Set'ten listeye
set_data = {1, 2, 3}
liste = list(set_data)
print(liste) # Çıktı: [1, 2, 3]
#list ile listelenir

#Listeler, başka listeleri eleman olarak içerebilir:
icerik = [[1, 2], [3, 4], [5, 6]]
print(icerik[0]) # Çıktı: [1, 2]
print(icerik[0][1]) # Çıktı: 2
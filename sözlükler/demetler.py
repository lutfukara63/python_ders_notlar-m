'''

demetler (Tuples)
Genel Bilgi ve Özellikler
• Tanım:
Demetler, sıralı fakat değiştirilemez (immutable) veri yapılarıdır.
• Oluşturma:
Parantezler () kullanılarak oluşturulur.
• Kullanım Durumları:
o Sabit veriler saklamak için idealdir.
o Değişmezlikleri sayesinde sözlüklerin anahtarları olarak da 
kullanılabilirler.
• Özellikler:
o Immutable: Bir kere oluşturulduktan sonra elemanları ekleme, silme veya 
değiştirme yapılamaz.
o İndekslenebilir: Listeler gibi indeksleme, slicing (dilimleme) ve unpacking
yapılabilir.
Temel İşlemler
1. Basit Demet Oluşturma ve Yazdırma
Kod:
2. my_tuple = (1, 2, 3, 4)
3. print(my_tuple)
Beklenen Çıktı:
(1, 2, 3, 4)
4. Elemanlara Erişim (Indexing)
Kod:
5. my_tuple = (10, 20, 30, 40)
6. print("İlk eleman:", my_tuple[0])
7. print("Son eleman:", my_tuple[-1])
Beklenen Çıktı:
İlk eleman: 10
Son eleman: 40
8. Demet Unpacking (Ayrıştırma)
Kod:
9. my_tuple = (10, 20, 30)
10. a, b, c = my_tuple
11. print(a, b, c)
Beklenen Çıktı:
10 20 30
12. Tek Elemanlı Demet Oluşturma
Kod:
13. single_tuple = (5,) # Tek elemanlı demet oluşturmak için sonrasında virgül 
gerekir.
14. print(single_tuple)
Beklenen Çıktı:
(5,)
15. Dönüşümler: Demet ↔ Liste
o Demeti Listeye Çevirme:
o my_tuple = (1, 2, 3, 4)
o my_list = list(my_tuple)
o print(my_list)
Beklenen Çıktı:
[1, 2, 3, 4]
o Listeyi Demete Çevirme:
o my_list = [1, 2, 3, 4]
o my_tuple = tuple(my_list)
o print(my_tuple)
Beklenen Çıktı:
(1, 2, 3, 4)
16. Slicing (Dilimeleme) İşlemi
Kod:
17. my_tuple = (0, 1, 2, 3, 4, 5)
18. slice_tuple = my_tuple[2:5]
19. print(slice_tuple)
Beklenen Çıktı:
(2, 3, 4)
20. Tuple İçinde Tuple Kullanımı
Kod:
21. nested_tuple = ((1, 2), (3, 4), (5, 6))
22. print(nested_tuple[1][0]) # İkinci iç demetin ilk elemanı.
Beklenen Çıktı:
3










'''
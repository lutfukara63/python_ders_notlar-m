'''

Sözlükler (Dictionaries)
Genel Bilgi ve Özellikler
• Tanım:
Sözlükler, anahtar-değer (key-value) çiftlerini saklayan, değiştirilebilir 
(mutable) veri yapılarıdır.
• Anahtar (Key):
Genellikle immutable (değiştirilemez) veri tiplerinden (örneğin, string, sayı, 
demet) seçilir. Her anahtar benzersizdir.
• Değer (Value):
Herhangi bir veri tipi olabilir; hatta başka bir sözlük veya liste bile olabilir.
• Özellikler:
o Değiştirilebilir: Oluşturulduktan sonra eleman ekleyip, güncelleyebilir 
veya silebilirsiniz.
o Sırasız (Python 3.7 öncesinde): Python 3.7 ve sonraki sürümlerde ekleme 
sırasını korur.
o Hızlı Erişim: Anahtarlar sayesinde O(1) zamanlı erişim sağlar.


Temel İşlemler
1. Sözlük Oluşturma ve Yazdırma
Kod:
2. person = {"isim": "Ali", "yas": 30, "sehir": "Ankara"}
3. print(person)
Beklenen Çıktı:
{'isim': 'Ali', 'yas': 30, 'sehir': 'Ankara'}
4. Anahtar Değer Erişimi
Kod:
5. print(person["isim"])
Beklenen Çıktı:
Ali
6. Değer Güncelleme ve Yeni Eleman Ekleme
Kod:
7. person["yas"] = 31 # Mevcut değeri güncelleme
8. person["meslek"] = "Mühendis" # Yeni anahtar-değer çifti ekleme
9. print(person)
Beklenen Çıktı:
{'isim': 'Ali', 'yas': 31, 'sehir': 'Ankara', 'meslek': 'Mühendis'}
10. Eleman Silme (del ve pop)
Kod (del ile):
11. del person["sehir"]
12. print(person)
Beklenen Çıktı:
{'isim': 'Ali', 'yas': 31, 'meslek': 'Mühendis'}
Kod (pop ile):
person["sehir"] = "Ankara" # "sehir" anahtarını yeniden ekleyelim
sehir = person.pop("sehir")
print("Silinen şehir:", sehir)
print(person)
Beklenen Çıktı:
Silinen şehir: Ankara
{'isim': 'Ali', 'yas': 31, 'meslek': 'Mühendis'}
13. Döngü ile Anahtar, Değer ve Çiftler Üzerinde Gezinme
o Anahtarlar Üzerinde:
o for key in person:
o print(key, "->", person[key])
Beklenen Çıktı (sıra ekleme sırasına göre):
isim -> Ali
yas -> 31
meslek -> Mühendis
o Sadece Değerler:
o for value in person.values():
o print(value)
Beklenen Çıktı:
Ali
31
Mühendis
o Anahtar-Değer Çiftleri:
o for key, value in person.items():
o print(key, ":", value)
Beklenen Çıktı:
isim : Ali
yas : 31
meslek : Mühendis
14. Sözlüğü Kopyalama ve Birleştirme (update)
Kod:
15. person_copy = person.copy()
16. print("Kopya:", person_copy)
17.
18. extra_info = {"sehir": "Istanbul", "ülke": "Türkiye"}
19. person.update(extra_info)
20. print("Güncellenmiş:", person)
Beklenen Çıktı:
Kopya: {'isim': 'Ali', 'yas': 31, 'meslek': 'Mühendis'}
Güncellenmiş: {'isim': 'Ali', 'yas': 31, 'meslek': 'Mühendis', 'sehir': 'Istanbul', 'ülke': 
'Türkiye'}
21. Sözlük Comprehension
Kod:
22. sayilar = [1, 2, 3, 4, 5]
23. kareler = {sayi: sayi**2 for sayi in sayilar}
24. print(kareler)
Beklenen Çıktı:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
25. İç İçe Sözlük Kullanımı
Kod:
26. ogrenci = {
27. "isim": "Ayşe",
28. "yas": 20,
29. "dersler": {
30. "Matematik": 90,
31. "Fizik": 85
32. }
33. }
34. print(ogrenci["dersler"]["Matematik"])
Beklenen Çıktı:
90




'''
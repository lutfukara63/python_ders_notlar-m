# Basit Sözlük Oluşturma

person = {"isim": "Ali", "yas": 30, "sehir": "Ankara"}
print(person)


#Sözlükte Anahtar Değer Güncelleme

person = {"isim": "Ali", "yas": 30, "sehir": "Ankara"}
person["yas"] = 31
print(person)

#Get Metodu ile Varsayılan Değer

person = {"isim": "Ali", "yas": 30}
sehir = person.get("sehir", "Bilinmiyor")
print("Şehir:", sehir)

# Nested Sözlük Oluşturma
ogrenci = {
 "isim": "Ayşe",
 "yas": 20,
 "dersler": {"Matematik": 90, "Fizik": 85}
 }
print(ogrenci)
#Sözlükte Lambda Fonksiyonları Kullanımı
operations = {
"topla": lambda a, b: a + b,
"cikar": lambda a, b: a - b
}
print("Fark:", operations["cikar"](5, 3))
#Öğrenci Notlarına Göre Durum Yazdırma

students = [
 {"isim": "Ali", "notlar": (70, 80, 90)},
 {"isim": "Ayşe", "notlar": (40, 50, 55)},
 {"isim": "Ahmet", "notlar": (80, 85, 90)}
]
for student in students:
 status = "Geçti" if sum(student["notlar"]) / len(student["notlar"]) >= 60 else "Kaldı"
 print(f"{student['isim']} - {status}")
'''
while Döngüsü
while döngüsü, bir koşul doğru olduğu sürece işlemleri tekrar eder. Koşul yanlış 
olduğunda döngü sona erer. Sonsuz döngüler, koşulun hiçbir zaman yanlış olmadığı 
durumlarda oluşur.
Kullanım Alanları
• Kullanıcıdan doğru girdi almak.
• Belirli bir işlemi, belirli bir koşul sağlanana kadar tekrarlamak.
• Algoritmik problemleri çözmek (örneğin, faktöriyel veya Fibonacci dizisi).
'''

sayi = 1
while sayi <= 10:
 print(sayi)
 sayi += 1
# Çıktı: 1 2 3 4 5 6 7 8 9 10

# Kullanıcı "exit" yazana kadar girdi al
girdi = ""
while girdi != "exit":
 girdi = input("Bir şey yazın (çıkmak için 'exit' yazın): ")
 print(f"Girdiğiniz: {girdi}")


# Çift sayıları yazdırma
sayi = 0
while sayi <= 10:
 if sayi % 2 == 0:
  print(sayi)
 sayi += 1

 # Faktöriyel Hesaplama
#Kullanıcıdan bir sayı alın ve faktöriyelini hesaplayın.
sayi = int(input("Bir sayı girin: "))
sonuc = 1
while sayi > 0:
 sonuc *= sayi
 sayi -= 1
print(f"Faktöriyel: {sonuc}")


#Fibonacci Dizisi Hesaplama
#ilk n Fibonacci sayısını yazdırın.
n = int(input("Kaç Fibonacci sayısı yazdırılsın: "))
a, b = 0, 1
sayac = 0
while sayac < n:
 print(a)
 a, b = b, a + b
 sayac += 1

 
#If(Eğer demektir)
#If else (Eğer değilse demektir)
#Elif (Başka bir durum demektir)

ad = input("Adınız nedir? ")
if ad:
 print(f"Merhaba, {ad}!")
else:
 print("Adınızı girmediniz.")



sıcaklık = 20
if sıcaklık > 30:
 print("Hava çok sıcak!")
elif sıcaklık > 15:
 print("Hava ılık.")
else:
 print("Hava soğuk.")


kullanıcı_adı = "admin"
şifre = "1234"
giriş_adı = input("Kullanıcı adınızı girin: ")
giriş_şifre = input("Şifrenizi girin: ")
if giriş_adı == kullanıcı_adı:
 if giriş_şifre == şifre:
  print("Giriş başarılı!")
 else:
  print("Şifre yanlış.")
else:
  print("Kullanıcı adı yanlış.")

a = 45
b = 67
c = 23
if a > b and a > c:
 print(f"En büyük sayı: {a}")
elif b > c:
 print(f"En büyük sayı: {b}")
else:
 print(f"En büyük sayı: {c}")  
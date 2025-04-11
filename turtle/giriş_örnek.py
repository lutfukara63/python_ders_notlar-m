#örnek Basit Bir Kare Çizimi
import turtle
# Kaplumbağa oluştur
t = turtle.Turtle()
# Çizim ayarları
t.color("blue") # Renk
t.pensize(3) # Kalem kalınlığı
t.speed(3) # Çizim hızı
# Kare çiz
for _ in range(4):
 t.forward(100) # 100 birim ileri git
 t.right(90) # 90 derece sağa dön
# Çizim tamamlandıktan sonra pencereyi kapatma
turtle.done()


#rnek 2: Bir Daire ve Çokgen Çizimi
import turtle
# Kaplumbağa oluştur
t = turtle.Turtle()
t.color("green")
t.speed(5)
# Daire çiz
t.circle(50) # Yarıçapı 50 olan daire
# Çokgen çiz (örneğin, bir beşgen)
t.penup()
t.goto(-100, 0) # Çokgen için başlangıç konumu
t.pendown()
for _ in range(5):
 t.forward(100) # 100 birim ileri
 t.right(72) # 72 derece sağa dön (360/5)
turtle.done()


#ek 3: Yıldız Çizimi
import turtle
# Kaplumbağa oluştur
t = turtle.Turtle()
t.color("orange")
t.speed(3)
# Yıldız çiz
for _ in range(5):
 t.forward(150)
 t.right(144) # Yıldız için 144 derece sağa dön
turtle.done()


#rnek 4: Kaplumbağanın İzini Kaldırmak ve Arka Plan Rengi Ayarlamak
import turtle
# Pencere ayarları
screen = turtle.Screen()
screen.bgcolor("lightblue") # Arka plan rengi
# Kaplumbağa oluştur
t = turtle.Turtle()
t.shape("turtle") # Kaplumbağa şekli
t.penup() # Kalemi kaldır (çizim yapma)
t.goto(0, 0) # Başlangıç noktası
t.pendown() # Kalemi indir
# İleri geri hareket
t.color("red")
t.forward(100)
t.backward(50)
turtle.done()

#rnek 5: Klavye ve Fare Olayları ile Etkileşim
#urtle, etkileşimli grafik uygulamaları oluşturmak için kullanılabilir.
import turtle
# Kaplumbağa ve pencere oluştur
t = turtle.Turtle()
screen = turtle.Screen()
# Hareket fonksiyonları
def ileri():
 t.forward(20)
def geri():
 t.backward(20)
def saga():
 t.right(15)
def sola():
 t.left(15)
# Klavye olaylarını bağla
screen.listen()
screen.onkey(ileri, "Up")
screen.onkey(geri, "Down")
screen.onkey(saga, "Right")
screen.onkey(sola, "Left")
turtle.done()
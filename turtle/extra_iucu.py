'''
Renk Ayarları: t.color() ile çizim ve dolgu renklerini aynı anda ayarlayabilirsiniz. 
Örneğin: 
• t.color("blue", "yellow") # Çizgi mavi, dolgu sarı
• t.begin_fill()
• t.circle(50)
• t.end_fill()
• Daha Karmaşık Grafikler: Fraktallar, spirograflar veya animasyonlar 
oluşturabilirsiniz.
• Pencere Kontrolü: turtle.Screen() sınıfını kullanarak pencere boyutunu, başlık 
metnini ve diğer özellikleri değiştirebilirsiniz.

'''

import turtle
def draw_circle(color, x, y, radius):
 turtle.penup()
 turtle.goto(x, y - radius)
 turtle.pendown()
 turtle.begin_fill()
 turtle.fillcolor(color)
 turtle.circle(radius)
 turtle.end_fill()
# Pencere ayarları
screen = turtle.Screen()
screen.bgcolor("white")
turtle.speed(5)
# Büyük daire
draw_circle("black", 0, 0, 100)
# Beyaz küçük daire
draw_circle("white", 0, 50, 50)
# Siyah küçük daire
draw_circle("black", 0, -50, 50)
# Üst beyaz nokta
draw_circle("white", 0, 50, 15)
# Alt siyah nokta
draw_circle("black", 0, -50, 15)
turtle.hideturtle()
turtle.done()
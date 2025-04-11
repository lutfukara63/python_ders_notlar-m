'''

range() fonksiyonu, bir sayı dizisi oluşturur ve genellikle for döngüsü ile kullanılır. Döngü 
sırasında bu sayı dizisinin her bir elemanı üzerinde işlem yapılır.

1. range(stop): 0'dan başlayarak belirtilen stop değerine kadar (dahil değil) bir sayı 
dizisi oluşturur.
2. for i in range(5):
3. print(i)
'''

for i in range(2, 7):
     print(i)


for i in range(1, 10, 2):
     print(i)    

for i in range(5, 0, -1):
  print("*" * i)

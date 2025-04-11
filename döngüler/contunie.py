'''
continue İfadesi
continue ifadesi, bir döngü içinde kullanıldığında, döngünün o anki iterasyonunu atlar ve 
bir sonraki iterasyona geçer. Döngü tamamen sonlanmaz; yalnızca o iterasyonun 
işlemleri gerçekleştirilmez

'''
# Çift Sayıları Atlayarak Yazdırma

for i in range(10):
 if i % 2 == 0:
   continue
print(i)       
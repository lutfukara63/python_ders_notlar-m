'''
 Modülleri İçe Aktarma (`import`) 
Modülleri içe aktarmak için `import` ifadesini kullanırız. İçe aktarılan modülün içindeki 
fonksiyonları veya değişkenleri kullanmak için modül adını kullanarak erişiriz. 


'''

import modul1 
import modul2 

# modul1'den fonksiyonları kullanma 
sonuc_topla = modul1.topla(3, 5) 
sonuc_carp = modul1.carp(3, 5) 


# modul2'den fonksiyonları kullanma 
mesaj = modul2.merhaba_de() 
kare = modul2.kare_al(4) 
print("Toplam:", sonuc_topla) 
print("Çarpım:", sonuc_carp) 
print("Mesaj:", mesaj) 
print("Kare:", kare) 
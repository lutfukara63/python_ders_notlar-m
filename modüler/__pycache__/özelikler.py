'''
Modülü Takma Adla İçe Aktarma (`import ... as ...`) 
Modül adı uzun veya karmaşık olduğunda, modülü takma bir adla (`alias`) içe 
aktarabilirsiniz.
'''
import modul1 as m1 
import modul2 as m2 
sonuc_topla = m1.topla(3, 5) 
sonuc_carp = m1.carp(3, 5) 
mesaj = m2.merhaba_de() 
kare = m2.kare_al(4) 
print("Toplam:", sonuc_topla) 
print("Çarpım:", sonuc_carp) 
print("Mesaj:", mesaj) 
print("Kare:", kare)

'''
### Özet - **`import modul`:** Tüm modülü içe aktarır. - **`from modul import fonksiyon`:** Modülden belirli bir fonksiyonu veya değişkeni içe 
aktarır. - **`import modul as takma_ad`:** Modülü takma bir adla içe aktarır. - **`__name__`:** Modülün doğrudan çalıştırılıp çalıştırılmadığını kontrol etmek için 
kullanılır. 
Python'da farklı dizinlerde bulunan modülleri içe aktarmak için birkaç yöntem vardır. Bu 
yöntemler, Python'un modül arama yolu (`sys.path`) üzerinde değişiklik yapmayı içerir. 
İşte bu yöntemlerin detaylı açıklamaları ve örnekleri:
'''
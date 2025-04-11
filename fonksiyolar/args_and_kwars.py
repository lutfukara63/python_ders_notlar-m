# *ARGS ve **KWARGS ile Esnek Parametre Kullanımı

# --------------------------------------------------------
# *args: Fonksiyona birden fazla POZİSYONEL argüman (sıralı) göndermek için kullanılır.
# Bu argümanlar fonksiyon içinde bir tuple olarak gelir.
# --------------------------------------------------------

def topla(*args):
    # args bir tuple'dır. İçindeki tüm sayıları topluyoruz.
    toplam = 0
    for sayi in args:
        toplam += sayi
    return toplam

# Örnek kullanımlar:
print(topla(1, 2, 3))          # Çıktı: 6
print(topla(4, 5, 6, 7, 8))    # Çıktı: 30


# --------------------------------------------------------
# **kwargs: Fonksiyona birden fazla ANAHTAR=DEĞER (keyword argument) çifti göndermek için kullanılır.
# Bu argümanlar fonksiyon içinde bir sözlük (dict) olarak gelir.
# --------------------------------------------------------

def bilgiler(**kwargs):
    # kwargs bir sözlük olduğu için .items() ile anahtar-değer çiftlerine ulaşabiliriz
    for anahtar, deger in kwargs.items():
        print(f"{anahtar} : {deger}")

# Örnek kullanım:
bilgiler(ad="Ahmet", yas=25, sehir="İstanbul")
# Çıktı:
# ad : Ahmet
# yas : 25
# sehir : İstanbul


# --------------------------------------------------------
# *args ve **kwargs birlikte kullanılabilir!
# Sıralama önemli: önce *args, sonra **kwargs gelmeli.
# --------------------------------------------------------

def karisik_fonksiyon(isim, *args, **kwargs):
    print(f"Merhaba, {isim}")
    print("Ekstra sayılar:", args)         # args → tuple
    print("Diğer bilgiler:", kwargs)       # kwargs → dict

# Örnek kullanım:
karisik_fonksiyon(
    "Zeynep",        # isim → normal parametre
    10, 20, 30,      # args → tuple
    sehir="Ankara", yas=22                # kwargs → dict
)

# Çıktı:
# Merhaba, Zeynep
# Ekstra sayılar: (10, 20, 30)
# Diğer bilgiler: {'sehir': 'Ankara', 'yas': 22}


# --------------------------------------------------------
# BONUS: *args ve **kwargs kullanarak fonksiyonu daha esnek hale getirmek
# --------------------------------------------------------

def siparis_ozeti(urun_adi, *ekstralar, **bilgiler):
    print(f"Ürün: {urun_adi}")
    if ekstralar:
        print("Ekstra istekler:")
        for ekstra in ekstralar:
            print(f" - {ekstra}")
    if bilgiler:
        print("Müşteri Bilgileri:")
        for key, value in bilgiler.items():
            print(f" {key} : {value}")

# Örnek kullanım:
siparis_ozeti(
    "Pizza", 
    "Ekstra peynir", "Zeytin", 
    isim="Ali", adres="İzmir", odeme="Nakit"
)

# Çıktı:
# Ürün: Pizza
# Ekstra istekler:
#  - Ekstra peynir
#  - Zeytin
# Müşteri Bilgileri:
#  isim : Ali
#  adres : İzmir
#  odeme : Nakit

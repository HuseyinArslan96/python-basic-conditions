#  1. Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
#     Ehliyet alma yaşı en az 18, eğitim durumu da lise ya da üniversite olmalıdır.
adSoyad = input("Ad-soyad: ")
yas = int(input("Yaş: "))
egitim = input("Eğitim durumu: ")
if (yas >= 18):
    if (egitim.lower() == "lise" or egitim.lower() == "üniversite"):
        print(f"{adSoyad} ehliyet alabilir.")
    else:
        print(f"{adSoyad} ehliyet alamaz; eğitim durumu uygun değil.")
else:
    print(f"{adSoyad} ehliyet alamaz; yaş uygun değil.")
#  2. Bir öğrencinin iki yazılı, bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
    # 0-24 => 0
    # 25-44 => 1
    # 45-54 => 2
    # 55-69 => 3
    # 70-84 => 4
    # 85-100 => 5
yazili1 = int(input("1. sınav notunu giriniz: "))
yazili2 = int(input("2. sınav notunu giriniz: "))
sozlu = int(input("Sözlü notunu giriniz: "))
ortalama = (yazili1 + yazili2 + sozlu) / 3
ortalama = round(ortalama, 2)
if (ortalama >= 0) and (ortalama <= 24):
    print(f"Ortalamanız: {ortalama}; 0 aldınız.")
elif ortalama > 24 and ortalama <= 44:
    print(f"Ortalamanız: {ortalama}; 1 aldınız.")
elif ortalama > 44 and ortalama <= 54:
    print(f"Ortalamanız: {ortalama}; 2 aldınız.")
elif ortalama > 54 and ortalama <= 69:
    print(f"Ortalamanız: {ortalama}; 3 aldınız.")
elif ortalama > 69 and ortalama <= 84:
    print(f"Ortalamanız: {ortalama}; 4 aldınız.")
elif ortalama > 84 and ortalama <= 100:
    print(f"Ortalamanız: {ortalama}; 5 aldınız.")
else:
    print("Geçersiz bilgi girdiniz.")
#%%
#  3. Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#     1. Bakım => 1. yıl
#     2. Bakım => 2. yıl
#     3. Bakım => 3. yıl
#     * Süre hesabını alınan gün, ay ve yıl bazlı hesaplayınız.
#     ** Datetime modülünü kullanmanız gerekiyor.
import datetime
from datetime import date 
tarih = input('Aracınız hangi tarihte trafiğe çıktı (2010/10/10): ')
tarih = tarih.split('/') # split metoduyla aldığımız tarih bilgisini yıl, ay, gün biçiminde parçalara böldük.
trafigeCikis = datetime.date(int(tarih[0]), int(tarih[1]), int(tarih[2]))
bugun = date.today()
fark = bugun - trafigeCikis
days = fark.days
print(f"Bugünün tarihi: {bugun}; fark: {fark}")
if days <= 365:
    print("1. servis aralığı")
elif days >= 365 and days <= 365*2:
    print("2. servis aralığı")
elif days >= 365*2 and days <= 365*3:
    print("3. servis aralığı")
elif days >= 365*3 and days <= 365*4:
    print("4. servis aralığı")
else:
    print("Geçersiz tarih bilgisi")
#%%
from datetime import date
from datetime import datetime, timedelta  
bugun = date.today()
print(f"Bu günün tarihi: {bugun}") #günün tarihini ekrana yazdırdık.
a = int(input("Lütfen yılı girin: ")) # a isimli bir değişken tanımlayıp, kullanıcıdan integer olarak doğduğu yılı girmesini istedik.
b = int(input("Lütfen ayı girin: "))  # b isimli bir değişken tanımlayıp, kullanıcıdan integer olarak doğduğu ayı girmesini istedik.
c = int(input("Lütfen günü girin: ")) # c isimli bir değişken tanımlayıp, kullanıcıdan integer olarak doğduğu günü girmesini istedik.
trafikCikis = date(a, b, c) # trafikCikis isimli değişkene date fonksiyonunu atadık.
bakimZamani = bugun - trafikCikis   # bakimZamani adlı değişken oluşturduk ve bugun adlı değişkenden trafikCikis adlı değişkeni çıkardık.
print(bakimZamani) # son olarak da bakimZamani değişkeninin sonucunu ekrana yazdırdık.
if (bakimZamani <= timedelta(days = 365)):
    print("Aracınızın birinci bakım zamanı gelmiştir.")
if (bakimZamani >= timedelta(days = 365)) and (bakimZamani <= timedelta(days = 365*2)):
    print("Aracınızın ikinci bakım zamanı gelmiştir.")
if (bakimZamani >= timedelta(days = 730)) and (bakimZamani <= timedelta(days = 365*3)):
    print("Aracınızın üçüncü bakım zamanı gelmiştir.")
if (bakimZamani >= timedelta(days = 1460)) and (bakimZamani <= timedelta(days = 365*4)):
    print("Aracınızın dördüncü bakım zamanı gelmiştir.")
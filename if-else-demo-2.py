# 1. Girilen bir sayının 0 ile 100 arasında olup olmadığını kontrol ediniz.
sayi = int(input("Sayı giriniz: "))
if sayi >= 0 and sayi <= 100:
    print(f"Sayı: {sayi}; girdiğiniz sayı 0 ile 100 arasındadır.")
else:
    print (f"Sayı: {sayi}; girdiğiniz sayı 0 ile 100 arasında değildir.")
# 2. Girilen bir sayının pozitif ve çift sayı olup olmadığını kontrol ediniz.
sayi = int(input("Sayı giriniz: "))
if (sayi > 0):
    if (sayi % 2 == 0):
        print("Sayı pozitif ve çifttir.")
    else:
        print("Sayı pozitif ve tektir.")
elif (sayi < 0) and (sayi % 2 == 0):
    print("Sayı negatif ve çifttir.")
elif (sayi < 0) and (sayi % 2 != 0):
    print("Sayı negatif ve tektir.")
# 3. E-posta ve parola bilgileriyle giriş kontrolü yapınız.
mail = "huseyin@gmail.com"
parola = "abc123"
girilenMail = input("E-posta: ")
girilenParola = input("Parola: ")
if (girilenMail.strip() == mail):
    if (girilenParola.lower() == parola):
        print("E-posta ve parola bilgileri doğru.")
    else:
        print("Girilen parola bilgisi yanlış.")
elif (girilenMail.strip() != mail) and (girilenParola.lower() != parola):
    print("Girilen e-posta ve parola bilgileri yanlış.")
else:
    print("Girilen e-posta bilgisi yanlış.")
# 4. Girilen üç sayıyı büyüklük açısından karşılaştırınız.
a = int(input("A sayısı: "))
b = int(input("B sayısı: "))
c = int(input("C sayısı: "))
if (a > b) and (a > c):
    print("A en büyük sayıdır.")
elif (b > a) and (b > c):
    print("B en büyük sayıdır.")
elif (c > a) and (c > b):
    print("C en büyük sayıdır")
# 5. Kullanıcıdan iki vize (%60) ve bir final (%40) notunu alıp ortalamasını hesaplayın.
#    Eğer ortalama 50 ve üstündeyse "geçti", altındaysa "kaldı" yazdırın.
#    a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b) Finalden 70 alındığında ortalamanın önemi yoktur.
vize1 = int(input("1. vize: "))
vize2 = int(input("2. vize: "))
final = int(input("Final: "))
ortalama = ((vize1 + vize2)/2*0.6) + (final*0.4)
if ortalama >= 50: #durum1
    if final >= 50:
        print("Dersi geçti.")
    else:
        print("Dersi geçemedi; final notu yetersiz.")
elif ortalama < 50 and final >= 70: #durum2
    print("Final notuyla dersi geçti.")
else:
    print("Dersi geçemedi; ortalama yetersiz.")
# durum2 için alternatif kod:
if ortalama >= 50:
    print(f"Ortalama: {ortalama}; dersi geçti.")
else:
    if final >= 70:
        print(f"Ortalama ({ortalama}) yetersiz ancak finalden en az 70 aldığınız için dersi geçtiniz.")
    else:
        print(f"Ortalama ({ortalama}) ve final notu ({final}) yetersiz.") 
# 6. Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#     Formül: Kilo/boy uzunluğunun karesi
#     Aşağıdaki tabloya göre kişi hangi gruba girmektedir?
#     0 - 18.4 => Zayıf
#     18.5 - 24.9 => Normal
#     25.0 - 29.9 => Kilolu
#     30.0 - 34.9 => Şişman (Obez)
adSoyad = input("Ad-soyad: ")
boy = float(input("Boy: "))
kilo = float(input("Kilo: "))
indeks = kilo / (boy ** 2)
if indeks >= 0 and indeks < 18.5:
    print(f"Ad-soyad: {adSoyad}; boy: {boy}; kilo {kilo}; vücut kitle indeksi: {round(indeks, 1)}; durum: zayıf")
elif indeks >= 18.5 and indeks < 25:
    print(f"Ad-soyad: {adSoyad}; boy: {boy}; kilo {kilo}; vücut kitle indeksi: {round(indeks, 1)}; durum: normal")
elif indeks >= 25 and indeks < 30:
    print(f"Ad-soyad: {adSoyad}; boy: {boy}; kilo {kilo}; vücut kitle indeksi: {round(indeks, 1)}; durum: kilolu")
elif indeks >= 30 and indeks < 35:
    print(f"Ad-soyad: {adSoyad}; boy: {boy}; kilo {kilo}; vücut kitle indeksi: {round(indeks, 1)}; durum: şişman")
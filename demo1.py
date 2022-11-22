# # 1. Girilen bir sayının 0 ile 100 arasında olup olmadığını kontrol ediniz.
sayi = int(input("Sayı giriniz: "))
if (sayi > 0) and (sayi < 100):
    print("Sayı 0 ile 100 arasındadır.")
else:
    print("Sayı 0 ile 100 arasında değildir.")
# # 2. Girilen bir sayının pozitif ve çift sayı olup olmadığını kontrol ediniz.
sayi = int(input("Sayı giriniz: "))
if (sayi > 0) and (sayi % 2 == 0):
    print("Sayı pozitif ve çifttir.")
elif (sayi < 0) and (sayi % 2 == 0):
    print("Sayı negatif ve çifttir.")
elif (sayi > 0) and (sayi % 2 == 1):
    print("Sayı pozitif ve tektir.")
elif (sayi < 0) and (sayi % 2 == 1):
    print("Sayı negatif ve tektir.")
# # 3. E-posta ve parola bilgileriyle giriş kontrolü yapınız.
eposta = "huseyin@gmail.com"
parola = "abc123"
girilenEposta = input("E-posta: ")
girilenParola = input("Parola: ")
if (eposta == girilenEposta.strip()) and (parola == girilenParola.lower()):
    print("Girilen e-posta ve parola bilgileri doğrudur.")
elif (eposta != girilenEposta.strip()) and (parola != girilenParola.lower()):
    print("Girilen bilgiler yanlıştır.")
elif (eposta != girilenEposta.strip()) and (parola == girilenParola.lower()):
    print("E-posta yanlıştır.")
elif (eposta == girilenEposta.strip()) and (parola != girilenParola.lower()):
    print("Parola yanlıştır.")
# # 4. Girilen üç sayıyı büyüklük açısından karşılaştırınız.
sayi1 = float(input("Sayı giriniz: "))
sayi2 = float(input("Sayı giriniz: "))
sayi3 = float(input("Sayı giriniz: "))
sira = sayi1, sayi2, sayi3
yeniSira = sorted(sira, reverse = True)
if sayi1 > sayi2 > sayi3:
    print("Girilen sayılar büyükten küçüğe sıralanmıştır.")
else:
    print(f"Girilen sayılar büyükten küçüğe sıralanmamıştır. Sıralama: {yeniSira}")
liste = []
adet = int(input('Kaç Sayı Girilecek: '))
for n in range(adet):
    sayi = int(input('Sayı giriniz: '))
    liste.append(sayi)
enBuyuk = max(liste)
print(f"En büyük sayı: {enBuyuk}")
# 5. Kullanıcıdan iki vize (%60) ve bir final (%40) notunu alıp ortalamasını hesaplayın.
#    Eğer ortalama 50 ve üstündeyse "geçti", altındaysa "kaldı" yazdırın.
#    a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b) Finalden 70 alındığında ortalamanın önemi yoktur.
vize1 = int(input("İlk vize notu: "))
vize2 = int(input("İkinci vize notu: "))
final = int(input("Final notu: "))
ortalama = ((vize1 + vize2)*0.6/2) + (final*0.4)
if (ortalama >= 50 and final >= 50) or (ortalama <= 50 and final >= 70):
    print(f"Ortalama: {ortalama}; geçme durumu başarılı.")
else:
    print(f"Ortalama: {ortalama}; geçme durumu başarısız.")
# 6. Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
    # Formül: Kilo/boy uzunluğunun karesi
    # Aşağıdaki tabloya göre kişi hangi gruba girmektedir?
    # 0 - 18.4 => Zayıf
    # 18.5 - 24.9 => Normal
    # 25.0 - 29.9 => Kilolu
    # 30.0 - 34.9 => Şişman (Obez)
adSoyad = input("Ad-soyad: ")
kilo = float(input("Kilo: "))
boy = float(input("Boy: "))
formul = kilo/(boy ** 2)
zayif = formul > 0 and formul <= 18.4
normal = formul > 18.4 and formul <= 24.9
kilolu = formul > 24.9 and formul <= 29.9
sisman = formul > 29.9
if zayif:
    print(f"Ad-soyad: {adSoyad}, kilo: {kilo}, boy: {boy}, indeks: {round(formul, 2)}; sonuç: zayıf")
if normal:
    print(f"Ad-soyad: {adSoyad}, kilo: {kilo}, boy: {boy}, indeks: {round(formul, 2)}; sonuç: normal")
if kilolu:
    print(f"Ad-soyad: {adSoyad}, kilo: {kilo}, boy: {boy}, indeks: {round(formul, 2)}; sonuç: kilolu")
if sisman:
    print(f"Ad-soyad: {adSoyad}, kilo: {kilo}, boy: {boy}, indeks: {round(formul, 2)}; sonuç: şişman")
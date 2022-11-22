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
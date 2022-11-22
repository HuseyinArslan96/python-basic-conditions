x = int(input("x: "))
y = int(input("y: "))
if x > y:
    print("x, y'den büyüktür.")
elif x >= y:
    print("x, y'ye eşit.")
else:
    print("y, x'den büyüktür.")
sayi = int(input("Sayı giriniz: "))
if sayi > 0:
    print("Sayı pozitif.")
elif sayi < 0:
    print("Sayı negatif.")
else:
    print("Sayı nötr.")
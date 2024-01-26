liste = [
    ["A", 10, 20, 30],
    ["B", 15, 25, 35],
    ["C", 70, 75, 80],
    ["D", 30, 50, 70],
    [210444029, 100, 100, 95]
]

for satir in liste:
    ogrenci_no = satir[0]
    notlar = satir[1:]
    
    ortalama = sum(notlar) / len(notlar)
    ortalamaa = round(ortalama, 1)
    
    print(ogrenci_no, "=", ortalamaa)

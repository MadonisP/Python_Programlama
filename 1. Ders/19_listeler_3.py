liste = ["mert", "süha", "igaç"]

liste.sort()
print(liste)

liste.reverse()
print(liste)

def fonksiyon(n):
  return abs(n - 50)

sayi_listesi = [100, 50, 65, 82, 23]
sayi_listesi.sort(key=fonksiyon)
print(sayi_listesi)

#7  ile bölünen sayıların toplamı ve ortalaması 
print("7'ye b�l�nen say�lar�n toplam� ve ortalamas� ")
toplam=0
for c in range(0,101):
    if c%7==0:
        toplam=toplam+c    
print(toplam)
ort=toplam/14
print(ort)
#ALAN BULMA 
print("üçgen için 1. \n dörtgenler için 2 \n daire için 3 ")
y=int(input("şekil seçiniz"))
if y==1:
    h=int(input("yükseklik giriniz"))
    t=int(input("taban uzunluğu giriniz"))
    u=h*t/2
    print(u)
if y==2:
    a=int(input("kenar uzunluğu giriniz"))
    b=int(input("kenar uzunluğu giriniz "))
    u=a*b
    print(u)
if y==3:
    r=int(input("yarı çap girniz"))
    u=3.14*r*r
    print(u)
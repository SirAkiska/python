#vize final ortalaması
v=int(input("vize notunuz "))
f= int(input("final notunuz"))
vizenot=v*40/100
finnot=f*60/100
top=finnot+vizenot
if 85<top<101:
    print(" AA  NOTUNU ALDINIZ VE ORTALAMANIZ {}".format(top))
if 75<top<86:
     print(" BB  NOTUNU ALDINIZ VE ORTALAMANIZ {}".format(top))
if 65<top<76:
     print("CC  NOTUNU ALDINIZ VE ORTALAMANIZ {}".format(top))
if 55<top<66:
     print(" DD  NOTUNU ALDINIZ VE ORTALAMANIZ {}".format(top))
if 45<top<56:
     print(" EE  NOTUNU ALDINIZ VE ORTALAMANIZ {}".format(top))
if 25<top<46:
     print(" FF  NOTUNU ALDINIZ VE ORTALAMANIZ {}".format(top))
if 00<top<26:
     print(" DEĞERLENDİRİLMEDİ  NOTUNU ALDINIZ VE ORTALAMANIZ {}".format(top))
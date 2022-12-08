#10
from math import *
print("Ajateisendus")
v=float(input("sisesta aja minutites: "))
t=int(v//60)
sec=int(v%60)
print(f"minutes {t}:sekundid {sec}")

#9
from math import *
print("Rulluisutajad")
print("Rulluisutaja keskmine kiirus on 29,9km/h")
m=24/60
t=m*29.9
t=round(t,2)
print(f"Vastus: {t}km")
print()


#8
from math import* 
print("Kütusekulu arvutamine")
l=float(input("Kasutaja sisestab tangitud kütuse liitrid: "))
km=float(input("Kasutaja sisestab läbitud kilomeetrid: "))
p=l/km*100
print (f"Vastus: {p}l/100km")
print()

#7
from math import * 
print("Pitsa Võtsite 3 sõbraga suure pitsa hinnaga 12,90€ te jätate teenindajale 10% jootraha")
s=10*12.90/100
s=round(s)
d=(12.90+s)
p=d/3
p=round(p,1)
print (f"Iga sõber peab maksma: {p}€")
print()
#6 
from random import *
print("Arvutame kolmnurga ümbermõõdu")
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
print(f"Külg a={a}\nKülg b={b}\nKülg c={c}")
print(f"Kolmnurga ümbermõõt = {a+b+c}")
print()

#5
print(" @..@")
print("(----)")
print("(\__/)")
print("^^"'""'"^^")
print()



#4
from math import* 
print("programm, mis arvutab keskmise aritmeetilise")
a=int(input("1arv: "))
b=int(input("2arv: "))
c=int(input("3arv: "))
d=int(input("4arv: "))
e=int(input("5arv: "))
S=((a+b+c+d+e)/5)
print(f"Vastus: {S}")
print()





#3
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg/teepikkus
print()
print("Sinu kiirus oli " + str(round(kiirus)) + " km/h")
print()



#2
from math import * 
print("Ristkülikukujlise matüki deagonaal")
N=float(input("Siseta ristküliku 1. külje pikkus -> " ))
M=float(input("Siseta ristküliku 2. külje pikkus ->" ))
d=sqrt(N**2+M**2)
print (f"Maatüki diagonaal on {d} m**2")
print()



#1
from math import *
print("Puu läbimõdu arvutamine")
C=float(input("Puu ümbermõõt: "))
d=2*(C/(2*pi))
print(f"Vastus:\nPuu läbimõõduga {C} ümbermõõt võrdub {d}")
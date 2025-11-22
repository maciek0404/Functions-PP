import math
a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
c = int(input("Podaj bok c: "))

def triangle_area(a,b,c):
    obwod = 0.5 * (a+b+c)
    pole = math.sqrt((obwod * (obwod - a) * (obwod - b) * (obwod - c)))
    return pole

    

heron = triangle_area(a,b,c)
print (heron)



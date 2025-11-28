def f(number, even):
    suma = 0
    for d in str(abs(number)):
        cyfra = int(d)
        if even and cyfra % 2 == 0:       
            suma += cyfra
        if not even and cyfra % 2 == 1:   
            suma += cyfra
    return suma
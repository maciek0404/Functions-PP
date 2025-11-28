def f(number):
    digits = str(number)
    suma = 0
    for d in set(digits):
        count = digits.count(d)
        if count > 1:
            suma += int(d) * count
    return suma
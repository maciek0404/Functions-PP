def f(product_code):
    suma = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    return (suma % 7) == int(product_code[3])
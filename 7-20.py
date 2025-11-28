def f(n):
    count = 0
    number = 2
    while True:
        # sprawdzamy, czy number jest pierwszą
        is_prime = True
        i = 2
        while i * i <= number:
            if number % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            count += 1
            if count == n:
                return number

        number += 1
print(f(1))
print(f(5))
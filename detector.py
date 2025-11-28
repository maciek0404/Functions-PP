def f(detector):
    count = 0
    for c in detector:
        if c == '+':
            count += 1
        elif c == '-':
            count -= 1
        if count >= 3:
            return True
    return False
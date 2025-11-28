def f(binary_number):
    if not binary_number:
        return False
    
    for symbol in binary_number:
        if symbol not in ('0', '1'):
            return False
        
    return True
    
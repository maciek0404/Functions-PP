def f(expression):
    total = int(expression[0])       
    i = 1

    while i < len(expression):
        op = expression[i]            
        num = int(expression[i+1])    

        if op == '+':
            total += num
        else:  
            total -= num

        i += 2

    return total

print(f("2+3"))
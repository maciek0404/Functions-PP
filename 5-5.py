import range

x = int(input('Podaj zakres x: '))
y = int(input('Podaj zakres y: '))

if x > y:
        x, y = y, x
        print(f"Uwaga: Limity zakresu zostały automatycznie zamienione na <{x}, {y}>.")

number = int(input('Podaj liczbę: '))

result = range.check_range(number,x,y)

print(result)
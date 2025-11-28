def month1(n):
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
        }
    return months.get(n, "Niepoprawny numer miesiąca")
if __name__ == "__main__":
        print(f"The name of 9 month is: {month1(9)}")



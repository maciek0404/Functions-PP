def hide(card_number):
    if len(card_number) < 16 or not card_number.isdigit():
        return "Nie poprawny numer karty"
    else:
        first_two = card_number[:2]
        last_four = card_number[-4:]
        masked = '*' * 10
        return first_two + masked + last_four
    
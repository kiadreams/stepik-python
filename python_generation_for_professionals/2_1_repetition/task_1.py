def hide_card(card_number: str):
    return '*' * 12 + card_number.replace(' ', '')[12:]


print(hide_card('905 678123 45612 56'))
print('1235'[3:])
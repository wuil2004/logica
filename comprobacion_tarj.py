def luhn_check(card_num):
    digits = [int(x) for x in str(card_num)]

    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total_sum = sum(digits)
    return total_sum % 10 == 0

card_num = 499273987163
is_valid = luhn_check(card_num)
print(f"El número de tarjeta {card_num} es {'válido' if is_valid else 'no es válido'}")


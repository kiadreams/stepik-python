def check_password(password):
    digits = 0
    upper_case = 0
    is_symbol = False

    for s in "!@#$%*":
        if s in password:
            is_symbol = True

    for w in password:
        if w.isupper():
            upper_case += 1
        elif w.isdigit():
            digits += 1

    if all([upper_case, is_symbol, digits > 2, len(password) > 9]):
        print("Perfect password")
    else:
        print("Easy peasy")

with open('18_1_exam/ledger.txt', encoding='utf-8') as f:
    revenue = sum([int(line[1:]) for line in list(f)])
    print(f'${revenue}')
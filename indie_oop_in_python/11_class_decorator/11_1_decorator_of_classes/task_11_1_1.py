def init_card(cls):
    cls.total = 0
    cls.type_card = 'debit'
    return cls


@init_card
class BankAccount:
    pass


print(BankAccount.total)
print(BankAccount.type_card)
def init_card(total=0, type_card='debit'):

    def inner(cls):
        cls.total = total
        cls.type_card = type_card
        return cls

    return inner


@init_card(total=100, type_card="credit")
class BankAccount:
    pass


@init_card(total=5005)
class TimeDeposit:
    pass


print(TimeDeposit.total, TimeDeposit.type_card)
print(BankAccount.total, BankAccount.type_card)

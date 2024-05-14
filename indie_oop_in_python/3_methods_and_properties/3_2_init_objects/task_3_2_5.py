class Zebra:

    def __init__(self):
        self.is_black = False

    def which_stripe(self):
        print(("Полоска белая", "Полоска черная")[self.is_black])
        self.is_black = not self.is_black

    def run_away(self):
        print("Oh, Sugar Honey Ice Tea")


zebra = Zebra()
zebra.run_away()
zebra.which_stripe()
zebra.which_stripe()
zebra.which_stripe()
zebra.which_stripe()
zebra.which_stripe()
zebra.run_away()

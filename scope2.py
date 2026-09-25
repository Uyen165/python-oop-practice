def discount_factory(discount_rate):
    #discount_rate là Free Variable
    def apply_discount(price):
        return price * (1 - discount_rate)
    return apply_discount
ten_percent_off = discount_factory(0.10)
print(ten_percent_off(100)) #price = 100, discount_rate = 0.10 -> Output 90.0
print(ten_percent_off.__code__.co_freevars) #('discount_rate',)
print(ten_percent_off.__closure__) #(<cell at 0x00000288EAF6AB90: float object at 0x00000288EAE9A930>,)
print(ten_percent_off.__closure__[0].cell_contents) #0.10
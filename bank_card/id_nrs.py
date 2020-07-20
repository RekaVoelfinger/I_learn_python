import random
import string


class IdNrs:
    mii = "4"
    inn = "00000"

    def __init__(self, length, id_type):
        self.length = length
        self.digits = ""
        self.id_type = id_type

    def generate_numeric_id(self):
        for _ in range(self.length):
            self.digits += random.choice(string.digits)
        return self.digits

    def generate_card_nr(self):
        self.digits = self.mii + self.inn + self.generate_numeric_id() + "7"
        self.id_type = "card number"
        return self.digits

    def generate_pin(self):
        return self.generate_numeric_id()

    def to_string(self):
        return f"It is {self.id_type}, has {self.length} digits and they are {self.digits}"

"""
acc_nr = IdNrs(9, "account number")
acc_nr.generate_card_nr()
card_nr = acc_nr
print(card_nr.digits)
print(IdNrs.to_string(card_nr))
pin = IdNrs(4, "PIN")
pin.generate_pin()
print(IdNrs.to_string(pin))
"""

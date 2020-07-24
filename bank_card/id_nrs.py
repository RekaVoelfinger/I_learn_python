import random
import string


class IdNrs:

    def __init__(self, length, id_type):
        self.length = length
        self.digits = "400000"
        self.num_digits = []
        self.checksum = ""
        self.id_type = id_type

    def random_numeric_id(self):
        for _ in range(self.length):
            self.digits += random.choice(string.digits)
        return self.digits

    def string2number(self):
        i = 0
        for i in range(length(self.digits)):
            self.num_digits.append(int(self.digits[i]))

    def duble_even_digits(self):
        i = 0
        for i in range(length(self.num_digits)):
            self.num_digits[i] += self.num_digits[i]
            i += 2

    def calculate_checksum(self):
        self.checksum = 10 - sum(self.num_digits)%10

    def luhn_algorithm(self):
        self.random_numeric_id()
        self.string2number()
        self.duble_even_digits()
        self.calculate_checksum()

    def generate_card_nr(self):
        self.luhn_algorithm()
        self.digits = self.mii + self.inn + self.random_numeric_id() + self.checksum
        self.id_type = "card number"
        return self.digits

    def generate_pin(self):
        return self.random_numeric_id()

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

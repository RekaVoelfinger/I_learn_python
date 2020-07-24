import id_nrs

class Account:
    def __init__(self):
        self.bank_card_nr = ""
        self.pin_nr = ""
        self.stored_data = {}
        self.balance = dict()
        self.balance[self.bank_card_nr] = 99

    def show_main_menu(self):
        menu_string = "\n1. Create an account\n2. Log into account\n0. Exit\n>"
        action = input(menu_string)
        if action == "1":
            self.create_account()
            self.print_account_data()
        if action == "2":
            self.login()
        if action == "0":
            self.stop()
        else:
            print("Choose from the given options!")

    def start(self):
        while True:
            self.show_main_menu()

    def stop(self):
        print("Bye!")
        exit()

    def create_account(self):
        self.create_card()
        self.create_pin()
        self.create_balance()
        self.store_account_data()

    def create_card(self):
        account_nr = id_nrs.IdNrs(9, "account number")
        self.bank_card_nr = account_nr.generate_card_nr()

    def create_pin(self):
        pin_nr = id_nrs.IdNrs(4, "PIN")
        self.pin_nr = pin_nr.generate_pin()

    def create_balance(self):
        self.balance[self.bank_card_nr] = 99

    def store_account_data(self):
        self.stored_data[self.bank_card_nr] = self.pin_nr
        print(self.stored_data)

    def print_account_data(self):
        print(f"Your card has been created\nYour card number:\n{self.bank_card_nr}\nYour card PIN:\n{self.pin_nr}")

    def login(self):
        login_data = input("Enter your card number:\n")
        if self.check_login_data(login_data):
            pin_data = input("Enter your PIN:\n")
            self.check_pin_data(login_data, pin_data)
        else:
            print("Give a valid card number")

    def check_login_data(self, login_data):
        if login_data in self.stored_data.keys():
            return True
        else:
            print("Wrong card number or PIN!")

    def check_pin_data(self, login_data, pin_data):
        if self.stored_data[login_data] == pin_data:
            print("You have successfully logged in!\n")
            self.bank_card_nr = login_data
            while True:
                self.logged_in_menu()
        else:
            print("Wrong card number or PIN!")

    def logged_in_menu(self):
        menu_string = f"1. Balance\n2. Log out\n0. Exit\n>"
        action = input(menu_string)
        if action == "1":
            self.get_balance(self.bank_card_nr)
        if action == "2":
            self.logout()
        if action == "0":
            self.stop()

    def get_balance(self, card_nr):
        print(f"Balance: {self.balance[card_nr]}\n")

    def logout(self):
        self.bank_card_nr = ""
        print("You have successfully logged out!")
        self.show_main_menu()

    def _get_bank_card_nr(self):
        return f" Bank card nummer: {self.bank_card_nr}"


account = Account()
account.start()

if __name__ == "main":
    account = Account()
    account.start()

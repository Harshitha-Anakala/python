class bank_details:
    def __init__(self, a, b, c, d, e, f):
        self.recepient_name = a
        self.acc_num = b
        self.mobile_no = c
        self.bank_balance = d
        self.branch = e
        self.address = f

    def account(self):
        return f"He has an account"
obj = bank_details("Riku", 84522233, 632589741, 7885, "Ramnagar branch", "Anantapur, Andhra Pradesh")
print(obj.account())
def display_bank_details(self):
    return (f"Name: {self.recepient_name}\n" f"Account Number: {self.acc_num}\n"f"Mobile Number: {self.mobile_no}\n" f"Bank Balance: {self.bank_balance}\n" f"Branch: {self.branch}\n"
            f"Address: {self.address}")
bank_details.display_bank_details = display_bank_details
print(obj.display_bank_details())

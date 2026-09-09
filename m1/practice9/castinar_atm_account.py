class Account:

    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance

    def check_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True

        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True

        return False





"""

######### Learning Signature #########

Programmed by: THEO PAULO CASTINAR

Date Submitted: September 9, 2026

Program Description: This program creates an Account class that can check the balance deposit money and withdraw money.

Reflection: I learned how to add a withdraw method that checks the amount first before changing the account balance.

AI Usage

[ ] No AI Assistance - Completed independently without AI.

[X] AI as Support Tool - Used AI for explanations syntax or minor corrections.

[ ] AI as Collaborative Partner - Used AI to design structure or co-create significant code.

"""
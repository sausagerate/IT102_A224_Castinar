from datetime import datetime


def deposit_money(account, amount):

    if amount <= 0:
        return False

    success = account.deposit(amount)

    if success:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file = open("transactions.txt", "a", encoding="utf-8")

        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Account: {account.account_name}\n")
        file.write("Transaction: Deposit\n")
        file.write(f"Amount: ₱{amount:.2f}\n\n")

        file.close()

        return True

    return False


"""

######### Learning Signature #########

Programmed by: THEO PAULO CASTINAR

Date Submitted: September 9 2026

Program Description: This program processes a deposit using the Account object and saves the transaction with a timestamp.

Reflection: I learned how to pass an Account object and amount into a function then save the transaction after the deposit is successful.

AI Usage

[ ] No AI Assistance - Completed independently without AI.

[X] AI as Support Tool - Used AI for explanations syntax or minor corrections.

[ ] AI as Collaborative Partner - Used AI to design structure or co-create significant code.

"""
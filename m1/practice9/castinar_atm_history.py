def view_history():
    try:
        file = open("transactions.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        return lines

    except FileNotFoundError:
        return []


"""

######### Learning Signature #########

Programmed by: THEO PAULO CASTINAR

Date Submitted: September 9 2026

Program Description: This program reads the ATM transaction history from a text file and returns the data to the main program.

Reflection: I learned how to return transaction data from a module and handle a missing file without crashing the program.

AI Usage

[ ] No AI Assistance - Completed independently without AI.

[X] AI as Support Tool - Used AI for explanations syntax or minor corrections.

[ ] AI as Collaborative Partner - Used AI to design structure or co-create significant code.

"""
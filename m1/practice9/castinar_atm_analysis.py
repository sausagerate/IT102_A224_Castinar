def analyze_transactions():

    try:
        file = open("transactions.txt", "r", encoding="utf-8")
        lines = file.readlines()
        file.close()

    except FileNotFoundError:
        return {
            "total_transactions": 0,
            "deposits": 0,
            "withdrawals": 0,
            "total_deposited": 0.00,
            "total_withdrawn": 0.00,
            "average_transaction": 0.00,
            "latest_transaction": "None",
            "latest_timestamp": "None",
            "largest_transaction": 0.00
        }


    transactions = []
    current = {}


    for line in lines:

        line = line.strip()

        if line == "":
            continue


        if line.startswith("Timestamp:"):
            current["timestamp"] = line.replace("Timestamp:", "").strip()


        elif line.startswith("Account:"):
            current["account"] = line.replace("Account:", "").strip()


        elif line.startswith("Transaction:"):
            current["type"] = line.replace("Transaction:", "").strip()


        elif line.startswith("Amount:"):
            amount_text = line.replace("Amount:", "").strip()
            amount_text = amount_text.replace("₱", "").replace(",", "")

            try:
                current["amount"] = float(amount_text)

            except ValueError:
                current["amount"] = 0.00


            if (
                "timestamp" in current
                and "account" in current
                and "type" in current
                and "amount" in current
            ):
                transactions.append(current)
                current = {}


    total_transactions = len(transactions)

    deposits = 0
    withdrawals = 0

    total_deposited = 0.00
    total_withdrawn = 0.00


    for transaction in transactions:

        if transaction["type"] == "Deposit":
            deposits += 1
            total_deposited += transaction["amount"]

        elif transaction["type"] == "Withdraw":
            withdrawals += 1
            total_withdrawn += transaction["amount"]


    if total_transactions > 0:

        total_amount = 0.00

        for transaction in transactions:
            total_amount += transaction["amount"]


        average_transaction = total_amount / total_transactions


        largest_transaction = transactions[0]["amount"]

        for transaction in transactions:

            if transaction["amount"] > largest_transaction:
                largest_transaction = transaction["amount"]


        latest_transaction = transactions[-1]["type"]
        latest_timestamp = transactions[-1]["timestamp"]


    else:

        average_transaction = 0.00
        largest_transaction = 0.00
        latest_transaction = "None"
        latest_timestamp = "None"


    return {
        "total_transactions": total_transactions,
        "deposits": deposits,
        "withdrawals": withdrawals,
        "total_deposited": total_deposited,
        "total_withdrawn": total_withdrawn,
        "average_transaction": average_transaction,
        "latest_transaction": latest_transaction,
        "latest_timestamp": latest_timestamp,
        "largest_transaction": largest_transaction
    }


"""

######### Learning Signature #########

Programmed by: THEO PAULO CASTINAR

Date Submitted: September 9 2026

Program Description: This program reads the ATM transaction file and calculates information about deposits withdrawals amounts and recent transactions.

Reflection: I learned how to process several transaction records and store the results in a dictionary so the Streamlit app can display them.

AI Usage

[ ] No AI Assistance - Completed independently without AI.

[X] AI as Support Tool - Used AI for explanations syntax or minor corrections.

[ ] AI as Collaborative Partner - Used AI to design structure or co-create significant code.

"""
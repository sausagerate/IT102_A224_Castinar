import streamlit as st

from castinar_atm_account import Account
import castinar_atm_balance
import castinar_atm_deposit
import castinar_atm_withdraw
import castinar_atm_history
import castinar_atm_analysis


# Configure the page
st.set_page_config(
    page_title="CASTINAR ATM",
    page_icon="🏧",
    layout="wide"
)


# Create the Account object only once
if "account" not in st.session_state:
    st.session_state.account = Account(
        "THEO PAULO CASTINAR",
        10000.00
    )


account = st.session_state.account


# Main title
st.title("🏧 PYTHON ATM by CASTINAR")

st.write(f"Welcome {account.account_name}")

st.divider()


# Sidebar menu
st.sidebar.title("ATM MENU")

menu = st.sidebar.radio(
    "Choose an option",
    [
        "Check Balance",
        "Deposit",
        "Withdraw",
        "View History",
        "Analyze Transactions"
    ]
)


# CHECK BALANCE
if menu == "Check Balance":

    st.header("Check Balance")

    balance = castinar_atm_balance.check_balance(account)

    st.metric(
        "Current Balance",
        f"₱{balance:,.2f}"
    )


# DEPOSIT
elif menu == "Deposit":

    st.header("Deposit Money")

    amount = st.number_input(
        "Enter deposit amount",
        value=0.00,
        step=100.00
    )

    if st.button("Deposit Money"):

        success = castinar_atm_deposit.deposit_money(
            account,
            amount
        )

        if success:

            st.success("Deposit successful.")

            balance = castinar_atm_balance.check_balance(account)

            st.metric(
                "New Balance",
                f"₱{balance:.2f}"
            )

        else:

            st.error("Invalid deposit amount.")


# WITHDRAW
elif menu == "Withdraw":

    st.header("Withdraw Money")

    current_balance = castinar_atm_balance.check_balance(account)

    st.metric(
        "Available Balance",
        f"₱{current_balance:.2f}"
    )

    amount = st.number_input(
        "Enter withdrawal amount",
        value=0.00,
        step=100.00
    )

    if st.button("Withdraw Money"):

        if amount <= 0:

            st.error("Invalid withdrawal amount.")

        elif amount > current_balance:

            st.error("Insufficient balance.")

        else:

            success = castinar_atm_withdraw.withdraw_money(
                account,
                amount
            )

            if success:

                st.success("Withdrawal successful.")

                new_balance = castinar_atm_balance.check_balance(
                    account
                )

                st.metric(
                    "New Balance",
                    f"₱{new_balance:.2f}"
                )

            else:

                st.error("Withdrawal failed.")



# VIEW HISTORY
elif menu == "View History":

    st.header("Transaction History")

    lines = castinar_atm_history.view_history()

    if lines:

        transactions = []
        current = {}

        for line in lines:

            line = line.strip()

            if line.startswith("Timestamp:"):
                current["Timestamp"] = line.replace(
                    "Timestamp:",
                    ""
                ).strip()

            elif line.startswith("Account:"):
                current["Account"] = line.replace(
                    "Account:",
                    ""
                ).strip()

            elif line.startswith("Transaction:"):
                current["Transaction"] = line.replace(
                    "Transaction:",
                    ""
                ).strip()

            elif line.startswith("Amount:"):
                current["Amount"] = line.replace(
                    "Amount:",
                    ""
                ).strip()

                transactions.append(current)
                current = {}

        if transactions:

            st.dataframe(
                transactions,
                use_container_width=True
            )

        else:

            st.info("No transactions found.")

    else:

        st.info("No transaction history yet.")


# ANALYZE TRANSACTIONS
elif menu == "Analyze Transactions":

    st.header("Transaction Analysis")

    analysis = castinar_atm_analysis.analyze_transactions()


    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Transactions",
            analysis["total_transactions"]
        )

    with col2:
        st.metric(
            "Deposits",
            analysis["deposits"]
        )

    with col3:
        st.metric(
            "Withdrawals",
            analysis["withdrawals"]
        )


    col4, col5 = st.columns(2)

    with col4:
        st.metric(
            "Total Deposited",
            f"₱{analysis['total_deposited']:.2f}"
        )

    with col5:
        st.metric(
            "Total Withdrawn",
            f"₱{analysis['total_withdrawn']:.2f}"
        )


    col6, col7 = st.columns(2)

    with col6:
        st.metric(
            "Average Transaction",
            f"₱{analysis['average_transaction']:.2f}"
        )

    with col7:
        st.metric(
            "Largest Transaction",
            f"₱{analysis['largest_transaction']:.2f}"
        )


    st.subheader("Latest Activity")

    st.write(
        f"Latest Transaction: "
        f"{analysis['latest_transaction']}"
    )

    st.write(
        f"Latest Timestamp: "
        f"{analysis['latest_timestamp']}"
    )


elif menu == "Deposit":

    st.header("Deposit Money")

    amount = st.number_input(
        "Enter deposit amount",
        min_value=0.00,
        step=100.00,
        format="%.2f"
    )

    if st.button("Deposit Money"):

        if amount <= 0:
            st.error("Invalid deposit amount.")

        else:
            success = castinar_atm_deposit.deposit_money(
                account,
                amount
            )

            if success:
                st.success("Deposit successful.")

                new_balance = castinar_atm_balance.check_balance(
                    account
                )

                st.metric(
                    "New Balance",
                    f"₱{new_balance:,.2f}"
                )

            else:
                st.error("Deposit failed.")

elif menu == "Withdraw":

    st.header("Withdraw Money")

    current_balance = castinar_atm_balance.check_balance(account)

    st.metric(
        "Available Balance",
        f"₱{current_balance:,.2f}"
    )

    amount = st.number_input(
        "Enter withdrawal amount",
        min_value=0.00,
        step=100.00,
        format="%.2f"
    )

    if st.button("Withdraw Money"):

        if amount <= 0:
            st.error("Invalid withdrawal amount.")

        elif amount > current_balance:
            st.error("Insufficient balance.")

        else:
            success = castinar_atm_withdraw.withdraw_money(
                account,
                amount
            )

            if success:
                st.success("Withdrawal successful.")

                new_balance = castinar_atm_balance.check_balance(
                    account
                )

                st.metric(
                    "New Balance",
                    f"₱{new_balance:,.2f}"
                )

            else:
                st.error("Withdrawal failed.")                


elif menu == "View History":

    st.header("Transaction History")

    lines = castinar_atm_history.view_history()

    transactions = []
    current = {}

    for line in lines:

        line = line.strip()

        if line == "":
            continue

        if line.startswith("Timestamp:"):
            current["Timestamp"] = line.replace(
                "Timestamp:",
                ""
            ).strip()

        elif line.startswith("Account:"):
            current["Account"] = line.replace(
                "Account:",
                ""
            ).strip()

        elif line.startswith("Transaction:"):
            current["Transaction"] = line.replace(
                "Transaction:",
                ""
            ).strip()

        elif line.startswith("Amount:"):
            current["Amount"] = line.replace(
                "Amount:",
                ""
            ).strip()

            transactions.append(current)
            current = {}

    if transactions:
        st.dataframe(
            transactions,
            use_container_width=True
        )

    else:
        st.info("No transactions found.")


elif menu == "Analyze Transactions":

    st.header("Transaction Analysis")

    analysis = castinar_atm_analysis.analyze_transactions()


    # ==========================================
    # TRANSACTION SUMMARY
    # ==========================================

    st.subheader("1. Transaction Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Transactions",
            analysis["total_transactions"]
        )

    with col2:
        st.metric(
            "Deposits",
            analysis["deposits"]
        )

    with col3:
        st.metric(
            "Withdrawals",
            analysis["withdrawals"]
        )


    # ==========================================
    # TRANSACTION AMOUNT ANALYSIS
    # ==========================================

    st.divider()

    st.subheader("2. Transaction Amount Analysis")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "Total Deposited",
            f"₱{analysis['total_deposited']:,.2f}"
        )

    with col5:
        st.metric(
            "Total Withdrawn",
            f"₱{analysis['total_withdrawn']:,.2f}"
        )

    with col6:
        st.metric(
            "Average Transaction",
            f"₱{analysis['average_transaction']:,.2f}"
        )


    # ==========================================
    # ACCOUNT ACTIVITY ANALYSIS
    # ==========================================

    st.divider()

    st.subheader("3. Account Activity Analysis")

    col7, col8, col9 = st.columns(3)

    with col7:
        st.metric(
            "Latest Transaction",
            analysis["latest_transaction"]
        )

    with col8:
        st.metric(
            "Largest Transaction",
            f"₱{analysis['largest_transaction']:,.2f}"
        )

    with col9:
        st.metric(
            "Latest Activity",
            analysis["latest_timestamp"]
        )

"""

######### Learning Signature #########

Programmed by: THEO PAULO CASTINAR

Date Submitted: September 9 2026

Program Description: This program creates a web based ATM using Streamlit and connects the Account object with the different ATM modules.

Reflection: I learned how to turn the ATM program into a web app and connect the Streamlit interface to the Account object and modules.

AI Usage

[ ] No AI Assistance - Completed independently without AI.

[X] AI as Support Tool - Used AI for explanations syntax or minor corrections.

[ ] AI as Collaborative Partner - Used AI to design structure or co-create significant code.

"""
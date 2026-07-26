import pandas as pd
from datetime import datetime

from extensions import db
from models.income import Income
from models.expense import Expense


def import_transactions(file, current_user):
    """
    Imports transactions from CSV.
    Credit -> Income
    Debit -> Expense
    """

    df = pd.read_csv(file)

    required_columns = [
        "Date",
        "Description",
        "Type",
        "Category",
        "Amount",
        "Payment Method"
    ]

    # Validate columns
    for column in required_columns:
        if column not in df.columns:
            return False, f"Missing column: {column}"

    imported = 0

    for _, row in df.iterrows():

        try:

            transaction_date = datetime.strptime(
                str(row["Date"]),
                "%Y-%m-%d"
            ).date()

            amount = float(row["Amount"])

            transaction_type = str(
                row["Type"]
            ).strip().lower()

            description = str(
                row["Description"]
            )

            category = str(
                row["Category"]
            )

            payment_method = str(
                row["Payment Method"]
            )

            if transaction_type == "credit":

                income = Income(
                    user_id=current_user.user_id,
                    source=category,
                    amount=amount,
                    income_date=transaction_date,
                    description=description
                )

                db.session.add(income)

            elif transaction_type == "debit":

                expense = Expense(
                    user_id=current_user.user_id,
                    category=category,
                    amount=amount,
                    payment_method=payment_method,
                    description=description,
                    expense_date=transaction_date
                )

                db.session.add(expense)

            imported += 1

        except Exception:
            continue

    db.session.commit()

    return True, imported
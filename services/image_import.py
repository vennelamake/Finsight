import easyocr
import re

reader = easyocr.Reader(['en'])


def extract_transactions(image_path):

    result = reader.readtext(image_path)

    lines = [item[1].strip() for item in result if item[1].strip()]

    transactions = []

    i = 0

    while i < len(lines):

        if lines[i] in ["DEP TFR", "WDL TFR"]:

            tx_type = lines[i]

            date = ""

            description = ""

            amount = ""

            balance = ""

            if i + 1 < len(lines):
                date = lines[i + 1]

            if i + 3 < len(lines):
                description = lines[i + 3]

            if i + 4 < len(lines):
                amount = lines[i + 4]

            if i + 5 < len(lines):
                balance = lines[i + 5]

            transactions.append({
                "date": date,
                "type": tx_type,
                "description": description,
                "amount": amount,
                "balance": balance
            })

            i += 6

        else:
            i += 1

    return transactions
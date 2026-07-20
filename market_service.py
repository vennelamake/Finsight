import yfinance as yf
import time

from datetime import timedelta


def get_stock_price(symbol):

    try:

        symbol = symbol.strip().upper()

        stock = yf.Ticker(symbol)

        data = stock.history(
            period="5d",
            auto_adjust=False
        )

        if data.empty:

            print(
                f"Price unavailable for {symbol}"
            )

            return None

        current_price = float(
            data["Close"].dropna().iloc[-1]
        )

        return round(
            current_price,
            2
        )

    except Exception as error:

        print(
            f"Market price error for {symbol}:",
            error
        )

        return None
    
def refresh_investment_prices(investments, db):

    updated = False

    for investment in investments:

        if investment.symbol:

            latest_price = get_stock_price(
                investment.symbol
            )

            if latest_price is not None:

                investment.current_price = latest_price

                updated = True

    if updated:

        db.session.commit()

def get_market_data(symbol):

    try:

        ticker = yf.Ticker(symbol)

        history = ticker.history(period="5d")

        if history.empty:
            return None

        current_price = float(
            history["Close"].iloc[-1]
        )

        if len(history) > 1:

            previous_price = float(
                history["Close"].iloc[-2]
            )

            change_percent = (
                (
                    current_price
                    - previous_price
                )
                / previous_price
            ) * 100

        else:

            change_percent = 0

        return {
            "price": current_price,
            "change": change_percent
        }

    except Exception as error:

        print(
            f"Market data error for {symbol}:",
            error
        )

        return None

# ADD HERE

market_cache = {
    "data": None,
    "timestamp": 0
}

CACHE_DURATION = 300

def get_market_overview():

    market_symbols = {
        "NIFTY 50": "^NSEI",
        "SENSEX": "^BSESN",
        "Bitcoin": "BTC-INR"
    }

    market_data = {}

    for name, symbol in market_symbols.items():

        market_data[name] = get_market_data(symbol)

    # GOLD - INR PER 10 GRAMS

    gold_data = get_market_data("GC=F")
    usd_inr_data = get_market_data("INR=X")

    if gold_data and usd_inr_data:

        # Gold futures price is per troy ounce.
        # 1 troy ounce = 31.1035 grams.

        gold_price = (
            gold_data["price"]
            * usd_inr_data["price"]
            / 31.1035
            * 10
        )

        market_data["Gold"] = {
            "price": round(gold_price, 2),
            "change": gold_data["change"]
        }

    else:

        market_data["Gold"] = None

    return market_data


def get_historical_price(symbol, price_date):

    try:

        symbol = symbol.strip().upper()

        ticker = yf.Ticker(symbol)

        start_date = price_date

        end_date = price_date + timedelta(days=5)

        history = ticker.history(
            start=start_date,
            end=end_date,
            auto_adjust=False
        )

        if history.empty:
            return None

        price = float(
            history["Close"].dropna().iloc[0]
        )

        return round(price, 2)

    except Exception as error:

        print(
            f"Historical price error for {symbol}:",
            error
        )

        return None
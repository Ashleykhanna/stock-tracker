import os
from dotenv import load_dotenv

from stock_data import get_last_two_closes, calculate_percent_change
from alert import build_alert_message, should_alert

load_dotenv()

STOCK_SYMBOL = os.getenv("STOCK_SYMBOL", "TSLA")
COMPANY_NAME = os.getenv("COMPANY_NAME", STOCK_SYMBOL)
ALERT_THRESHOLD_PERCENT = float(os.getenv("ALERT_THRESHOLD_PERCENT", "5"))


def run():
    previous_close, close_before_that = get_last_two_closes(STOCK_SYMBOL)
    percent_change = calculate_percent_change(previous_close, close_before_that)

    print(f"{STOCK_SYMBOL}: {percent_change:+.2f}% "
          f"(${close_before_that:.2f} -> ${previous_close:.2f})")

    if should_alert(percent_change, ALERT_THRESHOLD_PERCENT):
        message = build_alert_message(
            STOCK_SYMBOL, COMPANY_NAME, percent_change,
            previous_close, close_before_that,
        )
        print("\nALERT TRIGGERED")
        print(message)
    else:
        print(f"No alert: change is within the {ALERT_THRESHOLD_PERCENT}% threshold.")


if __name__ == "__main__":
    run()

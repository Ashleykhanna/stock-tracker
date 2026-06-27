def build_alert_message(symbol: str, company_name: str, percent_change: float,
                         previous_close: float, close_before_that: float) -> str:
    arrow = "🔺" if percent_change > 0 else "🔻"
    return (
        f"{arrow} {company_name} ({symbol}): {percent_change:+.2f}%\n"
        f"  Previous close: ${previous_close:.2f}\n"
        f"  Close before that: ${close_before_that:.2f}"
    )


def should_alert(percent_change: float, threshold_percent: float) -> bool:
    return abs(percent_change) >= threshold_percent

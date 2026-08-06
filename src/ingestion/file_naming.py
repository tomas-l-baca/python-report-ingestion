from datetime import datetime, timedelta, timezone


MDT = timezone(timedelta(hours=-6))


def build_report_filename(city_name):
    formatted_date = datetime.now(MDT).strftime("%Y-%m-%d")
    return f"{city_name}_Report_{formatted_date}.csv"
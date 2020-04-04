def income_per_week(weekdays_load=30, weekends_load=300, fee_per_person=20):
    income = (weekdays_load * 5 + weekends_load * 2) * fee_per_person
    return income


def income_per_year():
    income_per_day = income_per_week() / 7
    return income_per_day * 365


print(income_per_year())

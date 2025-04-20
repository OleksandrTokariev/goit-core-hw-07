import datetime as dt

def get_days_from_today(date):
    try:
        today = dt.datetime.today() # get today date
        datetime_date = dt.datetime.strptime(date, "%Y-%m-%d") # convert date into datetime format
        days_difference = (today - datetime_date).days # calculate difference between today and date in days
        return days_difference # return days difference
    except ValueError:
        print("date does not match format '%Y-%m-%d'")


print(get_days_from_today('2025-04-20'))
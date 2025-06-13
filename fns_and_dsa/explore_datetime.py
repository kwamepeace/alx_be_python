from datetime import date, datetime, time, timedelta

def display_current_datetime ():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date ():
    day = int(input("Enter the number of days to add to the current date: "))
    future_date = date.today() + timedelta( days = day)
    future_date_strftime = future.strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")


display_current_datetime()
calculate_future_date()


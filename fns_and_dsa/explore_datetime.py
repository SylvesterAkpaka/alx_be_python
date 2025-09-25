# explore_datetime.py

from datetime import datetime, timedelta  # ✅ import datetime module

def display_current_datetime():
    current_date = datetime.now()  # ✅ save current date
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # ✅ format
    print("Current date and time:", formatted_date)
    return formatted_date  # ✅ return the formatted date

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # ✅ save future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future_date)
    return formatted_future_date  # ✅ return the formatted date

if __name__ == "__main__":
    # Part 1
    display_current_datetime()
    
    # Part 2
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(number_of_days)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

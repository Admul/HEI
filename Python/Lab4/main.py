import datetime as dt

def get_date():
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_v = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    year = int(input("Enter year: "))
    while year < dt.MINYEAR or year > dt.MAXYEAR:
        invalid_value_message()
        year = int(input("Enter year: "))
    
    month = int(input("Enter month: "))
    while month < 1 or month > 12:
        invalid_value_message()
        month = int(input("Enter month: "))
        
    day = int(input("Enter day: "))
    
    while day < 1 or condition(year, day, days, days_v, month):
        invalid_value_message()
        day = int(input("Enter day: "))
        
    return dt.date(year, month, day)

def check_year_v(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
    
def invalid_value_message():
    print("Invalid value... Please try again.")
    
def condition(year, day, days, days_v, month):
    day_check = check_year_v(year) == False and day > days[month-1]
    day_check_v = check_year_v(year) and day > days_v[month-1]
    
    return day_check or day_check_v
    
first_date = get_date()
second_date = get_date()

date_difference = abs(first_date-second_date)
print(date_difference)

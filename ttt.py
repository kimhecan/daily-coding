def isleapyear(year):
    # assume year >= 0
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

def next_month(year, month):
    # assume year >= 0 and 1 <= month <= 12
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return (year, month)

def days_in_month(year, month):
    # assume year >= 0 and 1 <= month <= 12
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isleapyear(year):
            return 29
        else:
            return 28

def date_after_n_days(year, month, day, n):
    totalDay = day + n
    if totalDay <= days_in_month(year, month):
        return (year, month, totalDay)
    else:
        #이번달의 day를 뺀다
        totalDay -= days_in_month(year, month)
        #년과 달을 업데이트해준다.
        nextYear, nextMonth = next_month(year, month)
        return date_after_n_days(nextYear, nextMonth, 0,totalDay)

print(date_after_n_days(2017,4,20,2))
print(date_after_n_days(2017,4,20,10))
print(date_after_n_days(2017,4,20,200))
print(date_after_n_days(2017,4,20,300))
print(date_after_n_days(2017,4,20,1000))
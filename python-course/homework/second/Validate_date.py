def is_leap_year(year):
    return year % 4 == 0


def is_valid_date(day, month, year):
    days_30 = [4,6,9,11]
    days_31 = [1,3,5,7,8,10,12]
    if day < 1 or day > 31:
        return False
    if month < 1 or month > 12:
        return False
    if year < 1 :
        return False
    leap_year = is_leap_year(year)
    is_feb = month == 2
    #Check month Feb
    if (leap_year and is_feb):
        if day > 29:
            return False

    if (not leap_year and is_feb):
        if day > 28:
            return False

    # Check months with 30 days
    if month in days_30:
        if day > 30:
            return False
    # Check months with 31 days
    if month in days_31:
        if day > 31:
            return False
    return True


print(is_valid_date(31, 12, 2000))
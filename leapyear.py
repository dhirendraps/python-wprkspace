def is_leap(year):
    """
    Determine if a year is a leap year.
    A year is a leap year if:
    - Divisible by 4 AND not divisible by 100, OR
    - Divisible by 400
    """
    MIN_YEAR = 1900
    MAX_YEAR = 100000
    
    if not (MIN_YEAR <= year <= MAX_YEAR):
        return False
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input())

print(is_leap(year))
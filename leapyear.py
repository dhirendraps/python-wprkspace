def is_leap(year):
    leap = False
    
    if 1900 <= year and year <= (10**5):
        if year%4==0 and year%100==0 and year%400==0:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))
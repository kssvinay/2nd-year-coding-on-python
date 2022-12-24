#Assignment -8:
#Write a program to print leap years upto given range?

def is_leap(year):
    leap = False
    
    if year%100==0:
        if year%400==0:
            leap = True
    else:
        if year%4==0:
            leap = True
    
            
    
    return leap

year_start = int(input())
year_end = int(input())
for i in range(year_start,year_end):
    if is_leap(i):
        print(i)

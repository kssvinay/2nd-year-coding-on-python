'''https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true'''

def is_leap(year):
    leap = False
    
    if year%100==0:
        if year%400==0:
            leap = True
    else:
        if year%4==0:
            leap = True
    
            
    
    return leap

year = int(input())

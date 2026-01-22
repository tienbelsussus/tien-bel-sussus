def year():
    leap_year= int(input("enter a year: "))
    if leap_year%4 == 0:
        print(" This is the leap year ")
    elif leap_year%100 == 0:
        if leap_year%400 ==0:
            print("this is the leap yyyyyyear ")
    else:
        print(" this is not the leap year")
year()
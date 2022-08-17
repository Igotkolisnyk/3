time = int(input("enter the number of minutes:"))
if time < 0 or time > 60:
    print ("Eror, please enter correct time")
elif 0 <= time <= 15:
    print ("firest quarter")
elif 15 < time <= 30:
    print ("second quater")
elif 30 < time <= 45:
    print ("third quater")
elif 45 < time <= 60:
    print ("fourd quater")

    

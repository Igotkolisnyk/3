amount = int(input("enter the amout of coffee :")) 
a = 6
b = int(amount/6)
if amount >= a:
           print (f"you took {b} free cofffe")
           print ("get your coffee at the checkout")
elif amount  < a and amount > 0:
    print ("get your coffee at the checkout")
if amount <= 0:
    print ("Eror, pease try again")


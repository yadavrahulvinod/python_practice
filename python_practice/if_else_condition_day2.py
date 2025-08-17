user_val= int(input("enter the temprature "))

if user_val>=30:
    print("its a hot day")
if user_val>=50:
   print("eve if the above if is true still this if is gonna get checked ,beacause if is the fist condition and elif is only done when if is wrong")
elif user_val <=20:
    print("its a notmal day")
elif user_val <=10:
    print("its a cold day")
else:
 print("unkown weather")



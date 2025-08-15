#here we need a 2 input one in int and another in string , first we need to specify weigth and then 
# specify weight in lbs or kgs then provide the answer


weight = int(input("Enter Your Weight"))
weight_in =input("Weight in (K)gs or (L)bs")

if weight <= 1 or weight_in=="":
   print("ivalid input")


if  weight_in.lower() == "l":
     print("Weight in Kgs: "+str(weight*0.45))
elif weight_in.lower()=="k":
    print("weight in Lbs: "+str(weight/0.45))
   
var1 =5
var2=99

addition = var1+var2
print("addition "+str(addition))
subtraction =var1-var2
print( "subtraction "+str(subtraction))
multiplication= var1*var2
print("multiplication "+str(multiplication))
divison = var1/var2   # this return float value (3.33333333)
print("divison "+str(divison))
divison_type_2=var1//var2 # this returns a whole number/ integer (3)
print("divison_type_2 "+str(divison_type_2))
modulo=var1%var2 
print("modulo "+str(modulo))
exponent_operator=var1**var2 # this is use to return a raised too values like, here it is returning 5^99 5 to the power of 99
print("Exponent "+str(exponent_operator)) 


# same operation in less line of code mentioned below
var1+=var2
print(var1) #=104
var1-=var2
print(var1) #= 5
var1*=var2
print(var1) #= 495
var1/=var2
print(var1) #= 5.0
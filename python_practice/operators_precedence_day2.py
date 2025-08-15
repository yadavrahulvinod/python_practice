# bassically there is a precedence in arithemetic operations in python which means that 
# whenever you use mutiply or divide while try addition on the same line it first does 
# multiplication and divion and then does the subtraction and addition 

#Examples

var1=5
var=26

result =var1+var * 6   #161
result2 = (var1+var) * 6 #186
print(result)
print(result2)

#same happens for the other operators

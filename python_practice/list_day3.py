"4 main data structures in python"
"list -[1,2,3,4] "
"tuples-(1,2,3,4)"
"set-{1,2,3,4}"
"dictionary-{'Brand':'google','model':'pexel 10'}"
#sequence types = lists,tuple
"lists are mutable"
"tuples are immutable"
"set are mutable"
"dictionary are mutable"



names= ["radha","krishna","bholenath","maa parvati","hanumann"]
print(names)
print(names[0])
print(names[0].upper().find("DHA"))
print(names[0].upper().find("DHA"))
print(names[3].upper())
print(names[-2].upper())
names[4]="hanuman" #this proves list has index and data can be changed latteron 
print(names)
print(names[0:3])
names.append("narsimha") 
print(names)

numbers=[1,2,3,4,5,6,7,8,9,9,"a",]
print(numbers)
numbers.insert(0,1001)
numbers.insert(4,1002)
numbers.insert(-1,1003)
print(numbers)
numbers.remove("a") 
print(numbers) 

print(1000 in numbers)
print(1001 in numbers) #returns boolean values
print(len(numbers))

print(dir(numbers))

"""
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__'
 , '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '
 __rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
   'insert', 'pop', 'remove', 'reverse', 'sort']
"""
print(names.count("maa parvati"))

print(numbers.pop())# removes last elements from the list
#numbers.clear()
print(numbers)

for inn in numbers:
    print( str(type(inn)) + f"value : {inn}")

newlist=range(1,5)
sum = 0
for i in newlist:
  sum = sum + i 
print (sum)


newex=[100,200,None,"invalid",300,400.5,100,100]
sun =0

for  ii in newex:
     if  type(ii)== int or type(ii)== float :
        sun +=ii
     
     else:
      continue
 
print(sun)


print(newex.index("invalid"))

print(newex.count(100))

numbers.sort() # it sorts from smaller to bigger number
numbers.reverse() # it just reverse the list
print(numbers)

numbers2=numbers 
numbers2[1]=200
print(numbers2)
print(numbers)# value is changed in both of them since both of the list points to the same memory location of that value
#so you can't copy like that 

numbers2=numbers2.copy()
numbers2[1]=1000
print(numbers2)
print(numbers)# see now it didnt changed


customerid=[102,105,102,103,107,109,110,109]

ucust =[]

for y in customerid:
 if y in ucust:
    continue
 else:
    ucust.append(y)   
  

print(ucust) # {102, 103, 105, 107, 109, 110}

# now using sets

unique_cust_set =set(customerid) #this used to add values in set from lists 
print(unique_cust_set)  # {102, 103, 105, 107, 109, 110} same output because set only hold unique values


ammount = [100,200,50,500,400,900,1200,70]
newammount_withgst = []
for b in ammount:
   newammount_withgst.append(b+b*18/100)
print(newammount_withgst)

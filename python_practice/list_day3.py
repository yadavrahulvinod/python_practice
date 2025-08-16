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

numbers.clear()
print(numbers)
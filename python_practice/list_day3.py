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

numbers=[1,2,3,4,5,6,7,8,9,"a",]
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

numbers.clear()
print(numbers)
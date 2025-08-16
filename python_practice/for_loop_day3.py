rahul=5
names=[1,2,3,4,5,6,7,8]


for iterator in names:
    print(iterator)

print("done")

# range

# range(start, stop, step)
'''start → (optional) the first number (default = 0)
stop → the number up to but not including this value
step → (optional) the difference between each number (default = 1)'''

for num in range(4,0,-1):

    print(names[num])




'''
✅ Method 1: Using [::-1] (slicing)
names = [1, 2, 3, 4, 5, 6, 7, 8]

for item in names[::-1]:
    print(item)
'''


'''
✅ Method 2: Using reversed()
names = [1, 2, 3, 4, 5, 6, 7, 8]

for item in reversed(names):
    print(item)
'''
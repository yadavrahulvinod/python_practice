ammount = [100,200,50,500,400,900,1200,70]
newammount_withgst = []
for b in ammount:
   newammount_withgst.append(b+b*18/100)
print(newammount_withgst)


"LIST COMPREHENSION BELOW"

"""
List comprehension is a shorter and cleaner way to create lists in Python.

Instead of writing a full for loop, you can generate lists in one line.

🔹 Basic Syntax
******[expression for item in iterable if condition]******

expression → what you want in the list

item → variable from the loop

iterable → list, range, string, etc.

if condition (optional) → filter items

"""


orders_including_gst=[x+x*18/100 for x in ammount]
print(orders_including_gst)

# its a list of tuple it can consits of 2 values where it is mostly called like [(0[1],0[2]) ,(1[0],1[1])] so on  
new_gst=[(100,5),(200,18),(50,12),(500,18),(400,12),(900,5),(1200,5),(70,12)] 
new_gst_list=[y[0]+y[0]*y[1]/100 for y in new_gst]
print(new_gst_list)


new_nested_list=[[m,m**2,m**3] for m in range(1,4)] # created a nested list using a list comprehension
print(new_nested_list) # [[1, 1, 1], [2, 4, 8], [3, 9, 27]]

flatend =[]
for k in new_nested_list:
   for h in k:
      flatend.append(h)
print(flatend)



flatend1 = [item for j in new_nested_list for item in j ] #nested list flattening using list comprehension

print(flatend1)




orders_list = [
    [101, '2023-07-25 00:00:00.0', 11599, 'CLOSED'],
    [102, '2023-07-25 00:00:00.0', 256, 'PENDING_PAYMENT'],
    [103, '2023-07-25 00:00:00.0', 12111, 'COMPLETE']
]

closed_orders_flat=[ i for sublist in orders_list for i in sublist if "CLOSED" in sublist]

# another way of doing it 

closed_orders_flat1=[sublist for sublist in orders_list if sublist[3] =="CLOSED"]

print(closed_orders_flat)
print(closed_orders_flat1)


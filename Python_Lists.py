
thislist = ["Mahesh", "Samrat", "Ashok", "Sachin"]
print(thislist)
print(type(thislist))
print(len(thislist))
print(thislist[1])
thislist[1] ="Rohit"

#change the list items
print(thislist)

#checking whether the item is present or not
if "SAndip" in thislist:
    print("Yes it is present...")
else:
    print("Sorry couldn't find the item...")

# add the item in the list
thislist.append("Sandip")
print(thislist)

#append two list
thislist2 =["Suraj","Sachin","Mahesh"]
thislist2.extend(thislist)
print(thislist2)


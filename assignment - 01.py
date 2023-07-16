# create a list of fruits by taking input from the user

fruits = []
n = int(input("How many fruits do you want to enter ?  " ) )
for i in range(n):
  fruit=input("enter the fruit :")
  i+=1
  fruits.append(fruit)
print("The list of fruits is:", fruits)

# combine two list

lst1=[1,2,3,4]
lst2=[5,6,7,8]
lst3=lst1+lst2
print(lst3)

# add element to list

addlst=[1,2,3,4,5,6]
addlst.append(0)
print(addlst)

# print only integer data for list
intlst=[1,2,3,4.0,9.9]

for i in intlst:
  if type(i)==int:
    print(i)
  else:
    print("not an integer")

# append a value in list if not present

newlst=['what','where','when','what']
new_value=input("enter a new value :")

if new_value not in newlst:
  newlst.append(new_value)
  print(newlst)
else:
  print("already present")
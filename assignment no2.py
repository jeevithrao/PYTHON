# List
# ------

# Write a Python program to create a list.

lst=[1,2,3,4,5,6]
print(type(lst))
print(lst)

# Write a Python program to add an element to a list.

lst.append(0)
print(lst)

# Write a Python program to remove an element from a list.

lst.pop()
print(lst)

# Write a Python program to sort a list.

lst1=[1,3,4,2,5,6,3]
lst1.sort()
print(lst1)

# Write a Python program to reverse a list.

lst.reverse()
print(lst)

# Write a Python program to find the maximum element in a list.

numbers = [10, 5, 8, 12, 7]
maximum = numbers[0]
for number in numbers:
  if number > maximum:
    maximum = number
print("The maximum element is", maximum)

# Write a Python program to find the minimum element in a list.


numbers = [10, 5, 8, 12, 7]
minimum = numbers[0]
for number in numbers:
  if number < minimum:
    minimum = number
print("The minimum element is", minimum)

# Write a Python program to find the sum of all elements in a list.

numbers = [10, 5, 8, 12, 7]
sum = 0
for number in numbers:
  sum = sum + number
print("The sum of all elements is", sum)

# Write a Python program to find the average of all elements in a list.
average=sum/len(numbers)
print(average)

# Write a function to find the maximum and minimum values in a list.

def max_min(lst):
  max = lst[0]
  min = lst[0]
  for num in lst[1:]:
    if num > max:
      max = num
    if num < min:
      min = num
  return (max, min)

# Write a function to reverse the order of a list.

lstn = [1,2,3,4,5,6,7,8,9,10,11]
lstn.reverse()
print(lstn)

# Write a function to sort a list in ascending or descending order.

lst2 = [1,3,4,2,1,6]
lst2.sort()
print("ascending order :" , lst2)
lst2.reverse()
print("descending order :", lst2)

# Write a function to remove duplicates from a list.

lst5=[1,1,2,2,3,3,4,4,4]
conv_lst5=set(lst5)
print(conv_lst5)
conv_set=list(conv_lst5)
print(conv_set)

# Write a function to find the index of a given element in a list.
lst6=[1,2,3,4,5,6]
print(lst6[4])
print(id(4))

# Tuple
# -------
# Write a Python program to create a tuple.

tup=(1,2,3,4)
print(tup)
print(type(tup))

# Write a Python program to add an element to a tuple. 

tup1=(1,2,3,4,5,6,7)
tup_lst=list(tup1)
tup_lst.append(8)
print(tup_lst)
tupp=tuple(tup_lst)
print(tupp)

# Write a Python program to remove an element from a tuple.

lst_tup=[1,2,3,4]
lst_tup.pop()
print(lst_tup)
tup2=tuple(lst_tup)
print(tup2)

# Write a Python program to sort a tuple.

tuplst=[1,2,3,4,4,8,5,6,2,1]
tuplst.sort()
tup4=tuple(tuplst)
print(tup4)

# Write a Python program to reverse a tuple.

tuplst.sort(reverse=True)
tup5=tuple(tuplst)
print(tup5)

# Write a Python program to find the maximum element in a tuple.

numbers = (10, 5, 8, 12, 7)
maximum = numbers[0]
for number in numbers:
  if number > maximum:
    maximum = number
print("The maximum element is", maximum)

# Write a Python program to find the minimum element in a tuple.

numbers = (10, 5, 8, 12, 7)
minimum = numbers[0]
for number in numbers:
  if number < minimum:
    minimum = number
print("The minimum element is", minimum)

# Write a Python program to find the sum of all elements in a tuple.

numbers = (10, 5, 8, 12, 7)
sum = 0
for number in numbers:
  sum = sum + number
print("The sum of all elements is", sum)

# Write a Python program to find the average of all elements in a tuple.

avg=sum/len(numbers)
print(avg)

# Set
# ------

# Write a Python program to create a set.
set={1,2,3,4}
print(set)
print(type(set))

# Write a Python program to add an element to a set.

set1={1,2,3,4,5}
set1.update({0})
print(set1)

# Write a Python program to remove an element from a set.

set2={6,5,4,3,2,1,0}
set2.remove(0)
print(set2)

# Write a Python program to find the union of two sets.

set3={1,2,3,4}
set4={4,5,6,7}
print(set3.union(set4))

# Write a Python program to find the intersection of two sets.

set5={2,3,4,5}
set6={4,5,6,7}
print(set5.intersection(set6))

# Write a Python program to find the difference of two sets.

set7={1,2,3,4}
set8={4,5,6,7}
print(set7.difference(set8))

# Write a Python program to find the symmetric difference of two sets.

print(set7.symmetric_difference(set8))

# Write a Python program to check if an element is present in a set.

set_1={1,2,3,4,5,6}
element=int(input("enter the element :"))
if element in set_1:
  print("element present in set")
else:
  print("element not present")

# Write a Python program to print all elements of a set.

numbers = {10, 5, 8, 12, 7}
for number in numbers:
  print(number)

# Binary Search 

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(l: list, target: int, high=None, low=None):

  if low == None:
    low = 0
  if high == None:
    high = len(l) -1 
  if low > high:
    return -1

  mid = (low + high) // 2
  if l[mid] == target:
    return mid
  elif l[mid] < target:
    return binary_search(l, target, high, mid+1)
  elif l[mid] > target:
    return binary_search(l, target, mid -1, low)



test_list = [1,3,9,11,17,19,29]
test_val1 = 25
test_val2 = 15

# print(1 // 2)
# print(test_list[0])
print(binary_search(test_list, test_val1)) 
print(binary_search(test_list, test_val2)) 


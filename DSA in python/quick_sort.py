"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
# [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
def quicksort(array):
    pivot = array[-1]
    stop = False
    compar_index = 0
    before_pivot_count = -1
    after_action = -1
    if array <= 1:
      return array
    while not stop:
      if pivot < array[compar_index]:
        before_pivot_count -= 1
        before_pivot = array[before_pivot_count]
        print(before_pivot_count)
        print(after_action)
        
        # Switching numbers 
        array[before_pivot_count] = pivot
        array[after_action] = array[compar_index]
        array[compar_index] = before_pivot
        after_action -= 1
        continue
      elif pivot == array[compar_index]:
        print('equal while')
        pivot = array[-1]
        compar_index = 0
        before_pivot_count = -1
        after_action = -1
        continue
      
      for i in range(len(array)):
        
        if pivot > array[i]:
          # print('continued')
          continue
        elif pivot == array[i]:
          print('equal for')
          stop = True
          break
        else:
          compar_index = i
          before_pivot_count += 1
          print('break')
          break
      # break
    print(f'{array}')
    print(f'i:{compar_index} c1:{before_pivot_count} c2:{after_action}')
    return 

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# print(test[-1])
quicksort(test)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
  
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
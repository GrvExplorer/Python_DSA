"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    pivot = array[-1]
    stop = False
    compar_index = 0
    count = -1
    count2 = -1
    while not stop:
      if pivot < array[compar_index]:
        count -= 1
        before_pivot = array[count]
        array[count] = pivot
        array[count2] = array[compar_index]
        array[compar_index] = before_pivot
        count2 -= 1
        continue
      elif pivot == array[compar_index]:
        print('equal')
      for i in range(len(array)):
        if pivot > array[i]:
          print('continued')
          continue
        elif pivot == array[i]:
          print('wrong')
          break
        else:
          compar_index = i 
          print(f'{array}')
          print(f'i:{compar_index} c1:{count} c2:{count2}')
          break
      break
    return []

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quicksort(test)
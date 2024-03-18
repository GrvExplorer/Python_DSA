def bubble_sort(array, times_bubble):
  
  counter = 0 # ans: len(array)
  looped = 0
  isArraySorted = False
  while not isArraySorted:
    for f in range(len(array) -1): 
      print(f'current {array[f]} prev: {array[f+1]}')
      if array[f] > array[f+1]:
        store = array[f]
        array[f] = array[f+1]
        array[f+1] = store
        continue
      elif array[f] < array[f+1]:
        counter += 1
        continue
      else:
        continue
    looped += 1
    if times_bubble == looped:
      isArraySorted = True
    
  return array

        
print()
print(f'Answer: {bubble_sort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14], 3)}')
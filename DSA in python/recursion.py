"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

# def check_is_fib(position, start=0, second=1):
#   output = start+second
#   if position == start:
#     return start
#   elif position < start:
#     return -1
  
#   return check_is_fib(position, second, output)

# # Test cases
# print(check_is_fib(8))
# print(check_is_fib(11))
# print(check_is_fib(0))

def get_fib_sec_value(position, start=0, second=1, counter=0):
  output = start+second
  if position == counter:
    return start
  elif position < counter:
    return second
  counter = counter + 1
  return get_fib_sec_value(position, second, output, counter)
# Test cases
print(get_fib_sec_value(9))
print(get_fib_sec_value(16))
print(get_fib_sec_value(0))

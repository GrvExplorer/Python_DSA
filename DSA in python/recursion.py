"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position, start=0, second=1):
  output = start+second
  
  if position == output:
    return start
  elif position < output:
    return -1
  return get_fib(position, output, output+second)

# Test cases
print(get_fib(8))
print(get_fib(21))
print(get_fib(0))

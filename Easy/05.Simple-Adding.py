# Using the JavaScript language, have the function SimpleAdding(num) add up all the numbers from 1 to num. 
# For the test cases, the parameter num will be any number from 1 to 1000.

def SimpleAdding(num):
  total = 0;
  for x in range(0, num + 1):
      total = total + x
  return total


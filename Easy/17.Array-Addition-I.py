# Using the Python language, have the function ArrayAdditionI(arr) take the array of numbers stored in arr
# and return the string true if any combination of numbers in the array ca be
# added up to equal the largest number in the array, otherwise return the string false. 
# For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true  
# because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all
# the same elements, and may contain negative numbers

def ArrayAdditionI(arr):
  arr.sort()
  largest = arr.pop()
  result = [False]
  def findCombo(sum=0,i=0):
    if sum is largest:
      result[0] = True
      return
    while i < len(arr):
      sum += arr[i]
      findCombo(sum,i+1)
      sum -= arr[i]
      i += 1
  findCombo()
  return result[0]
print ArrayAdditionI([5,4,3,1,9])


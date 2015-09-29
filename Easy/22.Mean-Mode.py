# Using the Python language, have the function MeanMode(arr) take the array of numbers stored in arr 
# and return 1 if the mode equals the mean, 0 if they don't equal each other
# (ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)). 
# The array will not be empty, will only contain positive integers, and will not contain more than one mode. 

def MeanMode(arr):
  mean = reduce(lambda x,y: x + y, arr)/float(len(arr))
  def getMode(arr):
      storage = {}
      for num in arr:
        try:
            storage[num] = storage[num] + 1
        except: storage[num] = 1
      tempMode = max(storage, key=lambda k: storage[k])
      return tempMode   
  mode = getMode(arr)
  return 1 if mean == mode else 0 

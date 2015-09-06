def FirstReverse(str):
  result = ""
  rev = reversed(list(str))
  for letter in rev:
    result = result + letter
  return result 

# this is also a cool way to do it  

# def FirstReverse(str):
#   return str[::-1]


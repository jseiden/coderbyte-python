# Using the Python language, have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str. 
# For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number. 

def DashInsert(str):
  res = list()
  for i in range(len(str)):
     num = str[i]
     res.append(num)
     if int(num) % 2 != 0 and i != len(str) - 1 and int(str[i + 1]) % 2 != 0:
         res.append("-")


  return ''.join(res)


  

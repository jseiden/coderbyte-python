# Using the Python language, have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
# Replace every letter in the string with the letter following it in the alphabet 
# (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 

def LetterChanges(str):
  result = ""

  for x in str:
    if x == "z": 
      newChar = "a"
    elif x == "Z":
      newChar = "A"
    elif x.isalpha():
      newChar = chr(ord(x) + 1)
    else:
      newChar = x

    if newChar in "aeiou":
      newChar = newChar.upper()
    result = result + newChar

  return result

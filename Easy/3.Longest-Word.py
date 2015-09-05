# Using the Python language, have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. 
# If there are two or more words that are the same length, return the first word from the string with that length. 
# Ignore punctuation and assume sen will not be empty.

def LongestWord(sen):
  longest = "" 
  longestCount = 0
  for x in sen.split():
      tempCount = 0
      for y in x:
         if y.isalpha():
            tempCount += 1 
      if tempCount > longestCount:
          longestCount = tempCount
          longest = x
  return longest

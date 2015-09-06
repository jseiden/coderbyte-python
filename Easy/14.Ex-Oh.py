# Using the Python language, have the function ExOh(str) take the str parameter being passed 
# and return the string true if there is an equal number of x's and o's, otherwise return the string false. 
# Only these two letters will be entered in the string, no punctuation or numbers. 
# For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's. 

def ExOh(str):
    ex = 0
    oh = 0
    for letter in str:
        if letter.lower() == "x":
            ex += 1
        elif letter.lower() == "o": 
            oh += 1
    if ex == oh:
        return "true"
    else:
        return "false"

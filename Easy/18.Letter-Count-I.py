# Using the Python language, have the function LetterCountI(str) take the str parameter being passed 
# and return the first word with the greatest number of repeated letters. 
# For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) 
# and it comes before ever which also has 2 e's. If there are no words with repeating letters return -1. Words will be separated by spaces. 

def LetterCountI(str):
    greatest = "-1"
    greatestCount = 0;

    def findRepeats(word):
        storage = {}
        rep = 0
        for letter in list(word):
            try:
                storage[letter] = storage[letter] + 1
            except: 
                storage[letter] = 1
        for n in storage:
            if storage[n] > 1:
                rep = rep + storage[n]
        return rep

    arr = str.split()

    for word in arr:
        c = findRepeats(word)
        if c > greatestCount:
            greatest = word
            greatestCount = c

    return greatest


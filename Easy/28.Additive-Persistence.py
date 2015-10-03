# Using the Python language, have the function AdditivePersistence(num) take the num parameter being passed 
# which will always be a positive integer and return its additive persistence 
# which is the number of times you must add the digits in num until you reach a single digit. 
# For example: if num is 2718 then your program should return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9. 

def AdditivePersistence(num):
    count = 0
    ls = list(str(num))
    while len(ls) > 1:
        newNum = reduce(lambda x,y: int(x) + int(y), ls)
        ls = list(str(newNum))
        count += 1
    return count


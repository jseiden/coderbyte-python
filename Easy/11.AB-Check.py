# Using the Python language, have the function ABCheck(str) take the str parameter being passed and 
# return the string true if the characters a and b are separated by exactly 3 places anywhere in the string at least once 
# (ie. "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise return the string false. 

def ABCheck(str):
    ls = list(str)
    l = len(str)
    for x in range(l):
        if ls[x] == "a":
            if l - x >= 4:
                if ls[x + 4] == "b":
                    return "true"
        elif ls[x] == "b":
            if l - x >= 4:
                if ls[x + 4] == "a":
                    return "true"
    return "false"

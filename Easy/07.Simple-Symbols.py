# Using the Python language, have the function SimpleSymbols(str) take the str parameter being passed 
# and determine if it is an acceptable sequence by either returning the string true or false. 
# The str parameter will be composed of + and = symbols with several letters between them 
# (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. 
# So the string to the left would be false. The string will not be empty and will have at least one letter. 

def SimpleSymbols(str):
    flag = True
    if len(str) < 3:
        return "false"
    for x in range(1,len(str)):
        if str[x].isalpha() and (str[x-1] != "+" or str[x+1] != "+"):
            flag = False
    if flag:
        return "true"
    else:
        return "false"

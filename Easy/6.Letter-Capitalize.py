# Using the Python language, have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. 
# Words will be separated by only one space.

def LetterCapitalize(str):
    result = ""
    for word in str.split():
        result = result + " " + word[0].upper() + word[1:] 
    # cut off extra space at beginning of result
    return result[1:]

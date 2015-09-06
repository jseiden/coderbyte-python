# Using the Python language, have the function VowelCount(str) take the str string parameter being passed and return the number of vowels the string contains 
# (ie. "All cows eat grass" would return 5). Do not count y as a vowel for this challenge.

def VowelCount(str):
    count = 0
    vowels = "aeiou"
    for letter in str:
        if letter.lower() in vowels:
            count += 1
    return count

'''
PROBLEM 1
Create a function that returns True if the given string has any of the following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters or contains characters that don't fit into any category, return False.

Examples:

csAlphanumericRestriction("Bold") ➞ True
csAlphanumericRestriction("123454321") ➞ True
csAlphanumericRestriction("H3LL0") ➞ False
Notes:

Any string that contains spaces or is empty should return False.
'''

def csAlphanumericRestriction(input_str):
    # check if input_str has all letters
        # yes, then it is TRUE
    # check if input_str has all numbers
        # yes, then it is TRUE
    # check if input_str has all letters and numbers
        # yes, then it is False

    if input_str.isalpha():
        return True
    elif input_str.isdigit():
        return True
    else:
        return False

'''
PROBLEM 2:
Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

Examples:

csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
csOppositeReverse("Radar") ➞ "RADAr"
Notes:

The input string will only contain alpha characters.
'''
def csOppositeReverse(txt):
    reverseTxt = ''
    
    for letter in txt:
        if letter != letter.upper():
            reverseTxt = reverseTxt + letter.upper()
        else:
            reverseTxt = reverseTxt + letter.lower()

    return reverseTxt[::-1]

'''
PROBLEM 3:
Create a function that given an integer, returns an integer where every digit in the input integer is squared.

Examples:

csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
csSquareAllDigits(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9
'''
def csSquareAllDigits(n):
    result = ''
    for num in str(n): # converting an int in into str
        result = result + str((int(num)) ** 2)
    return int(result)

'''
PROBLEM 4
Given a string, return a new string with all the vowels removed.

Examples:

csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
Notes:

For this challenge, "y" is not considered a vowel.
'''
def csRemoveTheVowels(input_str):
    txt_without_vowel = input_str
    
    for letter in 'aeiouAEIOU':
        txt_without_vowel = txt_without_vowel.replace(letter, "")
    return txt_without_vowel
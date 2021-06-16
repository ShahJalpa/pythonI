'''
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
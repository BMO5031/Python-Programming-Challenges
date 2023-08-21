# Toy Problem Challenges

This repository contains solutions to three programming challenges. Each challenge focuses on solving a specific problem using Python functions. The challenges cover various concepts such as time conversion, conditional logic, and string manipulation.

## Challenge 1: Converting 12-hour time to 24-hour time

**Problem:** Given a 12-hour time representation (hour, minute, and period), write a function that converts it to the 24-hour time format.

**Function Signature:**
```python
def convert_to_24_hour(hour, minute, period):
    """
    Converts a 12-hour time to 24-hour time.

    :param hour: Hour (1 to 12)
    :param minute: Minute (0 to 59)
    :param period: "am" or "pm"
    :return: 24-hour time string (HHMM)
    """
    # Implementation details here
    pass

Challenge 2: Two numbers are positive

Problem: Write a function that takes three integers as arguments and returns True if exactly two of the three integers are positive numbers, and False otherwise.

Function Signature:

python

def two_positive(a, b, c):
    """
    Determines if exactly two out of three integers are positive.

    :param a: First integer
    :param b: Second integer
    :param c: Third integer
    :return: True if exactly two integers are positive, False otherwise
    """
    # Implementation details here
    pass

Challenge 3: Consonant value

Problem: Given a lowercase string with alphabetic characters, write a function that returns the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou". The value of consonants is assigned as a=1, b=2, c=3, ..., z=26.

Function Signature:

python

def solve(s):
    """
    Calculates the highest value of consonant substrings.

    :param s: Input string with alphabetic characters only
    :return: Highest value of consonant substrings
    """
    # Implementation details here
    pass

Usage Examples

python

# Challenge 1
result1 = convert_to_24_hour(8, 35, "pm")
print(result1)  # Output: "0830"

# Challenge 2
result2 = two_positive(2, 4, -3)
print(result2)  # Output: True

# Challenge 3
result3 = solve("zodiacs")
print(result3)  # Output: 26

Notes

    The solutions are implemented using Python programming language.
    Each challenge has a corresponding function that performs the specified task.
    Examples are provided to demonstrate the functionality of each challenge's solution.

Feel free to explore the source code and experiment with the provided examples.

vbnet


Remember to replace the placeholder text with actual implementation details and examples. This README should provide a clear overview of each challenge and its associated function.

Author: BRIAN MARTIN OMONDI ODHIAMBO
"""
Python Is Easy course @Pirple.com
Homework Assignment #3: "If" Statements
Patrick Kalkman / patrick@simpletechture.nl

Details:
 
Create a function that accepts 3 parameters and checks for equality between 
any two of them.

Your function should return True if 2 or more of the parameters are equal, 
and false is none of them are equal to any of the others.

Extra Credit:

Modify your function so that strings can be compared to integers if they are 
equivalent. For example, if the following values are passed to 
your function: 6,5,"5"

You should modify it so that it returns true instead of false. 
Hint: there's a built in Python function called "int" that will help you 
convert strings to Integers.

"""


def areTwoOrMoreInputsEqual(param1, param2, param3):

    convertedParam1 = int(param1)
    convertedParam2 = int(param2)
    convertedParam3 = int(param3)

    if convertedParam1 == convertedParam2:
        return True

    if convertedParam1 == convertedParam3:
        return True

    if convertedParam2 == convertedParam3:
        return True

    return False


result = areTwoOrMoreInputsEqual(1, 2, 3)
print(f"(1,2,3) should return False and is {result}")

result = areTwoOrMoreInputsEqual(1, 1, 3)
print(f"(1,1,3) should return True and is {result}")

result = areTwoOrMoreInputsEqual(1, 2, 2)
print(f"(1,2,2) should return True and is {result}")

result = areTwoOrMoreInputsEqual(1, 2, 1)
print(f"(1,2,1) should return True and is {result}")

result = areTwoOrMoreInputsEqual(1, 1, 1)
print(f"(1,1,1) should return True and is {result}")

result = areTwoOrMoreInputsEqual(1, 2, "1")
print(f"(1,2,'1') should return True and is {result}")

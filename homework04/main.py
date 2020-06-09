"""
Python Is Easy course @Pirple.com
Homework Assignment #4: Lists
Patrick Kalkman / patrick@simpletechture.nl

Details:

Create a global variable called myUniqueList. It should be an empty list to
start.

Next, create a function that allows you to add things to that list.
Anything that's passed to this function should get added to myUniqueList,
unless its value already exists in myUniqueList.
If the value doesn't exist already, it should be added and the function
should return True. If the value does exist, it should not be added,
and the function should return False;

Finally, add some code below your function that tests it out.
It should add a few different elements, showcasing the different scenarios,
and then finally it should print the value of myUniqueList to show that
it worked.

Extra Credit:

Add another function that pushes all the rejected inputs into a separate
global array called myLeftovers. If someone tries to add a value to
myUniqueList but it's rejected (for non-uniqueness),
it should get added to myLeftovers instead.

"""

myUniqueList = []
myLeftOvers = []


def addToUniqueList(thingToAdd):
    if thingToAdd not in myUniqueList:
        myUniqueList.append(thingToAdd)
        return True
    else:
        addToLeftOversList(thingToAdd)
        return False


def addToLeftOversList(leftOver):
    myLeftOvers.append(leftOver)


isAdded = addToUniqueList('Hello')
print(f"List is empty, item added to the list, result = True => {isAdded}")

isAdded = addToUniqueList('Second')
print(f"Added item is unique, item added to the list, result = True => {isAdded}")

isAdded = addToUniqueList(86)
print(f"Added item is unique, item added to the list, result = True => {isAdded}")

isAdded = addToUniqueList([1, 2])
print(f"Added item is unique, item added to the list, result = True => {isAdded}")

isAdded=addToUniqueList('Second')
print(f"Added item is not unique, item should not be added, result = False => {isAdded}")

isInLeftOvers='Second' in myLeftOvers
print(f"Added item is not unique,  item should added to the leftovers, result = True => {isInLeftOvers}")

isAdded=addToUniqueList(86)
print(f"Added item is not unique, item should not be added, result = False => {isAdded}")

isInLeftOvers=86 in myLeftOvers
print(f"Added item is not unique,  item should added to the leftovers, result = True => {isInLeftOvers}")

"""
Python Is Easy course @Pirple.com
Homework Assignment #2: Functions
Patrick Kalkman / patrick@simpletechture.nl

Details:
 
Let's return to the music example from assignment one. Pick 3 of the attributes you listed. 
For our example we're going to say "Genre", "Artist" and "Year". 
Create a new Python file and create 3 functions with the same name as those attributes. 
So in this example we'd have one function named "genre" another named "artist" and another called "year".

When someone calls any of those functions, that function should return the corresponding value for that attribute. 
For example, if we call the "Artist" function our function would return "Dave Brubeck". 
Yours should return whatever values make sense for your music choice.

Extra Credit:

One of the data types we haven't covered yet is called "booleans". When a variable is set to True or False, that's a boolean. 
For extra credit, see if you can figure out how to use booleans, and add an extra function that returns a boolean value instead of a String or Number. 
Hint: make sure to capitalize the first letter in the words True or False when you use them. 
We'll cover booleans more in the lecture on "if" statements coming up next in the course.

"""

# Favorite Song: Tennessee Whiskey by Chris Stapleton
def artistName():
    return "Chris Stapleton"

def artistGender():
    return "Male"

def title():
    return "Tenessee Whiskey"

def album():
    return "Traveller"

def numberOfSongsOnAlbum():
    return 14

def releasedIn():
    return 2015

def genre():
    return "Country"

def durationInSeconds():
    return 293

def originalAuthor():
    return "David Allan Coe"

def country():
    return "United States"

def priceInDollars(): 
    return 2.75

def bio():
    return "Christopher Alvin Stapleton is an American singer-songwriter, " + \
    "guitarist, and record producer. He was born in Lexington, Kentucky," + \
    " and grew up in Staffordsville, Kentucky, until moving to Nashville, " + \
    "Tennessee, in 2001 to pursue a career in music writing songs. " + \
    " Subsequently, Stapleton signed a contract with Sea Gayle Music to " + \
    "write and publish his music."

def wikipediaLink():
    return "https://en.wikipedia.org/wiki/Chris_Stapleton"

def isCover():
    return True

def isAvailableOnVinyl():
    return False

print(f"Title: {title()}")
print(f"Artist: {artistName()}")
print(f"Gender: {artistGender()}")
print(f"Album: {album()}")
print(f"Number of songs on album: {numberOfSongsOnAlbum()}")
print(f"Year: {releasedIn()}")
print(f"Genre: {genre()}")
print(f"Country: {country()}")
print(f"Duration: {durationInSeconds()} s")
print(f"Original autor: {originalAuthor()}")
print(f"Price: ${priceInDollars()}")
print(f"Bio: {bio()}")
print(f"Wikipedia link: {wikipediaLink()}")
print(f"Is a cover: {isCover()}")
print(f"Is available on vinyl: {isAvailableOnVinyl()}")


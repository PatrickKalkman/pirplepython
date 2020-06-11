"""
Python Is Easy course @Pirple.com
Homework Assignment #7: Dictionary and Sets
Patrick Kalkman / patrick@simpletechture.nl

Details:

Return to your first homework assignments, when you described your favorite
song. Refactor that code so all the variables are held as dictionary keys and
value. Then refactor your print statements so that it's a single loop that
passes through each item in the dictionary and prints out it's key and then
it's value.


Extra Credit:

Create a function that allows someone to guess the value of any key in the
dictionary, and find out if they were right or wrong. This function should
accept two parameters: Key and Value. If the key exists in the dictionary
and that value is the correct value, then the function should return true.
In all other cases, it should return false.

"""

# Favorite Song: Tennessee Whiskey by Chris Stapleton
FavoriteSong = {}
FavoriteSong["Artist"] = "Chris Stapleton"
FavoriteSong["ArtistGender"] = "Male"
FavoriteSong["Title"] = "Tenessee Whiskey"
FavoriteSong["Album"] = "Traveller"
FavoriteSong["NumberOfSongsOnAlbum"] = 14
FavoriteSong["Year"] = 2015
FavoriteSong["Genre"] = "Country"
FavoriteSong["DurationInSeconds"] = 293
FavoriteSong["OriginalAutor"] = "David Allan Coe"
FavoriteSong["Country"] = "United States"
FavoriteSong["TimesPlayedOnSpotify"] = 287881875
FavoriteSong["PriceInDollars"] = 2.75
FavoriteSong["Bio"] = "Chris Alvin Stapleton is a singer-songwriter, " + \
    "guitarist, and record producer. He was born in Lexington, Kentucky," + \
    " and grew up in Staffordsville, Kentucky, until moving to Nashville, " + \
    "Tennessee, in 2001 to pursue a career in music writing songs. " + \
    " Subsequently, Stapleton signed a contract with Sea Gayle Music to " + \
    "write and publish his music."
WikipediaLink = "https://en.wikipedia.org/wiki/Chris_Stapleton"


def printFavoriteSongAttributes():
    for key in FavoriteSong:
        print(f"{key}")


def printFavoriteSongAttributesAndValues():
    for key in FavoriteSong:
        print(f"{key} = {FavoriteSong[key]}")


def guessFavoriteSongAttribute(key, value):
    if key not in FavoriteSong:
        print("The given key does not exist")
        return False

    if FavoriteSong[key] == value:
        print("You guessed right")
        return True
    else:
        print("Sorry you guessed wrong, try again")
        return False


printFavoriteSongAttributes()
# Do not show the values as then the game is nu fun :)
# printFavoriteSongAttributesAndValues()

while True:
    key = input("What attribute do you want to guess? ")
    if key == "":
        break
    value = input(f"What or who do you think the {key} is? ")

    guessFavoriteSongAttribute(key, value)

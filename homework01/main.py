"""
Python Is Easy course @Pirple.com
Homework Assignment #1: Variables
Patrick Kalkman / patrick@simpletechture.nl

Details:

What's your favorite song?
Think of all the attributes that you could use to describe that song. That is:
all of it's details or "meta-data". These are attributes like "Artist",
"Year Released", "Genre", "Duration", etc. Think of as many different
characteristics as you can. In your text editor, create an empty file and name
it main.py.
Now, within that file, list all of the attributes of the song, one after
another, by creating variables for each attribute, and giving each variable
 a value.

"""

# Favorite Song: Tennessee Whiskey by Chris Stapleton
Artist = "Chris Stapleton"
ArtistGender = "Male"
Title = "Tenessee Whiskey"
Album = "Traveller"
NumberOfSongsOnAlbum = 14
Year = 2015
Genre = "Country"
DurationInSeconds = 293
OriginalAutor = "David Allan Coe"
Country = "United States"
TimesPlayedOnSpotify = 287881875
PriceInDollars = 2.75
Bio = "Christopher Alvin Stapleton is an American singer-songwriter, " + \
    "guitarist, and record producer.x He was born in Lexington, Kentucky," + \
    " and grew up in Staffordsville, Kentucky, until moving to Nashville, " + \
    "Tennessee, in 2001 to pursue a career in music writing songs. " + \
    " Subsequently, Stapleton signed a contract with Sea Gayle Music to " + \
    "write and publish his music."
WikipediaLink = "https://en.wikipedia.org/wiki/Chris_Stapleton"

print(f"Title: {Title}")
print(f"Artist: {Artist}")
print(f"Gender: {ArtistGender}")
print(f"Album: {Album}")
print(f"Number of songs on album: {NumberOfSongsOnAlbum}")
print(f"Year: {Year}")
print(f"Genre: {Genre}")
print(f"Country: {Country}")
print(f"Duration: {DurationInSeconds} s")
print(f"Original autor: {OriginalAutor}")
print(f"Number of plays on Spotify: {TimesPlayedOnSpotify}")
print(f"Price: ${PriceInDollars}")
print(f"Bio: {Bio}")
print(f"Wikipedia link: {WikipediaLink}")

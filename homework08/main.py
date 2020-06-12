"""
Python Is Easy course @Pirple.com
Homework Assignment #8: Input and Output (I/O)
Patrick Kalkman / patrick@simpletechture.nl

Details:

Create a note-taking program. When a user starts it up, it should prompt them
for a filename. If they enter a file name that doesn't exist, it should prompt
them to enter the text they want to write to the file. After they enter the
text, it should save the file and exit.

If they enter a file name that already exists, it should ask the user
if they want:

A) Read the file
B) Delete the file and start over
C) Append the file

If the user wants to read the file it should simply show the contents of
the file on the screen. If the user wants to start over then the file should
be deleted and another empty one made in its place. If a user elects to append
the file, then they should be able to enter more text, and that text should be
added to the existing text in the file.

Extra Credit:

Allow the user to select a 4th option:

D) Replace a single line

If the user wants to replace a single line in the file, they will then
need to be prompted for 2 bits of information:

1) The line number they want to update.
2) The text that should replace that line.

"""

import os.path


def ask_note_and_save(filename):
    content = input("Enter the text that you want to save: ")
    with open(filename, "w") as file:
        file.write(content)


def ask_note_and_append(filename):
    content = input("Enter the text that you want to add: ")
    with open(filename, "a") as file:
        # add a new line to that the appended content starts on a new line
        file.write("\n" + content)


def ask_line_and_note_and_replace(filename):
    line_number = int(input("Which line do you want to replace? "))
    content = input("Enter the text that you want to replace it with: ")

    # read existing file into line list
    with open(filename, "r") as file:
        lines = file.readlines()

    # replace the line using the list index
    # add new line as writelines does not add them
    lines[line_number - 1] = content + "\n"
    # remove the existing file
    os.remove(filename)

    # write the list with the replaced line back to the file
    with open(filename, "w") as file:
        file.writelines(lines)


def read_note(filename):
    with open(filename, "r") as file:
        return file.read()


def notes():
    filename = input("Enter the name of the file to save your note? ")
    if os.path.isfile(filename):
        print("The file already exists. Do you want to:")
        print("A) Read the file")
        print("B) Delete the file and start over")
        print("C) Append the file")
        print("D) Replace a single line")
        choice = input("What do you want to do? ")
        if choice == "A":
            print(read_note(filename))
        elif choice == "B":
            os.remove(filename)
            ask_note_and_save(filename)
        elif choice == "C":
            ask_note_and_append(filename)
        elif choice == "D":
            ask_line_and_note_and_replace(filename)

    else:
        ask_note_and_save(filename)


# Start the note taking app
notes()

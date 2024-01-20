# Escape characters :)

# backslash character has a special meaning in Python
# \n and \t for new line and tab respectively.

splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = '1\t2\t3\t4\t5'
print(tabbedString)     # print tabbed across the string

# tab is set to 4 char by default in intelliJ

# `\` can also be used to escape special characters like quotes and double quotes
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting.".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

#or
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")
# in triple quotes, we don't have to escape any characters.

anotherSplitString = """ This string has been
split over
several
lines"""

print(anotherSplitString)

# If we want to layout a string with breaks but don't want everyone to start with a new line
# we can escape the end of line with `\`


anotherSplitString1 = """This string has been\
split over\
several\
lines"""

print(anotherSplitString1)

#----------------------------------------------------------------------------------------------#
# More on Escape characters
print("""The pet shop owner said "No, no, \
'e's uh,...he's resting".""")


# what if we want to include second \ characters in string

# example

print("C:\Users\timbuchalka\notes.txt")
# to escape the escape character use \ as well.
# two ways to work with this.
print("C:\\Users\\timbuchalka\\notes.txt")
print(r"C:\Users\timbuchalka\notes.txt")    # or you can solve the problem by making it a raw string
# by including r before the string.

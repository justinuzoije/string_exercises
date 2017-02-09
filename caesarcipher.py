#Ceaser Cipher
#Justin Uzoije

#This function changes a letter to a number (a to z is 1 to 26)
def digitize(letter):
    if letter == 'a':
        return 1
    elif letter == 'b':
        return 2
    elif letter == 'c':
        return 3
    elif letter == 'd':
        return 4
    elif letter == 'e':
        return 5
    elif letter == 'f':
        return 6
    elif letter == 'g':
        return 7
    elif letter == 'h':
        return 8
    elif letter == 'i':
        return 9
    elif letter == 'j':
        return 10
    elif letter == 'k':
        return 11
    elif letter == 'l':
        return 12
    elif letter == 'm':
        return 13
    elif letter == 'n':
        return 14
    elif letter == 'o':
        return 15
    elif letter == 'p':
        return 16
    elif letter == 'q':
        return 17
    elif letter == 'r':
        return 18
    elif letter == 's':
        return 19
    elif letter == 't':
        return 20
    elif letter == 'u':
        return 21
    elif letter == 'v':
        return 22
    elif letter == 'w':
        return 23
    elif letter == 'x':
        return 24
    elif letter == 'y':
        return 25
    elif letter == 'z':
        return 26

#This function changes a number to a letter (1 to 26 is a to z)
def letterize(number):
    if number == 1:
        return 'a'
    elif number == 2:
        return 'b'
    elif number == 3:
        return 'c'
    elif number == 4:
        return 'd'
    elif number == 5:
        return 'e'
    elif number == 6:
        return 'f'
    elif number == 7:
        return 'g'
    elif number == 8:
        return 'h'
    elif number == 9:
        return 'i'
    elif number == 10:
        return 'j'
    elif number == 11:
        return 'k'
    elif number == 12:
        return 'l'
    elif number == 13:
        return 'm'
    elif number == 14:
        return 'n'
    elif number == 15:
        return 'o'
    elif number == 16:
        return 'p'
    elif number == 17:
        return 'q'
    elif number == 18:
        return 'r'
    elif number == 19:
        return 's'
    elif number == 20:
        return 't'
    elif number == 21:
        return 'u'
    elif number == 22:
        return 'v'
    elif number == 23:
        return 'w'
    elif number == 24:
        return 'x'
    elif number == 25:
        return 'y'
    elif number == 26:
        return 'z'

#This function adds 13 to a number. If the number is over 26 it rolls back to 1
def addThirteen(digit):
    intDigit = int(digit)
    plusThirteen = intDigit + 13
    if plusThirteen > 26:
        plusThirteen = plusThirteen - 26
    return plusThirteen

#This creates a blank new sentence
newSentence = ""

#This takes in the sentence the user wants
sentence = raw_input("Please input a sentence: ")

#This loops through the user's sentence and leaves spaces as spaces
#For nonspaces, it changes them to a number, adds 13, then back to a letter
for i in sentence:
    if i == " ":
       newChar = " "
    else:
       newChar = letterize(addThirteen(digitize(i)))
    newSentence = newSentence + newChar

#This prints the new sentence
print newSentence

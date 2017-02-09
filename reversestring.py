import sys
aString = raw_input("Please enter a string: ")

stringLength = len(aString) -1

counter = 0
for number in aString:
    sys.stdout.write (aString[stringLength - counter])
    counter = counter + 1


#import sys
#sys.stdout.write(string)

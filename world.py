#testing
print ('Hello World')

print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is :')
print (len(myName))

print('What is you age?')
myAge = input()
print('You will be '+ str(int(myAge)+1) +' in a year.')

total = 0
for num in range(101): #will auto increase by 1
#for num in range(0, 10, 2) start at 0, and increase by 2
#for num in range(10, -1, -1) start at 10, and decrease by -1
    total = total + num
print(total)

i = 0
while i < 5:
    print ('Jimmy five times ' + str(i))

#Random number library
import random
random.randint(1, 10)
#Import the system module
import sys
#below command will stop any code below to command from running
#sys.exit()

#Module for copy and paste
#pip.exe install pyperclip
import pyperclip
pyperclip.copy('Hello world!') #sends this text to the clip board
pyperclip.paste() #will return whatever text is currently on the clip board

#writing your own funtions
def hello(): #creates a function named 'hello'
    print('Howdy')

hello() #calling the new function 'hello'

def hello(yourName):
    print('Hello ' + yourName)

def plusone(numbers):
    return numbers + 1

print('cat', 'dog', 'mouse') #By default this will print with a space devider
print('cat', 'dog', 'mouse', sep='ABC') #Now the separator will be 'ABC' instead of space

spam = 42 #This is now a Global variable

def eggs():
    global spam #Will call the global variable
    bacon = 42 #local variable since it's inside a variable
    #local variables do not exist outside of the function

def div42by(divideby):
    try:
        return 42 / divideby
    #except ValueError:
    #   print('You did not enter a number')
    except ZeroDivisionError:
        print('Error: you tried to divide by zero')

print(div42by(2))

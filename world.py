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

#list
['cat', 'bat', 'rat', 'elephant']
things = ['cat', 'bat', 'rat', 'elephant']
#cat = things[0]
#bat = things[1]
#rat = things[2]
#elephant = things[3]

#cat = things[-4]
#bat = things[-3]
#rat = things[-2]
#elephant = things[-1]

#Slice is a list of values
things[1:3]
#You can assign a splice to override part of another list
#things[:2] - first 2 elements of the list will be shown
#things[1:] - starting with element 1 list all elements
len(things) #output will be 4 because there are 4 elements
del  things[1] #deletes the element at position 1

things2 = [['cat', 'bat'],[10, 20, 30, 40, 50]]
#cat = things2[0][0]
#bat = things2[0][1]
#30 = things2[1][2]
#40 = things2[]
 
list('Hello')
#['H', 'e','l','l','o']

#range returns a list like value
for i in range(4):
    print(i)
#0
#1
#2
#3

#list out a string
for i in range(len(things)):
    print('Index ' + str(i) _ ' in supplies is: ' + things[i])


cat = ['fat','orange','loud']
#Multi-variable list
size, color, disposition = cat
#could then go
size #output would then be 'fat'
color #output would then be 'orange'

#Methods - called on values
things = ['cat', 'bat', 'rat', 'elephant']
things.index('cat')
#will return 0
#Good way to find what element a value is located or the first occurance of the value
things.append('moose') #moose has been added to the end of the list
things.insert(1,'panda')#insert 'panda' at element position 1
things.remove('bat')#remove the value 'bat' from the list, or the first occurance of the valiable
things.sort()#Will sort ASCII alphabetical or smallest to largest. Uppercase will come before lowercase
things.sort(reverse=True)#Sort in reverse alphabetical or largest to smallest
things.sort(key=str.lower)#This will sort in true alphabetical order

#strings are immutable, they can not be changed
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
#output - 'Zophie the cat'
#lists are mutable
#a list like 'things' is referencing the values in memory, the values are not stored in 'things'
#if something else references the things list, then changes it, things will also be modified

#if you want to copy a list
import copy
things3 = copy.deepcopy(things)
#Things3 now is a copy of the things list

#Dictionary Data type
myCat = {'size':'fat', 'color':'gray','disposition':'loud'}
myCat['size']
#output - 'fat'
#dictionaries do not have an order
#This is like a word and definition sort of function
list(myCat.keys())#This will list all of the 'keys' of the dictionary
list(myCat.values())#This will list all of the 'values' of the dictionary
list(myCat.items())#This will list all of the 'keys' matched with their 'values'

for k,v in myCat.items():
    print(k,v)
#list all of the pairs

myCat.get('size',0) #If the value 'size' is not found return 0
myCat.get('size','') #If the value 'size' is not found return blank

myCat = {'name':'Zophie', 'age':7,'color':'gray'}
allCats = []
allCats.append({'name':'Zophie', 'age':7,'color':'gray'})
allCats.append({'name':'Pooka', 'age':5,'color':'black'})
allCats.append({'name':'Fat-tail', 'age':5,'color':'gray'})
allCats.append({'name':'???', 'age':-1,'color':'orange'})

type(myCat)#Type will tell you what data type you pass to it

newString = 'Hello World!'
newString.upper()#All characters are now upper case
newString.lower()#All Characters are now lower case

newString.isupper()#All characters checked if upper case
newString.islower()#All Characters checkeed if lower case
newString.isalpha()#Checks if all characters are alpha
newString.isalnum()#Checks if string is alpha numeric


','.join(['cat', 'bat', 'rat', 'elephant'])#Will join all of the strings with a comma in between
#output - 'cat,bat,rat,elephant'
'My name is Simon'.split()#Split at each empty space by default
#'my','name','is','Simon'
'My name is Simon'.split(m)#Split wherever the letter 'm' is
#'My na','e is Si','on'

#rjust
#ljust
#center
#strip

#String formatting
name = 'Alice'
place = 'park'
time = '6am'
food = 'pizza'

'Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food)
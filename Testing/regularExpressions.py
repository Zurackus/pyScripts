#! python 3
import re

def isPhoneNumber(text):
    print(text)#here would be some function that would find a phone number

message = "Call me 415-555-1011 tomorrow, or at 415-555-9999"
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')

#-------------------------------------------------------------------------#
message = "My number is 415-555-1011"

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)#phoneNumRegex.findall(message) - this will find all occurances within 'message'
print(mo.group())
#-------------------------------------------------------------------------#

message = "My number is 415-555-1011"
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(message)

mo.group()
#415-555-1011
mo.group(1)
#415
mo.group(2)
#555-1011

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
#This will search for Batman, Batmobile, Batcopter
#-------------------------------------------------------------------------#
batRegex = re.compile(r'Bat(wo)?man')#Search for Batman or Batwoman

#(wo)? Here the 'wo' can appear only 0 or 1 time in the expression
#(wo)* Here the 'wo' can appear 0 or 1 more in the expression
#(wo)+ Here the 'wo' can must appear 1 or more in the expression

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #requires the full number and area code
phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') #Can find a number without the area code

haRegex = re.compile(r'(Ha){3}')#Looking for 'Ha' 3 times like HaHaHa
#-------------------------------------------------------------------------#
digitRegex = re.compile(r'(\d){3,5}') #Default 'greedy' match and look for the first occurance of 5 digits
digitRegex = re.compile(r'(\d){3,5}?') #With the question mark the match will look for the shortest string possible
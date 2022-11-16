#! python 3
#The above line will say what version of python is required to run the script

#From the cmd line
#py c:\user\tkonsonlas\documents\hello.py

'''
@py c:\user\tkonsonlas\documents\hello.py %*
@pause
'''

import sys
print('Hello World')
sys.argv()

#the %* says to not show that line and forward provided arguments to python script
#@pyw - This will run a windowless python script
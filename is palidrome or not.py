# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:19:08 2022

@author: Dell
"""

#to accept a number as an argument and return true if the number is palindrome else return false.
def pal(p):
    if len(p)<1:
      return True
    else:
        if p[0]==p[-1]:
            return pal(p[1:-1])
        else:
            return False
a=str(input("Enter a number:"))
if (pal(a)==True):
    print("is palidrome")
else:
    print("not palidrome")
    
  
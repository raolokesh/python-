# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 03:40:06 2020

@author: Lokesh
"""

#Given a string of odd length greater 7, return a string made of the middle three chars of a given String

def middle_three_char(str):
    middle_index=int(len(str)/2)
    print('Original string is ',str)
    middle_str=str[middle_index-1:middle_index+2]
    print('Middle three words are ',middle_str)

str1=str(input('Enter a string:'))
middle_three_char(str1)



#Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1


def appendMiddle(s1, s2):
  middleIndex = int(len(s1) /2)
  print("Original Strings are", s1, s2)
  middleThree = s1[:middleIndex-1:]+ s2 +s1[middleIndex-1:]
  print("After appending new string in middle", middleThree)
  
appendMiddle("Chrisdem", "IamNewString")

#Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string


def mixString(s1, s2):
  resultString = s1[:1] + s2[:1] + s1[int(len(s1) /2):int(len(s1) /2)+1] +s2[int(len(s2) /2):int(len(s2) /2)+1] +s1[len(s1)-1] + s2[len(s2)-1]
  print("Mix String is ", resultString)
  
s1 = str(input('Enter a string:'))
s2 = str(input('Enter a string:'))
mixString(s1, s2)


#arrange String characters such that lowercase letters should come first

inputStr = str(input('Enter a string: '))
words = inputStr.split()
lower = []
upper = []
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedString = ''.join(lower + upper)
print("\n arranging characters giving precedence to lowercase letters:")
print(sortedString)


#Given a string input Count all lower case, upper case, digits, and special symbols




def findDigitsCharsSymbols(inputString):
  words = inputString.split()
  charCount = 0
  digitCount = 0
  symbolCount = 0
  for char in inputString:
    if char.islower() or char.isupper():
      charCount+=1
    elif char.isnumeric():
      digitCount+=1
    else:
      symbolCount+=1
      
  print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)
      
inputString = "P@#yn26at^&i5ve"
print("total counts of chars, digits,and symbols")
print(findDigitsCharsSymbols(inputString))


#Given two strings, s1 and s2, create a mixed String




def mixString(s1, s2):
  s2 = s2[::-1]
  lengthS1 = len(s1)
  lengthS2 = len(s2)
  length  = lengthS1 if lengthS1 > lengthS2 else lengthS2 
  resultString=""
  for i in range(length):
    if(i < lengthS1):
      resultString = resultString + s1[i]
    if(i < lengthS2):
      resultString = resultString + s2[i]
    
  print(resultString)
  
s1 = "Pynative"
s2 = "Website"
mixString(s1, s2)





#String characters balance Test


def stringBalanceCheck(s1, s2):
  flag = True
  for char in s1:
    if char in s2:
      continue
    else:
      flag = False
  return flag
  
s1 = "yn"
s2 = "Pynative"
flag = stringBalanceCheck(s1, s2)
print("s1 and s2 are balanced", flag)

s1 = "ynf"
s2 = "Pynative"
flag = stringBalanceCheck(s1, s2)
print("s1 and s2 are balanced", flag)


#Find all occurrences of “USA” in given string ignoring the case


inputString = "Welcome to USA. usa awesome, isn't it?"
substring = "USA"
tempString = inputString.lower()
count = tempString.count(substring.lower())
print("The USA count is:", count)


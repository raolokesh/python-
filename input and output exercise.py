# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:21:37 2020

@author: Lokesh
"""

#Question 1: Accept two numbers from the user and calculate multiplication

X=int(input('Enter a first number:'))
Y=int(input('Enter a second number:'))
print(x*y)


#Question 2: Display “My Name Is Lokesh” as “My**Name**Is**Lokesh” using output formatting of a print() function

# 
X = 'My Name Is Lokesh'
X.split()


#

print('My', 'Name', 'Is', 'Lokesh', sep='**')

#Question 3: Convert decimal number to octal using print() output formatting

x=int(input('enter a number:'))
print('%o'%(x))

#Question 4: Display float number with 2 decimal places using print()

x=float(input('Enter a float number:'))
print('%.2f'%(x))


# Question 5: Accept list of 5 float numbers as a input from user

floatNumbers = []
n = int(input("Enter the list size : "))

print("\n")
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = float(input())
    floatNumbers.append(item)
    
print("User List is ", floatNumbers)


#Question 6: write all file content into new file by skiping line 5 from following file


count=0
with open("text.txt", "r") as fp:
    lines = fp.readlines()
    count = len(lines)
with open("newFile.txt", "w") as fp:
    for line in lines:
        if (count == 3):
            count -= 1
            continue
        else:
            fp.write(line)
        count-=1
        
#`Question 7: Accept any three string from one input() call
    

str1,str2,str3=str(input().split())
print(str1,str2,str3)


'''Question 8: You have the following data.

totalMoney = 1000
quantity = 3
price = 450

display above data using string.format() method'''


quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))


#Question 9: How to check file is empty or not

import os
print(os.stat(r'H:\python code\python exercise\text.txt').st_size==0)


#Question 10: Read line number 4 from the following file

with open(r'H:\python code\python exercise\text.txt','r') as pd:
    line=pd.readlines()
    print(line[3])
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 23:20:54 2020

@author: Lokesh Rao
"""

#Question 1: Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum

# 1 type
x=int( input('Enter a first integer number :'))
y= int(input("Enter a second integer number :"))

if(x*y<1000):
    print('The result is ',x*y)
elif(x*y>1000):
    print('The result is ',x+y)
    

# 2 type in form of function

def multiplication_or_sum(x,y):
    if(x*y<1000):
        return x*y
    elif(x*y>1000):
        return x+y

a= int(input('Enter first number:'))
b= int(input('Enter second number:'))
result=multiplication_or_sum(a,b)
print('The result is ',result)


#Question 2: Given a range of first 10 numbers, 
#Iterate from start number to the end number and print the sum of the current number and previous number

# 1 type
x=0
for i in range(10):
    print('Currrent Number %d Previous number %d Sum: %d'%(i,x,i+x ))
    x=i

# 2 type

def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current Number", i, "Previous Number ", previousNum," Sum: ", sum)
        previousNum = i

print("Printing current and previous number sum in a given range(10)")
sumNum(10)


#Question 3: Given a string, display only those characters which are present at an even index number.

# 1 type
x=str(input('enter a string:'))
def string(x):
    for i in range(0,len(x),2):
        print('index[%d]'%i,x[i])
        
string(x)

#Question 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

# 1 type

x=str(input('Enter a string '))
y = int(input('enter a int'))
def remove_char(x,y):
    return x[y:]
remove_char(x,y)
    
#Question 5: Given a list of numbers, return True if first and last number of a list is same

# type

def first_last_number(lists):
    if(lists[0]==lists[-1]):
        return print('result is True')
    else:
        return print('result is False')

x=list(input('enter a numbers').split())
first_last_number(x)

#Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

# type 1

x=list(input('Enter the numbers in list: ').split()) #x is list its every element check i.e. is divisible by 5 
def div_by_5(x):
    list_div_by_5=list()
    for i in x:
        y=int(i)
        if (y%5==0):
            list_div_by_5.append(y)
    return list_div_by_5
result=div_by_5(x)
print('list that number divided by 5',result)


# type 2
def findDivisible(numberList):
    print("Given list is ", numberList)
    print("Divisible of 5 in a list")
    for num in numberList:
        if (num % 5 == 0):
            print(num)

numList = [10, 20, 33, 46, 55]
findDivisible(numList)



#Question 7: Return the total count of string “Lokesh” appears in the given string

# type 1

def string(str1):
    print('lokesh is %d times appears'%(str1.count('lokesh')))
    
x=str(input('Enter a string: '))
string(x)

# 2 type

def string(str1,str2):
    x=str1.count(str2)
    return x

input_str=str(input('Enter a string: '))
count_str=str(input('count string: '))
result = string(input_str,count_str)
print(count_str,' is appears ' ,result, 'times')    



#Question 8: Print the following pattern
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

# hint- using loop

# you think as 
for i in range(10):
    x=str(i)
    print(x*i)

# type 2
    
for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")
    

#Question 9: Reverse a given number and return true if it is the same as the original number

x = int(input('Enter a number:'))
def reverse(x):
    original_num = x
    reverse_num = 0
    while(x>0):
        reminader = x%10
        reverse_num=(reverse_num*10)+reminader
        x=x//10
    if (original_num == reverse_num):
        return True
    else:
        return False

print("The original and reverse number is the same:", reverse(x))


#Question 10: Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list 
#and even numbers from the second list

list1=list(input('Enter a list first: ').split())
list2=list(input('Enter a list second: ').split())
list_odd=[]
list_even=[]
for i in list1:
    y=int(i)
    if (y%2!=0):
        list_odd.append(i)

for i in list2:
    y=int(i)
    if (y%2 == 0 ):
        list_even.append(i)
        
list3=list_odd+list_even
print('result list is ',list3 )

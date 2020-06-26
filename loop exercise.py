# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:57:37 2020

@author: Lokesh
"""

#Question 1: Print First 10 natural numbers using while loop

i=0
while(i<11):
    print(i)
    i+=1
    
#Question 2: Print the following pattern
''' 1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5'''
    
last_num = int(input('Enter number:'))

for row in range(1,last_num):
    for column in range(1,row+1):
        print(column,end=' ')
    print('')   
    
    
#Question 3: Accept number from user and calculate the sum of all number between 1 and given number

last_num=int(input('Enter a last number: '))
sum=0
for i in range(0,last_num+1):
    sum+=i
print('Sum of all numbers up to %d number %d'%(last_num,sum))


#Question 4: Print multiplication table of given number

num = int(input('Enter a number:'))

for i in range(1,11):
    print(i*num)
    
    
#Question 5: A list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for item in list1:
    if (item > 150):
        break
    if(item % 5 == 0):
        print(item)
        
#Enter  a number count the total number of digits in a number


num = int(input('Enter a number: "))
count = 0
while num != 0:
    num //= 10
    count+= 1
print("Total digits are: ", count)



#Question 7: Print the following pattern using for loop
'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''

n = int(input('Enter  a number you want to start : '))
k = n
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
    
#Question 8: Reverse the following list using for loop
    
    
list1 = [10, 20, 30, 40, 50]
start = len(list1) - 1
stop = -1
step = -1
for i in range(start, stop, step) :
    print(list1[i])
    
#Question 9: Display -10 to -1 using for loop

for num in range(-10, 0, 1):
    print(num)
    
# Display a message “Done” after successful execution of for loop
    
    
for i in range(5):
    print(i)
else:
    print("Done!")

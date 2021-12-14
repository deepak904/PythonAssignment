# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:42:31 2021

@author: Deepak Kumar
@emailid: deepak.iafjnv@gmail.com

#Task 1
FULL NAME: DEEPAK KUMAR

"""
# QUESTION 1.
print("Question 1.")
print()
x: int = 5
y = x
for i in range(x, 0, -1):
    for j in range(0, i):
        print(y, end=' ')
    print()


# QUESTION 2.
print()
print("Question 2.")
print()
for i in range(5,0,-1):    
    for j in range(0,i+1):
        print(j, end=' ')
    print()


# QUESTION 3.
print()
print("Question 3.")
print()
a = 5
i = 1
while i <= a:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')
    
# QUESTION 4.
print()
print("Question 4.")
print()
a = 5
for i in range(1, a + 1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")
    
# QUESTION 5.
print()
print("Question 5.")
print()
a = 1
b = 2
current_num = b
for i in range(2, 6):
    for j in range(a, b):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    a = b
    b += i
    current_num = b
    
# QUESTION 6.
print()
print("Question 6.")
print()
def print_pattern(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(print_num(i, j), end=" ")
        print()

def print_num(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

print_pattern(7)


# QUESTION 7.
print()
print("Question 7.")
print()
for i in range(1, 5 + 1):
    for j in range(1, 5 + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
    
# QUESTION 8.
print()
print("Question 8.")    
print()
for i in range(1, 8 + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()
    
    
# QUESTION 9.
print()
print("Question 9.")    
print()
k = 8
for i in range(5, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")


# QUESTION 10.
print()
print("Question 10.")    
print()
star = 7
m = (2 * star) - 2
for i in range(0, star):
    for j in range(0, m):
        print(end=" ")
   
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")
    

# QUESTION 11.
print()
print("Question 11.")       
print()
start = 6
for i in range(0,start):
    for j in range(0,i+1):
        print("*", end=' ')
    print(" ")
print(" ")
for i in range(start+1,0,-1):
    for j in range(0,i-1):
        print("*", end=' ')
    print(" ")

# QUESTION 12.
print()
print("Question 12.")       
print()
star = 5
for i in range(0, star):
    for j in range(0, i+1):
        print("*", end= ' ')
    print(" ")
for i in range(star, 0, -1):
    for j in range(0,i-1):
        print("*", end= ' ')
    print(" ")
    
    
# QUESTION 13.
print()
print("Question 13.")       
print()

star = 5
i=1
while i <= star:
    j = i
    while j<star:
        print(' ',end=' ')
        j +=1
    k =1
    while k <= i:
        print("*",end=' ')
        k+=1
    print()
    i+=1
    
i = star
while i>=1:
    j=i
    while j <= star:
        print(" ",end =" ")
        j +=1
    k = 1
    while k < i:
        print("*", end =" ")
        k+=1
    print(" ")
    i-=1


# QUESTION 14.
print()
print("Question 14.")       
print()

star = 5
i=0
while i <= star-1:
    j = 0
    while j<i:
        print('',end=' ')
        j +=1
    k =i
    while k <= star-1:
        print("*",end=' ')
        k+=1
    print()
    i+=1
    
i = star-1
while i>=0:
    j=0
    while j < i:
        print("",end =" ")
        j +=1
    k = i
    while k <= star-1:
        print("*", end =" ")
        k+=1
    print("")
    i-=1
    
# QUESTION 15.
print()
print("Question 15.")       
print()    

star = 16
print("*" * star, end ="\n")
i = (star //2 )-1
j=2
while i !=0:
    while j<= (star-2):
        print("*" * i,end='')
        print("_" * j, end='')
        print("*" * i,end="\n")
        i = i-1
        j = j +2

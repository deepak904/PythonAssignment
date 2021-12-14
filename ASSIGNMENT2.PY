# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:42:31 2021

@author: Deepak Kumar
@emailid: deepak.iafjnv@gmail.com

#Task 2
FULL NAME: DEEPAK KUMAR

"""

# Question 1 -
import os
def GCD_Loop( a, b):  
    if a > b:  # define the if condition  
        temp = b  
    else:  
        temp = a  
    for i in range(1, temp + 1):  
        if (( a % i == 0) and (b % i == 0 )):  
            gcd = i  
    return gcd  

x = int(input (" Enter the first number: "))    
y =int (input (" Enter the second number: "))    
num = GCD_Loop(x, y)  
os.chdir(r"c:\\")
f=open('gcd_data.txt','w+')
f.write(f"Greatest Common Divisor of {x} and {y} is {num}")
f.close()


# Question 2 -
# Please create a deepak.txt file with some content
fileObj = open("deepak.txt","w+")
fileObj.seek(15)
print("Pointer is at byte ",fileObj.tell() )


fileObj.write("Writing starts after 15 bytes")


fileObj.close()

fileObj = open("deepak.txt","r")
output = fileObj.read()
fileObj.close()
print(output)


# Question 3 -
import re
 
def main():
    passwd = 'Geek12@'
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,15}$"
     
    pat = re.compile(reg)
                   
    mat = re.search(pat, passwd)
     
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")
   
if __name__ == '__main__':
    main()
    
    

# Question 4 -
import string

for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)
       f.close()

print("File created successfully!")           

# Question 5 -
# create first.txt and second.txt with content
with open('first.txt','r') as fh1, open('second.txt','r') as fh2, open('third.txt','w+') as fh3:
    fh1_lines = fh1.readlines()
    fh2_lines = fh2.readlines()
    
    for i in range(len(fh1_lines)):
        lines = fh1_lines[i].strip() +" "+fh2_lines[i]
        
    fh3.write(lines)
    fh3.close()
    
# Question 6 - 
import datetime
import json
from selenium import webdriver

import time

eleNM = None

def wish_birth(name):
    return "Happy Birthday " + name.split(" ")[0] + "!!"

# This function returns a list of values of some
# attribute based on conditions on two attributes from the JSON file.
# use to return names of contacts having their birthday on current date.
def getJsonData(file, attr_ret, attr1, attr2, attr_val1, attr_val2):

# Load the file's data in 'data' variable
    data = json.load(file)
    retv =[]

# If the attributes' value conditions are satisfied,
# append the name into the list to be returned.
    for i in data:
        if(i[attr1]== attr_val1 and i[attr2]== attr_val2):
            retv.append(i[attr_ret])
    return retv

# Create a file birthday.json and write 20th November, 2021 in it.
data_file = open("birthdays.json", "r")
namev =[]
print("Script Running")

while True:
    try:
# to get current date
        datt = datetime.datetime.now()
        namev = getJsonData(data_file, "name", "birth_month", "birth_date",
str(datt.month), str(datt.day))

    except json.decoder.JSONDecodeError:
        continue
    if(namev !=[]):
        break

chropt = webdriver.ChromeOptions()

chropt.add_argument("user-data-<LOCATION TO YOUR CHROME USER DATA>")

driver = webdriver.Chrome(executable_path ="<LOCATION TO CHROME WEBDRIVER>",
options = chropt)
driver.get("https://web.whatsapp.com/")

time.sleep(10)

print(namev)

# Finds the chat of your contacts (as in the namev list)
for inp in namev:
    try:
        eleNM = driver.find_element_by_xpath('//span[@title ="{}"]'.format(inp))
    except Exception as ex:
        print(ex)
        continue
    eleNM.click()

while(True):
    eleTF = driver.find_element_by_class_name("_13mgZ")
    eleTF.send_keys(wish_birth(inp))
    eleSND = driver.find_element_by_class_name("_3M-N-")
    eleSND.click()
    break

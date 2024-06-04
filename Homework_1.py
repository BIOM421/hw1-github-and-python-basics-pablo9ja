# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:17:28 2024

@author: cyto
"""

#Notebook for Homework 1
# Preliminary Codes -- DO NOT CHANGE ANYTHING IN THIS SECTION
import random, pickle
import numpy as np
xData = [100*random.random() for i in range(20)]
number = 5+random.randint(8,20)
fruit = 'apples'
day = 'Saturday'
string_4 = 'An alacritous abalone accelerates along an alarming aquatic ascent.'
string_5 = 'A                       large space was here.'
string_6 = 'ATCGTGCATGCTGAGTGGCGAGCGGCGGCCGTACGCTGTTACTTAAAACGTAGCTGTAAAAAAC\
            GCTGCTGATGCTGTGCATGTGACTAGCTGCATGTGTGACTGACTGCTGACGTACTGTACGTACG\
            ATGGTTCGTGCGATGCGCTTGACGTGTCGTAGTGCATGCTGCTAGCTGATCGATGTGTCGAGTC'
nDigits = 6
nPower = 3
List10 = ['apples','bananas','pears','pears','blueberries','apples','strawberries']
Student_IDs = [1,2,3,4,5]
Student_names = ['Jim','John','Jenna','Jamal','Jaden']
List12 = [1,2,3,4,5,6,7,8]

q1 = 'xxx'
q2 = 'XXX'
q3 = 'XXX'
q4 = 123
q5 = 'XXX'
q6 = 123
q7 = 'XXX'
q8 = 1.23
q8 = 'xxx'
q9 = 'xxx'
q10 = List10
q11 = 'xxx'
q12 = [1,2,3,4,5,6,7,8]

fnDat = 'Hwk1Data.pkl'
dataDict = {'xData':xData,'number':number,'fruit':fruit,'day':day,'string_4':string_4,
    'string_5':string_5,'string_6':string_6,'nDigits':nDigits,'nPower':nPower,
    'Student_IDs':Student_IDs,'Student_names':Student_names,'List10':List10,'List12':List12}
with open(fnDat, 'wb') as file:
    pickle.dump(dataDict, file)

def saveResults():
    fn = 'Hwk1Answers.pkl'
    answerDict = {'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'q6':q6,'q7':q7,'q8':q8,
                 'q9':q9,'q10':q10,'q11':q11,'q12':q12}
    with open(fn, 'wb') as file:
        pickle.dump(answerDict, file)

    #Read and print 
    with open(fn, 'rb') as file:
        loaded_dict = pickle.load(file)
    
    print("Your answers so far are:")
    print(loaded_dict)
    
#Problem Set 1 - Basic Arithmetic and String Manipulation
# Q1 - Concatenate the following strings with a space inbetween them (do not change the name).
string_1 = 'Hello my name is'
name = 'Name'

q1 = string_1 + " " + name
saveResults()
# Q2 = Convert the following string to uppercase
string_2 = 'i would like to be uppercase'

q2 = string_2.upper()
saveResults()
# Q3 - use string formatting to construct the following string: 
#. "I bought [number] [fruit] on [day]." where:
#     [number] is replaced with the number value of the variable "number",
#     [fruit] is replaced with the string value of the variable "fruit",
#     [day] is replaced with the string value of the variable "day",
print(number)
print(fruit)
print(day)

q3 = f"I bought {number} {fruit} on {day}."
saveResults()
# Q4 - count the number of a's in the string "string_4"
print(string_4)

q4 = string_4.count('a')
saveResults()
# Q5 - Strip "string_5" to remove all spaces and return the result as 'q5'
print(string_5)

q5 = string_5.replace(" ", "")
saveResults()
# Q6 - How long is the string "string_6"?

q6 = len(string_6)
saveResults()
# Q7 - Write a STRING that contains the value of pi^[nPower]. 
# Use exponent form to the 3rd decimal point (e.g., 2.500e+00).
pi = np.pi
print(pi)
print(nDigits)
print(nPower)
q7 = pi**nPower
saveResults()
#Problem Set 2 - Iterables, Slicing, and Sets
# Q8 - Consider the numbers in the list "xData", and compute their average.
print(xData)
 # Change this to produce the average of the numbers in 'xData'
q8 = sum(xData) / len(xData)

saveResults()
# Q9 - What's the last entry in the list "xData".  Get this by slicing the list.
print(xData)

q9 = [xData[-1]]
saveResults()
# Q10 - Convert between lists and sets to remove duplicate entries from the list "List10"
print(List10)

q10 =  list(set(List10))
saveResults()
# Q11 - Combine the lists 'Student_IDs' and 'Student_names' into a dictionary keyed by the IDs. 
# i.e. Create a dictionary with pairs of { ID : student name }
print(Student_IDs)
print(Student_names)

student_dict = {id: name for id, name in zip(Student_IDs, Student_names)}

q11 = student_dict
saveResults()
# Q12 - Slice to get every other entry in the list 'List12'
print(List12)
q12 = List12[::2]

saveResults()



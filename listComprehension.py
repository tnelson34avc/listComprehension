# -*- coding: utf-8 -*-
"""
Created on thur 8 20:05:32 2022

@author: ya boy

third assignment: list comprehensions

9/8/2022 (september)
"""

import numpy as np
import random as ran

'''
1. Writes a list comprehension that prints a list of the cubes of the numbers 1 through 10.
'''
onetoten = []
for x in range(1,11):
  onetoten.append((x**3))
print('\ngo fuck yourself {}'.format(onetoten))




'''2. Write a list comprehension that prints out the possible results of two coin flips (one result would be ’ht’).
(Hint - how many results should there be?)'''
flips=[]
for x in range(0,2):
  r = ran.randrange(0,2)
  if r==1:
    flips.append('t')
  elif r==0:
    flips.append('h')
  else:
    print('you fucked up')
print('\nyour flips are {}'.format(flips))




'''4. Run this list comprehension 
[x+y for x in [10,20,30] for y in [1,2,3]] and figure out what is going on here,.   Next, write a nested for loop that gives you the same result. 
This will show you've explained what the comprehension does 
'''
dafuck=[x+y for x in [10,20,30] for y in [1,2,3]]
print('\nwhat is dafuck {}'.format(dafuck))

fucks=[]
nani = 0
for x in range(1,4):
  nani+=10
  for x in range(1,4):
    fucks.append(nani+x)
print('\nnumber of fucks is {}'.format(fucks))






'''3. Write a function that takes in a string and uses a list comprehension to return all the vowels in the string.'''
dfordickbag = input('\ntype in your sentence whore: ')
c =0
for x in dfordickbag:
  if x == 'a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='y':
    c+=1
print('\nthe number of dicks in the bag is {}'.format(c))








'''
onetoten = [1,2,3,4,5,6,7,8,9,10] #np.linspace(1,10,9)#starting num, ending number, number of number

def cubethem(onetoten):
  for i in range(11):
    onetoten[i] = i**3 
  print('1 - 10 cubed is {}'.format(onetoten))
  return 

cubethem(onetoten)
'''
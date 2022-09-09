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
print('\nthe list is {}'.format(onetoten))




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
    print('you messed up')
print('\nyour flips are {}'.format(flips))




'''4. Run this list comprehension 
[x+y for x in [10,20,30] for y in [1,2,3]] and figure out what is going on here,.   Next, write a nested for loop that gives you the same result. 
This will show you've explained what the comprehension does 
'''
dis = [x+y for x in [10,20,30] for y in [1,2,3]]
print('\nwhat is dis {}'.format(dis))

copy=[]
nani = 0
for x in range(1,4):
  nani+=10
  for x in range(1,4):
    copy.append(nani+x)
print('\nnumbers in the list {}'.format(copy))






'''3. Write a function that takes in a string and uses a list comprehension to return all the vowels in the string.'''
line = input('\ntype in your sentence: ')
c =0
for x in line:
  if x == 'a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='y':
    c+=1
print('\nthe number of vowels in the string is {}'.format(c))








'''
onetoten = [1,2,3,4,5,6,7,8,9,10] #np.linspace(1,10,9)#starting num, ending number, number of number

def cubethem(onetoten):
  for i in range(11):
    onetoten[i] = i**3 
  print('1 - 10 cubed is {}'.format(onetoten))
  return 


cubethem(onetoten)
'''

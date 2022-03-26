import random

chances = 5
Realnum = random.randint(1,9)

A1 = int(input('What is the number? '))
chances = chances - 1
if Realnum == A1:
  print('You won')
else:
  if Realnum > A1:
    print('Too low.')
  if Realnum < A1:
    print('Too high.')
  A2 = int(input('What is the number? '))
chances = chances - 1
if Realnum == A2:
  print('You won')
else:
  if Realnum > A2:
    print('Too low.')
  if Realnum < A2:
    print('Too high.')
A3 = int(input('What is the number? '))
chances = chances - 1
if Realnum == A3:
  print('You won')
else:
  if Realnum > A3:
    print('Too low.')
  if Realnum < A3:
    print('Too high.')
A4 = int(input('What is the number? '))
chances = chances - 1
if Realnum == A4:
  print('You won')
else:
  if Realnum > A4:
    print('Too low.')
  if Realnum < A4:
    print('Too high.')
A5 = int(input('What is the number? '))
chances = chances - 1
if Realnum == A5:
  print('You won')
else:
  if Realnum > A5:
    print('Too low.')
  if Realnum < A5:
    print('Too high.')
if chances == 0:
  print('You lost. The real number is', Realnum)
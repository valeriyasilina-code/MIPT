"""Exercise 1: Print First 10 natural numbers using while loop
"""

# add your code
i=1
while i<=10:
  print(i)
  i+=1



"""Exercise 2: Max element

Input: a list of integers
Output: max element
"""

# input
l = [1, 10, 15, 20, 11, 14]
mx=l[0]
for el in l:
  if el>mx: mx=el
print(mx)

# add your code






"""Exercise 3: Find the factorial of a given number (using for loop)
"""

# input
n = 4

# add your code
f=1
for i in range(2,n+1):
  f*=i
print(f)







"""Exercise 4: Display Fibonacci series up to 10 terms

Output: [0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

# add your code

fib=[0,1]
while len(fib)<9:
  fib.append(fib[len(fib)-1]+fib[len(fib)-2])
print(fib)








"""Exercise 5: Print the following pattern (with different n)

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""

# input
n = int(input())
for i in range(1,n):
  print("* "*i)
for i in range(n,0,-1):
  print("* "*i)

# add your code








"""
Exercise 6: The input to the program is a integer number 'n'.
Write a program that prints the numbers through 'n', inclusive, except:

- numbers from 5 to 9 inclusive;
- numbers from 15 to 20 inclusive;
- numbers from 25 to 35 inclusive.
"""

# input
n = 50

# add your code
for i in range(1,n+1):
  if (not (5<=i<=9 or  15<=i<=20 or  25<=i<=35)):
    print(i)








"""
Exercise 7: Robot Return to Origin.

There is a robot starting at the position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot
where moves[i] represents its ith move.

Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return True if the robot returns to the origin after it finishes all of its moves, or False otherwise.

Note: The way that the robot is "facing" is irrelevant.
'R' will always make the robot move to the right once,
'L' will always make it move left, etc.
Also, assume that the magnitude of the robot's movement is the same for each move.

EXAMPLE 1:
Input: moves = "UD"
Output: True
Explanation: The robot moves up once, and then down once.
All moves have the same magnitude, so it ended up at the origin where it started.
Therefore, we return True.

EXAMPLE 2:
Input: moves = "LL"
Output: False
Explanation: The robot moves left twice.
It ends up two "moves" to the left of the origin.
We return False because it is not at the origin at the end of its moves.

EXAMPLE 3:
Input: moves = "RRDD"
Output: False

EXAMPLE 4:
Input: moves = "LDRRLRUULR"
Output: False

Keywords: list, string, for, if, elif, else!
"""

# input
moves = "UD"

# add your code
x=0
y=0
for i in moves:
  if i=="L":x-=1
  elif i=="R": x+=1
  elif i=="U": y+=1
  else: y-=1
if x==0 and y==0:
  print(True)
else:
  print(False)









# input ВТОРОЙ ВАРИАНТ
moves = "LRDU"

# add your code
x=[]
y=[]
for i in moves:
  if i=="L":x.append(1)
  elif i=="R": x.append(-1)
  elif i=="U": y.append(1)
  else: y.append(-1)
if sum(x)==0 and sum(y)==0:
  print(True)
else:
  print(False)

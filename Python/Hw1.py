"""1. Celsius and Fahrenheit Converter

Description: To convert temperature between Fahrenheit to Celsius and Celsius to Fahrenheit
"""

temp = float(input())
cels = (temp * 9/5) + 32
far = (temp - 32) * 5/9
print(f"Если Вы ввели температуру по Фаренгейту, то это {cels} по Цельсию. Если Вы ввели температуру по Цельсию, то это {far} по Фаренгейту.")






"""2. Road tax
Description: Write a program to accept the cost price of a bike and
             display the road tax to be paid according to the following criteria.

Cost price (in Rs)                Tax
   > 100_000                      15%
   > 50_000 and <= 100_000        10%
   <= 50_000                      5%
"""

price = float(input())
if price > 100000:
  print(f"Налог составит {price*0.15} рублей")
elif 50000<price<=100000:
  print(f"Налог составит {price*0.1} рублей")
else:
    print(f"Налог составит {price*0.05} рублей")






"""3. Data Format (Yandex Contest)

Description:
As you know, there are two most common date formats:
- European (first day, then month, then year)
- American (first month, then day, then year)

The system administrator changed the date on one of the backups and now wants to return the date back.
But he did not check what format the date is in the system.

In other words, you are given a record of some correct date.
It is required to find out whether the date is uniquely determined from this record.

INPUT:
Three integers x, y, z:
1 <= x <= 31, 1 <= y <= 31, 1970 <= z <= 2069.
It is guaranteed that at least one format the xyz entry specifies the correct date.

OUTPUT:
Print 1 if the date is uniquely determined, and 0 otherwise.


Test Case 1:
INPUT:
x = 1
y = 2
z = 2003

OUTPUT: 0

Test Case 2:
INPUT:
x = 2
y = 27
z = 2008

OUTPUT: 1

Description of the test cases:
In the first test case:
- with one recording system, the date is February 1, 2003;
- with the other - January 2, 2003.
It is impossible to name the date uniquely.


In the second test case:
the correct version of the date can be only American format: February 29, 2008.
"""
x=int(input())
y=int(input())
year=int(input())
if 1<=y<=12 and 1<=y<=12:
  print(0)
else:
  print(1)


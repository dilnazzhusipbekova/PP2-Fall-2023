#task 1
import math 

a = [12, 5, 56]
b = math.prod(a)
print(b)

#task 2
a = str(input())

count_u = 0
count_l = 0

for i in a:
    if(i.islower() == True):
        count_l += 1
    elif(i.isupper() == True):
        count_u += 1

print("Count of uppercase letters is ", count_u)
print("And count of lowercase letters is ", count_l)

#task 3
a = "heey"
a1 = "hello"
# a = str(input())
b = ''.join(reversed(a))
b1 = ''.join(reversed(a1))

if a == b: 
    print("Yes, I'm palindrome")
else:
    print("No, I'm not a palindrome")
"""
if a1 == b1: 
    print("Yes, I'm palindrome")
else:
    print("No, I'm not a palindrome")
"""

#task 4
"""
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858"""

import time
import math

n = int(input("Enter ur number: "))
ms =float(input("Enter the milliseconds: "))

time.sleep(ms/1000)
print("It took me {} ms, the square root is {}".format(ms,math.sqrt(n)))

#task 5

a = (12, 15, True, "Hello", 'World', [12,1,3])
b = ("", '', 0,[])

print(all(a)) # TRUE
print(all(b)) # FALSE


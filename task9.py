'''
Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math
n = 150
a, b = 0, 0
for i in range(int(n/2)):
    if a + b + math.sqrt(a**2 + b**2) == n:
        break
    a += 1
    b = a + 1
    for j in range(b, int(n/2)):
        b = j
        c = math.sqrt(a**2 + b**2)
        if c.is_integer() and a + b + c == n:
            print(a * b * int(c))
            break

if int(a + b + math.sqrt(a**2 + b**2)) != n:
    print('Not found')

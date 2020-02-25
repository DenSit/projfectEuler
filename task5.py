'''
Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def divider(n, m):
    for i in range(2, m + 1):
        if n % i != 0:
            return True
    return False


# m = int(input())
m = 20
n = m
while divider(n, m) is True:
    n += m

print(n)

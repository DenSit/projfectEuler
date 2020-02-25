'''
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def prime(num):
    k, j = 2, 0
    while k ** 2 <= num and j != 1:
        if num % k == 0:
            j = 1
        k += 1
    return j


n = int(input())
divider = 1
while True:
    divider += 1
    i = n / divider
    if i.is_integer() and i % 2 != 0:
        if prime(i) != 1:
            break
print(int(i))


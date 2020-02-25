'''
Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def prime(num):
    k, j = 3, 0
    while k*k <= num and j != 1:
        if num % k == 0:
            j = 1
            break
        k += 2
    return j


n = 2000000  # n =int(input())
if n % 2 == 0:
    n -= 1
summ = 0
for i in range(n, 1, -2):
    if i % 5 != 0:
        if prime(i) == 0:
            summ += i

print(summ + 7)


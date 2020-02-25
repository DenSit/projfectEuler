'''
10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def prime(num):
    k, j = 2, 0
    while k**2 <= num and j != 1:
        if num % k == 0:
            j = 1
        k += 1
    if j != 1:
        return True


n = 10001
counter = 6
prime_num = 13
while counter < n:
    prime_num += 2
    if prime(prime_num) is True:
        counter += 1
print(prime_num)
'''
Largest palindrome product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def simmetry(num):
    while num > int('1' + '0'*n + '1'):
        half = str(num)[:n]
        half_num = int(half)-1
        num = int(str(half_num) + str(half_num)[::-1])
        sim_num.append(num)


n = int(input())
if n == 1:
    print(9)
else:
    x = (int('9'*n))**2
    for i in range(n):
        while str(x)[i] != str(x)[-(i + 1)]:
            x -= 10**i
    sim_num = []
    simmetry(x)
    matches = []
    for j in range(1, 10**n):
        for i in range(1, 10**n):
            if j * i in sim_num:
                matches.append(j*i)
    print(max(matches))




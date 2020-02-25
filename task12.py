'''
Highly divisible triangular number
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''


def dev(num):
    count = 2  # любое число по-любому делится без остатка на себя и единицу
    i = 2
    while i < num / i:  # если число делится на другое число, то оно будет делиться и на результат от деления
        if num % i == 0:
            count += 2  # значит прибавляем сразу 2 делителя
        i += 1
    if i == num / i:  # на случай если делитель и частное равны
        count += 1
    return count


n = int(input())  # n = 500

triangle_num, add = 1, 1
while dev(triangle_num) <= n:
    add += 1
    triangle_num += add  # получаем труеугольные числа
print(triangle_num)
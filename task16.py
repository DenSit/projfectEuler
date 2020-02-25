'''
Power digit sum
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
'''

num, degree = 2, 1000
string = str(num**degree)
summa = 0
for i in string:
    summa += int(i)
print(summa)


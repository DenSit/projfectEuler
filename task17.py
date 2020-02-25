'''
Number letter counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and"
when writing out numbers is in compliance with British usage.
'''


def f(n):
    s = 0
    if n[0] == '0':
        s += hundreds[n[1]]
    elif n[0] == '1':
        s += teens[n]
    else:
        s += decades[n[0]] + hundreds[n[1]]
    return s


start, end = (input().split())
hundreds = {'1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4, '0': 0}
teens = {'10': 3, '11': 6, '12': 6, '13': 8, '14': 8, '15': 7, '16': 7, '17': 9, '18': 8, '19': 8}
decades = {'2': 6, '3': 6, '4': 5, '5': 5, '6': 5, '7': 7, '8': 6, '9': 6}


lst = [str(x) for x in range(int(start), int(end) + 1)]
summa = 0
for number in lst:
    if len(number) == 1:
        summa += hundreds[number]
    elif len(number) == 2:
        summa += f(number)
    elif len(number) == 3:
        summa += hundreds[number[0]] + 10
        if number[1:] == '00':
            summa -= 3
        number = number[1:]
        summa += f(number)
    elif number == '1000':
        summa += 11
print(summa)


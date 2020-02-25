'''
Counting Sundays
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
          8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def leap_year(year):  # проверка на високосность
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def rest_year(year):  # остаток до конца года от первой даты
    months[2] += leap_year(year)
    rest_y = sum(months.values()) - (sum([months[i] for i in range(1, month1)]) + day1)
    months[2] -= leap_year(year)
    return rest_y


def step(i):  # возвращает количество дней в текущем месяце
    while True:
        yield months[i]
        if i < 12:
            i += 1
        else:
            i = 1

# высчитываю ближайшее воскресенье до начала первой даты:


year1, month1, day1 = 2001, 1, 1
year2, month2, day2 = 2019, 3, 31

sunday = 0
for y in range(1900, year1):
    sum_days = sum(months.values())
    if leap_year(y):
        sum_days += 1
    while sunday <= sum_days - 7:
        sunday += 7
    sunday = sunday - sum_days
sum_days = 0
for j in range(1, month1 + 1):
    sum_days += months[j]
    if j == 2:
        if leap_year(year1):
            sum_days += 1
sum_days += day1 - 1
while sunday <= sum_days - 7:
    sunday += 7
sunday = sunday - sum_days

# количество дней на искомом периоде
period = rest_year(year1)
for y in range(year1 + 1, year2):
    months[2] += leap_year(y)
    period += sum(months.values())
    months[2] -= leap_year(y)
period += rest_year(year2)

lst_sundays = [i for i in range(sunday, period, 7)]  # список воскресений в искомом периоде

lst_months = [months[month1] - day1]
count = months[month1]
this_year = year1
for i in step(month1 + 1):
    if i == 28:
        if leap_year(this_year):
            i += 1
        this_year += 1
    count += i
    if count < period:
        lst_months.append(count)
    else:
        break

print(len(set(lst_sundays) & set(lst_months)))

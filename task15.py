'''
Lattice paths
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''

n = int(input())
d = {1: [1 for i in range(n)]}
for i in range(2, n + 1):
    for j in range(n):
        d[i] = d.get(i, []) + [sum(d[i - 1][j:])]

summa = 1
for i in d.values():
    summa += sum(i)
print(summa)

# second way
# But long execution:

'''
n = int(input())
def summa_1(num):
    return num

rows = summa_1(n)

for i in range(2, n + 1):
    exec(f'def summa_{str(i)}(num):\n s = 0\n for i in range(num):\n  s += summa_{str(i-1)}(num - i)\n return s')
    exec(f'rows += (summa_{str(i)}(n))')
print(rows + 1)

'''


pets = ['bob', 'jon', 'eli', 'bonhowser']

def print_list(pets):
    for i in range(0, len(pets)):
        print(pets[i])

print_list(pets)

"""
"""

boo = [3, 4, -3, -7]

for i in range(0, len(boo)):
    a = int(boo[i]) + i
    boo[i:i+1] = [a]

print(boo)

"""
"""
boo = [3, 5, -2, 8, -4, 5]

a = 0
for i in range(0, len(boo)):
    if int(boo[i]) < a:
        a = int(boo[i])

print(float(a))

"""


"""
from random import *

n = int(input('Give number: '))

boo = []

for i in range(n):
    boo.insert(i, randint(0, 1))

print(boo)
"""
"""
boo = [0, -23, 12, 4, 62]

a = 0 

for i in range(0, len(boo)):
    if int(boo[i]) > a:
        a =int(boo[i])


print(a)
"""
"""
boo = ['bol', 'grdg', 3]

a = 0
while a < 2:
    boo.append(boo[0])
    print(boo)
    boo.remove(boo[0])
    print(boo)
    a+=1

print(boo)
    
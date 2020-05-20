

# print(int('3'))

# print(int('4.2'))

# print(int('1001',10))

# print(float('3'))

# print(float(5))

# print(str(0))


#print('give 2 numbers')
#first = input()
#second = input()

#print('what do you want to do? add, substract, multiply, or divide?')

#bob = input()

# if bob == "add":
#   print(int(first) + int(second))
# elif bob == "substract":
#  print(int(first) - int(second))
# else :
#   print("we cannot do that")

"""print('Type a 4 digit number')

num = input()

a = int(num)//1000

b = int(num)%1000//100

c = int(num)%100//10

d = int(num)%10
print(str(a) + '*10^3 ' + '+ ' + str(b) + '*10^2' + ' + ' + str(c) + '*10' + ' + ' + str(d))


print('type a 3 digit number, i will give its base 5 number...')

num2 = input()

a = int(num2)

b = (a//100)*(5**2)

c = (a%100//10)*5

d = a%10

print('The base 5 number of ' + str(num2) + ' is ' + str(b) + '+' + str(c) + '+' + str(d) + '=' +str(b+c+d))
"""
"""print('give number ')

num = input()

while num != 0:
    print(str(int(num)%2))
    num = int(num)//2"""
"""import math

print('give binary number')
 
num = list(input("Input a binary number: "))
value = 0
for i in range(len(num)):
	digit = num.pop()
	if digit == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)"""
"""
x = input('Give first: ')
a = x 
y = input('Give second: ')
b = y
print('x was ' + str(x) +' and y was ' + str(y))
x = int(b)
y = int(a)
print('x is now ' + str(x))oopsa'''
print('y is now ' + str(y))"""
"""
x = input('Give a number: ')
y = input('Another: ')
z = input('Last one: ')

a = x < y < z

if int(y) % 2 == 0 and a == True:
    print('True')
else:
    print(str(a) + ', it is not even')"""
"""
F = input('Give Fah temp: ')
C = (int(F)-32)*5/9
print(int(C))"""
"""
x = input('Give first: ')
a = x 
y = input('Give second: ')
b = y
print('x was ' + str(x) +' and y was ' + str(y))
x = int(b)
y = int(a)
print('x is now ' + str(x))
print('y is now ' + str(y))"""
"""
import random 
min = random.randint(-100, 0)
print('Min is: ' + str(min))
max = random.randint(0, 100)
print('Max is: ' + str(max))
print('Number chosen is: ' + str(random.randint(min, max)))
"""

"""
from math import *

def f(a):
    return factorial(a)


result = 1
for i in range(1, 7):
    result = result*f(i)
    
print('Your chances of winning are: ' + str(floor(1/result)))
"""
"""
num = input('Give your number: ')

if int(num)%2 == 0:
    print('Your number is even.')
else:
    print('Odd')
    """
"""
x = input('Give first number: ')
y = input('Give other number: ')

if int(x) % int(y) == 0:
    print(x + ' is a multiple of ' + y)
else:
    print('Nope')
"""
"""
x = input('First: ')
y = input('Second: ')

a = int(x) % int(y) == 0

print(a)
"""
"""
x = input('First: ')
y = input('sECOND: ')

a = 10 - int(x)
b = 10 - int(y)

if a > b:
    print(y + ' is the closer number.')
elif b > a:
    print(x + ' is the closer number.')
else:
    print('0') 

"""
"""

m = input('Give length: ')
n = input('Give height: ')

a = input('Give character: ')

leng = a * int(m)  
for i in range(int(m)):
    print(a, end= '')

for i in range(int(n)):
    print(str(leng))


"""
"""
from math import *


def area_of_circle(radius):
    return (pi * pow(radius, 2.0))

print (area_of_circle(2.2))
"""


"""
from random import *

die_one = 6
die_two = 10
die_three = 20

seed(12)

print(randint(1, die_one))
print(randint(1, die_two))
print(randint(1, die_three))
"""
"""
x = input('Give first: ')
y = input('Give second: ')

if int(x) > int(y):
    print('The second number must be bigger.')
i = 1
while int(x) * i < int(y):
   
    print(int(x) * i, end = ' ')
    i += 1
"""
"""

from random import *

num = randint(1, 100)

guess = input('Guess the number boi: ')

count = 0

if int(guess) == int(num): 
    print('You guessed it in 1 try, the number was ' + str(num))


while int(guess) != num:
    if int(guess) > num:
        guess = input('Too high, try again: ')
        count += 1
    elif int(guess) < num:
        guess = input('Too low, try again: ')
        count += 1
    
if int(guess) == num:
        print('Mmmmm, you got it in ' + str(count) + ' tries. The number was ' + str(num))

"""
"""
x = input('Give first: ')
y = input('Give second: ')

if x == y :
    print('The greatest common denominator is: ' + x)
else:
    if x > y:
        den = int(y)
        while int(x) % den != 0 or int(y) % den != 0:
            den -= 1
        print('The greatest denonminator is ' + str(den))
    elif y > x:
        den = int(x)
        while int(y) % den != 0 or int(x) % den != 0:
            den -= 1
        print('The greatest denominator is ' + str(den))

"""
"""
x = input('Give first: ')
y = input('Give second: ')

if x == y :
    print('The least common multiple is: ' + x)
else:
    if x > y:
        mul = int(y)
        while mul % int(x) != 0 or mul % int(y) != 0:
            mul += 1
        print('The least multiple is: ' + str(mul))
    elif y > x:
        mul = int(x)
        while mul % int(y) != 0 or mul % int(x) != 0:
            mul += 1
        print('The least multiple is: ' + str(mul))
"""


"""
low-level languages

spoken by computer: machine directly understood by computer and assembly 

high level 
englsih, python

compiler translates program writen in high-level language into machine code

interpreter translates source code during execution

statement line of code that performs a basic operation

variable is a named location that stores a value

location a place in the memory of the computer 

command line arguments inputs we provide to teh program before the program is run 

function block of code that performs a task

module is a file that contains a collection of related functions 

scope of variable is part of code where it exists
local inside a functions body
global outside function

docstring string that we write after the header of a function to explain how the 
function works
 


""'

x = 3 
def f(x):
    x = x*5
    print(x)

f(x)

x = input('Small')
y = input('Large')
z = input('You want')

def chocolate(x, y, z):
    if int(x) + 5 * int(y) < int(z):
        print('-1')
    elif z :
        y = 5 * y
        

chocolate(x, y, z)
"""
"""
x = int(input("small chocc "))
y = int(input("big chocc "))
z = int(input("you want "))

def chocolate_bag(x,y,z):

    if (5 * y + x < z):
        print(-1) 

    while z > 0:
        if( z < 5 ):
            break
        z -= 5
        y -= 1
        
        if z > x:
            print(-1)
    
    print(x)


print(chocolate_bag(x, y, z))
"""
"""
from math import *
rad = int(input('What is your radius? '))

def volume(rad):

    vol = 4/3 * pi * rad**3

    return vol

print('Your volume is ' + str(floor(volume(rad))))

"""
"""
a = 0

for i in range(5):
    a += i

b = 1

for l in range(5):
    b *= i


print(a, b)

"""

"""
num = int(input('GIve bumebr: '))

def prime(num):

    a = 2
    while a <= num :
        
        if a == num:
            print('Prime')
            break
        elif num % a == 0 :

            print('Not prime')
            print('It is divisible by ' + str(a))
            break  
        
        
        a += 1
    
prime(num)
"""
"""
n = int(input('Give first '))

m = int(input('Give second '))


def multiples():

    for i in range(0, m+1):
        mul = i * n 
        print(mul)


multiples()
"""


"""
x = int(input('Leng '))

y = int(input('Hei '))

def table():
    
    for i in range(1, x+1):
        
        len = 1 * i 
        print(len, end=' ')

table()

a = 1
    
while a <= y+1 :
            
    hei = a * 2
    print(hei, end=' ')
        
    a += 1

"""
"""
word = input('Give word ')
letter = input('Give letter you want: ')


def count():

    a = 0
    for char in word:
        if char == letter:
            a += 1
        
    print(a)

count()

"""
"""
word = input('Give word: ')
letter = input('give letteer: ')

def remove():
    for char in word:
        if char == letter:
            continue
        print(char, end='bruh')
    
remove()
"""
"""                        
bam = input('gw ')

def potato():
    print(bam * 5)

potato()

word = input('Give word: ')

def count():
    for char in word:
        char = a
        if 


def remove():  
"""
"""
string = 'booboobaa'

substring = 'a'

count = string.count(substring)

print(count)
"""
"""
#for i in range(0, y+1):
 #   print()

word = input('Give word: ')

def remover():
    for char in word:
        count = word.count(char)
        if count == 1:
            print(str(count) + ' ' + char)
        elif count > 1:
            print(char)
            break
        

remover() 
"""
"""
letter = input('Give letter ')
vowels = 'aeiou'

a = 0

for char in letter:
    a += 1 
    

if a > 1:
   print('One letter only')

else:
    b = letter in vowels
    print( b )

"""
"""
word = input('Give word ')
vowel = 'aeiou' 


def vowels():
    
    a = 0

    for char in word:
        if (char in vowel) == True: 
            a += 1
        
    print(a)

vowels()
"""

"""

word = 'apple'

a = -1

for char in word:

    b = word.find(char, a+2 , len(word) + 1)
    c = word.find(char, 0, a)

    
   # print('this is a ' + str(a))
   # print('this is b ' + str(b))
   # print('this is c ' + str(c))
    

    if b == -1 and c == -1:
        print(char, end=' ')
    elif b > -1 and c > -1:
        print(char, end=' ')
    elif c == -1:
        print(char, end=' ')
    elif a == -1:
        print(char, end=' ')
    
    a += 1
    
"""

"""
def find():

    word = 'koala'
    letter = 'g'
    
    a = word.find(letter)
    if a == -1:
        print(len(word))
    else:
        print(a)
    
find()
"""
"""
def remover():

    word = 'i am saba'

    for char in word:

        if char == ' ' :
            continue
        
        else:
            print(char, end='')

remover()
"""
"""
n = int(input('first '))
m = int(input('second '))

a = n
for i in range(m):

    print(a)
    a += n
"""
"""
for i in range(1, 5):
    j = 0
    while (j < i):
        print('*', end= ' ')
        j += 1
    print()

"""
"""
from math import *
num = 0
result = False
while not result:
    try:
        num = int(input('Give number:--> '))
        result = True
    except ValueError:
        print("That is not an integer Try again.")



def primes():
    for i in range(num):

        for j in range(1, i-1):
            
            if i % j == 0:
                print('not prime')
              

primes()
"""
"""
def primes(N):

    i, j, flag = 0, 0, 0;

    for i in range(1, N + 1, 1):

        if (i == 1 or i == 0) :
            continue
        
        flag = 1

        for j in range(2, ((i // 2 ) + 1)):
            if (i % j == 0):
                flag = 0
                break

        if (flag == 1):
            print(i, end = ' ')

N = 100
primes(N)

"""

"""
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
    
"""
"""
word = 'potato'


for i in range(len(word)):
    
    print(word[ i ] in word[ i +1 :  ])
    if i == 0:
        print(word[ i ])
    
    if word[ i ] in word[i  : -1] == True or False:
        print(word[ i ])

"""
"""
for i in range(6):
    for j in range(8):
        print(i * j, end = '  ')

    print()
"""

"""
s = 'apple'

def mystery(s):
    t = ""
    for i in range(len(s)):
        for c in s:
            t += c
    return t

print(mystery(s))

"""
"""
def display(name):

    print(name)
    print(name)

name = input('giev')

display(name)
"""

"""

"""

# do the star diagonal thing
# first n primes
"""
lis = [3, 5, 5, 9, 0]
a = len(lis)/2
b = len(lis)/2 +1 
for a in lis[a:b]:
    print(a)

"""
"""


x = int(input('Give first: '))
y = int(input('Give second: '))


for i in range(1, x+1):
    j = 0
    while (j < i):
        print(i * j, end= ' ')
        j += 1
    print()


def primes(N):
    
    lis = []
    i, j, flag = 0, 0, 0;

    for i in range(1, N + 1, 1):

        if (i == 1 or i == 0) :
            continue
        
        flag = 1

        for j in range(2, ((i // 2 ) + 1)):
            if (i % j == 0):
                flag = 0
                break

        if (flag == 1):
            lis.append(i)

    print(lis)


N = 100
primes(N)


"""
"""

def display():
    
    print('Welcome, you want food? ')
    print('We got these things: \n 1. Candy Bar: $2.95 \n 2. Cookies: $3.90 \n 3. Soda: $4.00 \n 4. Chips $3.90 \n 5. No food ')
    


def prices():

    x = int(input('\nGive your choice  '))
    print('The price of your choice is', end=' ')
    if x == 1:
        print(295)
    elif x == 2:
        print(390)
    elif x == 3:
        print(400)
    elif x == 4:
        print(390)
    elif x >= 5:
        print(0)

def coins(price, value, available):

    x = 0
    sum = 0
    
    while (x < available) and ((sum + value) <= price):

        x += 1
        sum += value
        
    print(x)
    

def change():

    
    x = float(input('How much money in dollars you got?  '))
    x = x * 100
    print('\nYou have ' + str(int(x)) + ' cents.')

    too = 200
    t = 0
    loo = 100
    l = 0
    quart = 25
    q = 0
    dime = 10
    d = 0
    nick = 5
    n = 0


    a = x % 5 == 0

    if x % 5 != 0:
        print('We do not take pennies. Leave.')
    elif int(prices()) > x:
        print('Broke')
    elif x//100 > 10:
        print('We do not have that much money, Bill Gates.')
    else:
        while x > nick:
            while x > dime:
                while x > quart:
                    while x > loo:
                        while x > too:
                            
                            x -= too
                            t += 1
                        
                        x -= loo
                        l += 1
                    
                    x -= quart
                    q += 1
            
                x -= dime
                d += 1
            
            x -= nick
            n += 1

        print('\nHere is your change: ')
        print('Toonies x ' + str(t))
        print('Loonies x ' + str(l))
        print('Quarters x ' + str(q))
        print('Dimes x ' + str(d))
        print('Nickels x ' + str(n))
        

def operation():
    display()
    
    prices()
    
    #coins(1000, 100, 8)
    change()

operation()


"""
"""
from math import *

def display():

    print('Welcome to the pizza time zone...\nThese are the methods:')
    print('A. Quantity Quantfication')
    print('B. Money Mode\n')
      
    mode = input(('Give your method: '))
    mode = str.upper(mode)

    while len(mode) > 1 or ((('A' in mode) == False) and (('B' in mode) == False)):
        print('\nPlease present letter B or A.')
        mode = input('Give your method: ')
        mode = str.upper(mode)


def fair_quantity():

    print('\nYou are now in Quantity Quantification sir. ')
    big = input('What is the diameter of the big pizzas? ')
    small = input('What is the diameter of smaller pizzas? ')
    
    while True:
        try:
            big = int(big)
            small = int(small)
            
            break
        except ValueError:
            print('Give Positive Numbers only please\n')
            big = input('What is the diameter of the big pizza? ')
            small = input('What is the diameter of smaller pizza? ')
            continue
    
    Abig = ((big/2)**2) * pi
    Asmall = ((small/2)**2) * pi
    #print(Abig)
    #print(Asmall)
    num_smalls = 0
    total_area = 0

    if Abig == Asmall:
        print('They are the same size...')
   
    elif Abig < Asmall:
        print('\nYou lied about which was the bigger one...\n')
        Asmall, Abig = Abig, Asmall    

    else:
        while (total_area) <= Abig:

            num_smalls += 1
            total_area += Asmall

        print('You will need at least ' + str(num_smalls) +' of the smaller pizzas to get an equal amount.')

def money_mode():

    print('\nYou\'ve chosen money mode.')
    
    Dbig = input('What is the diameter of the big pizza? ')
    Pbig = input('What is the price of the big one? ')
    Dsmall = input('What is the diameter of the small one? ')
    NumSmall = input('How many small pizzas do you have? ')

    if Dbig > Dsmall:
        print('You lied about the sizes.')
        print('No more calculations for you...')
    else:
        while True:
            try:
                Dbig = int(Dbig)
                Pbig = float(Pbig)
                Dsmall = int(Dsmall) 
                NumSmall = int(NumSmall)
            
                break
            except ValueError:
                print('\nGive Positive Numbers only please\n')
                Dbig = input('What is the diameter of the big pizza? ')
                Pbig = input('What is the price of the big one? ')
                Dsmall = input('What is the diameter of the small one? ')
                NumSmall = input('How many small pizzas do you have? ')
                continue

        Abig = (Dbig/2)**2 * pi
        price_unit =  Abig/Pbig
        total_area_small = (Dsmall/2)**2 * pi * NumSmall
        fair_price = (total_area_small/price_unit)

        print(format(fair_price, '.2f'))

def pizza_operation():

    print('Welcome to the pizza time zone...\nThese are the methods:')
    print('A. Quantity Quantfication')
    print('B. Money Mode\n')
    
    mode = input(('Give your method: '))
    mode = str.upper(mode)

    while len(mode) > 1 or ((('A' in mode) == False) and (('B' in mode) == False)):
        print('\nPlease present letter B or A.')
        mode = input('Give your method: ')
        mode = str.upper(mode)

    if mode == 'A':
        fair_quantity()
    
    else:
        money_mode()

#display()

pizza_operation()
"""
"""
from random import *

def dice_roll():

    x = randint(1,6)
    y = randint(1,6)
    z = x + y
    return z


def second_stage():    
    
    b = pass_line()

    while True:
        

        a = dice_roll()

        if a == 7:
            print(a)
            print('You lose')
            break
        elif a == b:
            print(a)
            break
        else:
            print(a, end=' ')

def can_play():

    x = (input('How much money do you have? '))
    y = (input('Please place your bet here: '))
    
    
    while True:

            try:
                x = float(x)
                y = float(y)
                break            
            
            except ValueError:
                print('\nPlease enter valid numbers\n')
                x = (input('How much money do you have? '))
                y = (input('Please place your bet here: '))
                continue
    
    if y > x:
        print('You have insufficient funds, find coins somewhere...')
        return False    
    else:
        print('\nYou can play\n')
        return True
    
    return x
    return y
    

def pass_line():

    result = dice_roll()

    if result == 7 or result == 11:
        print('A ' + str(result) + ' has been rolled. You win!')
        return True
    elif result == 2 or result == 3 or result == 12:
        print('A ' +str(result) + ' has been rolled. Loser')
        return False
    else:
        print('A ' + str(result) +' has been rolled. Roll again!')
    return result

def play():
    a = can_play()
    if a == False:
        print('done')
    
    if a == True:
        
        a = pass_line()
        
        if a == True:
            print('done')
        elif a == False:
            print('bruh')
        else:   
            second_stage()

play()
"""

def split_in_two(word):

    even = ''
    odd =''
    
    for i in range(0, len(word), 2):
        even += word[i]
    for i in range(1, len(word), 2):
        odd += word[i]

    tuple = (even, odd)
    print(tuple)


from bs4 import BeautifulSoup
import requests
import pandas as pd

 
page = requests.get("http://www.pythonchallenge.com/pc/def/0.html")

page = http://www.pythonchallenge.com

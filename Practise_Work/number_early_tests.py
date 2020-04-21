
num = input('Give your number: ')

if int(num)%2 == 0:
    print('Your number is even.')
else:
    print('Odd')
   
x = input('Give first number: ')
y = input('Give other number: ')

if int(x) % int(y) == 0:
    print(x + ' is a multiple of ' + y)
else:
    print('Nope')

x = input('First: ')
y = input('Second: ')

a = int(x) % int(y) == 0

print(a)



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

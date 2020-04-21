

from math import *


def display():
    # this displays the message of a vending machine
    print('Welcome, you want food? ')
    print('We got these things: \n 1. Candy Bar: $2.95 \n 2. Cookies: $3.90 \n 3. Soda: $4.00 \n 4. Chips $3.90 \n 5. No food ')


def prices():
    # presents prices of foods in machine
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
    # determines amount of coins to return as change
    x = 0
    sum = 0

    while (x < available) and ((sum + value) <= price):

        x += 1
        sum += value

    print(x)


def change():

    # tells person how much change they are going to receive
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
    # calculates how much of each type of change they will return to person
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
        # prints amount of each coin
        print('\nHere is your change: ')
        print('Toonies x ' + str(t))
        print('Loonies x ' + str(l))
        print('Quarters x ' + str(q))
        print('Dimes x ' + str(d))
        print('Nickels x ' + str(n))


def operation():
    # puts all functions together for the vending machine
    display()

    prices()

    #coins(1000, 100, 8)
    change()


def display():
    # pizza program to avoid gettin ripped off,
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
    # calculates how much small pizzas one must buy to have the same amount of a bigger pizza
    print('\nYou are now in Quantity Quantification sir. ')
    big = input('What is the diameter of the big pizzas? ')
    small = input('What is the diameter of smaller pizzas? ')

    while True:
        try:
            big = int(big)
            small = int(small)

            break
        except ValueError:
            # prevents errors
            print('Give Positive Numbers only please\n')
            big = input('What is the diameter of the big pizza? ')
            small = input('What is the diameter of smaller pizza? ')
            continue

    Abig = ((big/2)**2) * pi
    Asmall = ((small/2)**2) * pi

    num_smalls = 0
    total_area = 0
    # determines how much
    if Abig == Asmall:
        print('They are the same size...')

    elif Abig < Asmall:
        print('\nYou lied about which was the bigger one...\n')
        Asmall, Abig = Abig, Asmall

    else:
        while (total_area) <= Abig:

            num_smalls += 1
            total_area += Asmall
    # presents how much of small pizzas
        print('You will need at least ' + str(num_smalls) +
              ' of the smaller pizzas to get an equal amount.')


def money_mode():
    # program to see how much one should pay for a small pizza to avoid getting ripped off
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
                # prevent errors
                print('\nGive Positive Numbers only please\n')
                Dbig = input('What is the diameter of the big pizza? ')
                Pbig = input('What is the price of the big one? ')
                Dsmall = input('What is the diameter of the small one? ')
                NumSmall = input('How many small pizzas do you have? ')
                continue

        Abig = (Dbig/2)**2 * pi
        price_unit = Abig/Pbig
        total_area_small = (Dsmall/2)**2 * pi * NumSmall
        fair_price = (total_area_small/price_unit)

        print(format(fair_price, '.2f'))


def pizza_operation():
    # puts the whole program together

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

# display()


pizza_operation()

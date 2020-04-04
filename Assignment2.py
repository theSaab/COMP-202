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
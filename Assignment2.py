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
"""

mult = [[1,2], [2,4], [3, 6]]

for a in mult:
    
    print(a)
    sum = 0

    for b in a:
        sum += b
        
print(sum)

"""

def in_alpha(word):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if ' ' in word == True:
        print('False')
    
    else:
        
        x = 0
        while x <= len(word):

            for char in word:
                b = char in alphabet 
                
                if b == False:
                    print(b)
                    break
                else:
                    x += 1
                    continue
            break 
       
    return b

def shift():
    
    letter = input('give letter: ')
    key = int(input('Give shift number: '))
    letter = str.lower(letter)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a = 0
    if key > 26:
        while key > 26:
            key -= 26
    if len(letter) > 1:
        print('Letter cannot be more than one character')
    
    elif letter in alphabet == False:
        print(letter)
    else:    
        for char in alphabet:
            if char == letter:
                break
            else:
                a += 1
        shifted = alphabet[a + key]

        print(shifted)

def get_keys():

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    lst = []
    word = input('Give your word: ')
    word = str.lower(word)

    if len(word) == 0 :
        print(lst)        
      
    elif in_alpha(word) == False:
        print('bad')
    
    else:
        for char in word:
            lst.append(alphabet.find(char))

            print(lst)




def ceasar():

    message = input('What is your message: ')
    key = int(input('What is the key: '))
    mode = input('What mode, 1 for encryption or -1 for decryption? ')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    if mode == 1:
        for char in message:
        
            print(alphabet[alphabet.find(char) + key], end=' ')
    elif mode == -1:

        for char in message:
            print(alphabet[alphabet.find(char) - key], end=' ')
    else:
        print('Chose one mode.')


def vignere():

    message = input('What is the message? ')
    message = str.lower(message)
    key = input('What is the key? ')
    key = str.lower(key)
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    mode = int(input('What mode you want '))
    if mode == 1:
        if len(key) < len(message):
            a = 0
            num = len(message) 
            while num >= len(key):
                a += 1
                num -= len(key)

            new = str(key) * a + str(key[0:num])
            
        # print(code)
        

            x = 0
            for char in new:
                a = alphabet.find(char)
                #print(a)
                
                while x <= len(message):
                    
                    if message[x] == ' ':
                        
                        continue
                    else:
                        b = message[x]
                    
                        w = alphabet.find(b)
                        z = alphabet[w + a]
                    
                        print(z, end=' ')
                        x += 1
                        break
        
        else:
            x = 0
            for char in key:
                a = alphabet.find(char)
                #print(a)
                
                while x <= len(message):
                    
                    if message[x] == ' ':
                        
                        continue
                    else:
                        b = message[x]
                    
                        w = alphabet.find(b)
                        z = alphabet[w + a]
                    
                        print(z, end=' ')
                        x += 1
                        break
    if mode == -1:
        if len(key) < len(message):
            a = 0
            num = len(message) 
            while num >= len(key):
                a += 1
                num -= len(key)

            new = str(key) * a + str(key[0:num])
            
        # print(code)
        

            x = 0
            for char in new:
                a = alphabet.find(char)
                #print(a)
                
                while x <= len(message):
                    
                    if message[x] == ' ':
                        
                        continue
                    else:
                        b = message[x]
                    
                        w = alphabet.find(b)
                        z = alphabet[w - a]
                    
                        print(z, end=' ')
                        x += 1
                        break
        
        else:
            x = 0
            for char in key:
                a = alphabet.find(char)
                #print(a)
                
                while x <= len(message):
                    
                    if message[x] == ' ':
                        
                        continue
                    else:
                        b = message[x]
                    
                        w = alphabet.find(b)
                        z = alphabet[w - a]
                    
                        print(z, end=' ')
                        x += 1
                        break
        



vignere()


"""
def pad(message, key):
    
    a = 0
    if len(key) < len(message):
        while len(key) >= len(word):
            num -= len(word)
            a += 1
            
        print(str(word) * 3 + str(word[0:num]))
    else:
        print(word[0:num])
"""
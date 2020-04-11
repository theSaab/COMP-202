
from random import *

def dice_roll():
    #gives a random integer between chosen values, to mimic a dice throw
    x = randint(1,6)
    y = randint(1,6)
    z = x + y
    return z


def second_stage():    
    #determine pass line number too bet on
    b = pass_line()

    while True:
        #mimic continued dice roll
        a = dice_roll()

        if a == 7:
            #applying the rules of the game in the program
            print(a)
            print('You lose')
            #lose = stop
            break
        elif a == b:
            #when you win it stops
            print(a)
            break
        else:
            #print results
            print(a, end=' ')


def can_play():
    #determine if person has funding to play the game with their bet
    x = (input('How much money do you have? '))
    y = (input('Please place your bet here: '))
    
    
    while True:
        #safeguard for errors
            try:
                x = float(x)
                y = float(y)
                break            
            
            except ValueError:
                #preventing errors
                print('\nPlease enter valid numbers\n')
                x = (input('How much money do you have? '))
                y = (input('Please place your bet here: '))
                continue
    
    if y > x:
        #if you have no money, it wont let you play
        print('You have insufficient funds, find coins somewhere...')
        return False    
    else:
        #allows you to play
        print('\nYou can play\n')
        return True
    
    return x
    return y
    

def pass_line():
    #modified pass line bet number roll, more messages
    result = dice_roll()

    #depending on the result of the dice, you win or lose, messages present
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
    #putting the whole casino program together, to simulate a game of craps
    a = can_play()
    if a == False:
        print('done')
    
    if a == True:
        #if it allows you to play the program continues
        
        a = pass_line()
        
        if a == True:
            print('done')
        elif a == False:
            print('bruh')
        else:   
            second_stage()



def in_alpha(word):
    #determine if a letter is in the alphabet, will deny any non alphabetical letters.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if ' ' in word == True:
        #if there is a space in your word, it is not in the alphabet
        print('False')
    
    else:
        #determine if legitimate letter
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
    #shift the letters of a word by an certain amount to another letter in the alphabet
    letter = input('give letter: ')
    key = int(input('Give shift number: '))
    letter = str.lower(letter)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a = 0
    if key > 26:
        #prevent erros from missing numbers
        while key > 26:
            key -= 26
    if len(letter) > 1:
        #prevent errors
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
        #print shifted word

        print(shifted)

def get_keys():
    #print the number assigned to as letter through a list
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    lst = []
    word = input('Give your word: ')
    word = str.lower(word)

    if len(word) == 0 :
    #if the word is empty nothing happens
       print(lst)        
      
    elif in_alpha(word) == False:
        #if the word isnt made up of alphabetical letter, it stops
        print('bad')
    
    else:
        for char in word:
            #add characters in list
            lst.append(alphabet.find(char))

            print(lst)




def ceasar():
    #program designed to mimic a ceasar cypher
    message = input('What is your message: ')
    key = int(input('What is the key: '))
    mode = input('What mode, 1 for encryption or -1 for decryption? ')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    if mode == 1:
        #encryption
        for char in message:
        
            print(alphabet[alphabet.find(char) + key], end=' ')
    elif mode == -1:
        #decryption

        for char in message:
            print(alphabet[alphabet.find(char) - key], end=' ')
    else:
        #prevent errors
        print('Chose one mode.')


def vignere():
    #mimic the vignere cypher

    message = input('What is the message? ')
    message = str.lower(message)
    key = input('What is the key? ')
    key = str.lower(key)
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    mode = int(input('What mode you want '))
    if mode == 1:
        #ecnryption
        if len(key) < len(message):
            #create code word for assigned message
            a = 0
            num = len(message) 
            while num >= len(key):
                a += 1
                num -= len(key)
            #print new code word for next part of program
            new = str(key) * a + str(key[0:num])
            

            x = 0
            for char in new:
                #print encrypted word
                a = alphabet.find(char)
             
                
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
            #same program as before without adjustements to key
            x = 0
            for char in key:
                a = alphabet.find(char)
                
                
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
        #decryption
        if len(key) < len(message):
            a = 0
            num = len(message) 
            while num >= len(key):
                a += 1
                num -= len(key)

            new = str(key) * a + str(key[0:num])
            
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
        


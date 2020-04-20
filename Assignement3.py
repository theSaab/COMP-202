

import random

# this displays a scrabble board


def display(x, y):
    # this prints the numbers on top
    for i in range(x+1):
        if i == x:
            print('  ' + str(i))
        else:
            print('  ' + str(i), end='   ')
    # pieces for making board
    left = '+-'
    right = '--+'
    middle = '-----'
    line = ''
    seperators = '     |'
    seperation = '|    |'

    # this prints the shape a pieces of board
    for i in range(x+1):
        line += middle
    for i in range(x):
        seperation += seperators

    # prints the bottom part
    for i in range(y):
        print(left + line + right)
        print(seperation)
    print(left + line + right)

# this is used to make a board out of lsits given


def create_board(x, y):

    lst = []
    inside_lst = []

    for i in range(y):
        inside_lst.append(' ')

    for i in range(x):
        lst.append(inside_lst)

    return lst

# this gives all letters of a column from a range of lists


def vertical(column):

    # given list of lists
    b = [['c', 'a', 't', 's', ], [' ', 'a', 'r', 't'], ['', '', 'a', ' ']]
    lst = []
    # based off column number, adds letters of the column to blank list
    for i in range(len(b)):
        lst.append(b[i][column])
    print(lst)

# this finds a word in list


def find(x):

    # given list
    b = [' ', 'squi', '', 'rre', 'l']
    word = ''
    num = 1
    # breaks if there is a seperation
    while num < len(b):
        if b[x-num] == '' or b[x-num] == ' ':
            break

        # creates word from list pieces
        else:
            word = b[x-num] + word
            num += 1

    # also creates word
    for i in range(x, len(b)):
        word = word + b[i]
    print(word)

# finds the amount of available spaces in a list


def space():
    # given list
    b = [' ', ' ', ' ', ' ', ' ']
    count = 0

    # counting available spaces
    for i in range(len(b)):
        if b[i] == ' ':
            count += 1
        else:
            continue
    print(count)

# determines if a word can fit inside a list


def fit(word, position):
    # given values
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    b = ['a', ' ', ' ', 'b', ' ', ' ', 'c', ' ', ' ']
    len_word = len(word)
    num = 1
    count = 0

    # if postition chosen is taken, it print false
    if b[position] in alpha == True:
        print(b[position] not in alpha)

    # begins to calculate if there is enoguh space
    else:
        # iterates through the list
        for i in range(0, len(b)):
            # if empty space the count goes up
            if b[i] == ' ':
                count += 1
            # if not empty it continues
            else:
                continue

        # if the count is the same or bigger, there enough empty spaces for the word
        if count >= len_word:
            print('True')

        # if count is smaller, there is not enough space for the word
        else:
            print('False')

# this counts the number of a letter in a word,
# returns a dictionary with letters as keys and numbers as values


def count():
    # given values
    dic = {}
    word = 'banana'
    count = 1

    # iterates through word characters
    for char in word:
        # if it already exists, it adds 1 to counter
        if (char in dic) == True:
            dic[char] += 1

        # if not in dic, it adds new key and value 1
        else:
            dic[char] = count

    print(dic)

# inserts each key for the amount of its value


def flatten():
    # given items
    dic = {'a': 0, 'f': 1, 'k': 5}
    lst = []

    for key in dic:
        num = int(dic[key])
        # inserts the key
        for i in range(num):
            lst.append(key)
    # if dic = {'a' : 2, 'f' : 1}
    # this will return ['a', 'a', 'f']
    print(lst)

# given the letters of a word,
# it returns an amount of points according to the characters within


def score():
    dic = {'a': 5, 't': 3, 'n': -2}
    word = 'cat'
    points = 0

    # if char is in point dic it gives points, if not it skips the letter
    for char in word:
        if (char in dic) == False:
            continue

        # adds the points of the letter to the sum of points
        else:
            points += dic[char]

    print(points)


a = {'a': 2, 'c': 1}
b = {'a': 2, 'b': 1, 'c': 2}
c = {'a': 5, 'b': 3}

# determines if a dic is a subset of other dic,
# subset is if all keys of d1 are in d2


def subset(d1, d2):
    count = 0

    # determining presence of a key
    for key in d1:
        if (key in d2) == True:
            # count for later
            count += 1
            continue

        # if a single key isnt present, it returns false
        else:
            return (key in d2)
            break

    # count determines if d1 has been all iterated,
    # returns true, meaning it is a subset of d2
    if count == len(d1):
        return True
    return(key in d2)

# removes values of a key in d1 based off value in d2


def substract(d1, d2):

    # only proceeds if d2 is a subset of d1
    if subset(d2, d1) == True:

        # removing value from keys
        for key in d2:
            d1[key] = d1[key] - d2[key]

            # if value is 0, it removes key entirely
            if d1[key] == 0:
                del d1[key]
        print(d1)
    # this returns false if not subsets
    else:
        print(subset(d2, d1))

# this creates a dictionary with len of word and starting letter from a given list w


def create_scrabble_dict(w):
    result = {}
   # w = ['aa', 'qi', 'za', 'cat', 'can',
    #     'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']

    # add keys and values
    for x in w:
        if len(x) in result.keys():
            if x[0] in result[len(x)]:
                result[len(x)][x[0]].append(x)
            else:
                result[len(x)][x[0]] = [x]
        else:
            result[len(x)] = {x[0]: [x]}
    print(result)

# determines if a word is valid,
# if it is the list, valid


def valid():
    word = 'zebra'
    w = ['aa', 'qi', 'za', 'cat', 'can', 'cow',
         'dog', 'dad', 'hippo', 'umami', 'uncle']
    # this creates a dictionary from the list, idk why
    d = create_scrabble_dict(w)

    # determines its presence in the dictionary
    if (word in w) == True:
        print(True)
    else:
        print(False)

# this prints out your rack of letters according to a dic


def rack():
    dic = {'g': 2, 'k': 0, 'p': 4}

    # iterates through dictionary
    for key in dic:
        num = dic[key]
        key = str.upper(key)

        # prints key for value amount of times
        for i in range(num):
            print(key, end=' ')

# determines if the letters of a word are  present in a dictionary


def has_letters(dic, word):
    point = 0
    lst = []

    # iterates through word
    for char in word:
        # count used to determine if the whole word has been processed
        count = word.count(char)

        # if not present, break from loop
        if (char in dic) == False:
            print(False)
            break

        # otherwise continue
        else:
            if count > dic[char]:
                print(False)
                break
            else:
                point += 1
                continue

    # see if the all the letters have been tested
    # prints a new dictionary
    if point == len(word):
        for char in word:
            count = word.count(char)
            if (char in lst) == True:
                continue
            else:
                if (char in dic) == False:
                    continue
                else:
                    # creates list to print???
                    dic[char] = dic[char] - count
                    lst.append(char)

    if point == len(word):
        for key in list(dic):
            if dic[key] == 0:
                dic.pop(key)

    if point == len(word):
        print(True)

    print(dic)

# this gives you a random set of letters from a stash,
# it gives letters until the limit is reached or the stash runs out of letters


def refill(rack, dic, limit):
    lst = list(dic)
    sum = 0

    # iterates as long as limit is respected
    while (sum <= limit):

        # iterates through rack, adds up the amount of total letters
        for key in rack:
            sum += rack[key]

        # randomly selects letters from stash
        a = random.choice(lst)

        # if letter already present in rack, adds 1 to value
        if (a in rack) == True:
            rack[a] = rack[a] + dic[a]
            dic[a] = dic[a]-dic[a]

        # otherwise creates a new key and value
        else:
            rack[a] = dic[a]
            dic[a] = dic[a] - dic[a]
    print(rack)

# this displays a scrabble board based off 2 integers given,
# prints length and width


def display(b):
    # aspects of board
    left = '+-'
    right = '-+'
    middle = '------'
    line = ''
    seperators = '  |'
    seperation = '| '
    len_outside = len(b)
    len_inside = len(b[1])
    out = 0
    inside = 0

    # prints top part, numbering of columns
    for i in range(len_inside):
        if i == len_inside-1:
            print('  ' + str(i))
        else:
            print('  ' + str(i), end='   ')

    # creates line between rows
    for i in range(len_inside-1):
        line += middle
    num = 0

    # add characters to board
    while num < len_outside:

        # adds characters from given list a
        for i in range(len_inside):
            seperation += (b[out][i] + seperators + '')
        print(left + line + right)
        print(seperation)
        seperation = ' | '
        out += 1
        if out == len_outside:
            break

    print(left + line + right)


a = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' '], ['h', ' ', ' ', 'j']]


# prints another scrabble board
# user determines direction of word and what the word will be
# also determines positioning
def place_tiles(lst, word, row, col, dir):
    count = 0
    # if word does not fit in board
    if (len(word) > (len(lst) - row)) or (len(word) > (len(lst[0]) - col)):
        print('too long')

    # based off direction of word
    elif dir == 'right':

        for char in word:
            lst[row][col + count] = char
            count += 1

    # word placed downwards
    elif dir == 'down':

        for char in word:
            lst[row + count][col] = char
            count += 1

    return lst


z = place_tiles(a, 'in', 1, 2, 'down')

display(z)

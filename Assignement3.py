

"""

def display(x, y):

    for i in range(x+1):
        if i == x:
            print('  ' + str(i))
        else:
            print('  ' + str(i), end='   ')

    left =  '+-'
    right = '--+'
    middle = '-----'
    line = ''
    seperators = '     |'
    seperation = '|    |'

    for i in range(x+1):
        line += middle
    for i in range(x):
        seperation += seperators

    for i in range(y):
        print(left + line + right)
        print(seperation)
    print(left + line + right)


display(4,2)
"""


import random


def create_board(x, y):

    lst = []
    inside_lst = []

    for i in range(y):
        inside_lst.append(' ')

    for i in range(x):
        lst.append(inside_lst)

    return lst


def display():

    b = [[' ', ' ', ' ', ' ', ' '], [' ', 'c', 'a', 't', 's']]

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

    for i in range(len_inside):
        if i == len_inside-1:
            print('  ' + str(i))
        else:
            print('  ' + str(i), end='   ')

    for i in range(len_inside-1):
        line += middle
    num = 0

    while num < len_outside:

        for i in range(len_inside):
            seperation += (b[out][i] + seperators + '')
        print(left + line + right)
        print(seperation)
        seperation = ' | '
        out += 1
        if out == len_outside:
            break

    print(left+line+right)


def vertical(column):

    b = [['c', 'a', 't', 's', ], [' ', 'a', 'r', 't'], ['', '', 'a', ' ']]
    lst = []
    for i in range(len(b)):
        lst.append(b[i][column])
    print(lst)


def find(x):

    b = [' ', 'squi', '', 'rre', 'l']
    word = ''
    num = 1
    while num < len(b):
        if b[x-num] == '' or b[x-num] == ' ':
            break
        else:
            word = b[x-num] + word
            num += 1
    for i in range(x, len(b)):

        word = word + b[i]
    print(word)


def space():

    b = [' ', ' ', ' ', ' ', ' ']
    count = 0
    for i in range(len(b)):
        if b[i] == ' ':
            count += 1
        else:
            continue
    print(count)


def fit(word, position):

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    b = ['a', ' ', ' ', 'b', ' ', ' ', 'c', ' ', ' ']
    len_word = len(word)
    num = 1
    count = 0

    if b[position] in alpha == True:
        print(b[position] not in alpha)

    else:

        for i in range(0, len(b)):
            if b[i] == ' ':
                count += 1

            else:
                continue
        if count >= len_word:
            print('True')
        else:
            print('False')


def count():
    dic = {}
    word = 'banana'
    count = 1

    for char in word:

        if (char in dic) == True:
            dic[char] += 1

        else:
            dic[char] = count

    print(dic)


def flatten():

    dic = {'a': 0, 'f': 1, 'k': 5}
    lst = []

    for key in dic:
        num = int(dic[key])
        for i in range(num):
            lst.append(key)
    print(lst)


def score():
    dic = {'a': 5, 't': 3, 'n': -2}
    word = 'cat'
    points = 0

    for char in word:
        if (char in dic) == False:
            continue
        else:
            points += dic[char]

    print(points)


a = {'a': 2, 'c': 1}
b = {'a': 2, 'b': 1, 'c': 2}
c = {'a': 5, 'b': 3}


def subset(d1, d2):
    count = 0
    for key in d1:
        if (key in d2) == True:
            count += 1
            continue
        else:
            return (key in d2)
            break
    if count == len(d1):
        return True
    return(key in d2)


def substract(d1, d2):

    if subset(d2, d1) == True:
        for key in d2:
            d1[key] = d1[key] - d2[key]

            if d1[key] == 0:
                del d1[key]
        print(d1)
    else:
        print(subset(d2, d1))


def create_scrabble_dict(w):
    result = {}
   # w = ['aa', 'qi', 'za', 'cat', 'can',
    #     'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']

    for x in w:
        if len(x) in result.keys():
            if x[0] in result[len(x)]:
                result[len(x)][x[0]].append(x)
            else:
                result[len(x)][x[0]] = [x]
        else:
            result[len(x)] = {x[0]: [x]}
    print(result)


def valid():
    word = 'zebra'
    w = ['aa', 'qi', 'za', 'cat', 'can', 'cow',
         'dog', 'dad', 'hippo', 'umami', 'uncle']
    d = create_scrabble_dict(w)
    if (word in w) == True:
        print(True)
    else:
        print(False)


def rack():
    dic = {'g': 2, 'k': 0, 'p': 4}
    for key in dic:
        num = dic[key]
        key = str.upper(key)

        for i in range(num):
            print(key, end=' ')


def has_letters(dic, word):
    point = 0
    lst = []
    for char in word:
        count = word.count(char)

        if (char in dic) == False:
            print(False)
            break
        else:
            if count > dic[char]:
                print(False)
                break
            else:
                point += 1
                continue

    if point == len(word):
        for char in word:
            count = word.count(char)
            if (char in lst) == True:
                continue
            else:
                if (char in dic) == False:
                    continue
                else:
                    dic[char] = dic[char] - count
                    lst.append(char)

    if point == len(word):
        for key in list(dic):
            if dic[key] == 0:
                dic.pop(key)

    if point == len(word):
        print(True)

    print(dic)


def refill(rack, dic, limit):
    lst = list(dic)
    sum = 0

    while (sum <= limit):
        for key in rack:
            sum += rack[key]
        a = random.choice(lst)
        if (a in rack) == True:
            rack[a] = rack[a] + dic[a]
            dic[a] = dic[a]-dic[a]
        else:
            rack[a] = dic[a]
            dic[a] = dic[a] - dic[a]
    print(rack)


refill({'a': 2, 'k': 1}, {'a': 1, 'r': 5}, 7)

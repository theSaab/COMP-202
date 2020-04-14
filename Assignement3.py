

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


def create_board(x, y):
    
    lst = []
    inside_lst = []
    
    for i in range(y):
        inside_lst.append(' ')

    for i in range(x):
        lst.append(inside_lst)
    
    return lst


def display():

    b = create_board(3,4)

    
    left =  '+-'
    right = '---+'
    middle = '------'
    line = ''
    seperators = '     |'
    seperation = '|    |'
    len_b = len(b)
    len_inside = len(b[1])
    
    
    for i in range(len_inside+1):
        if i == len_inside:
            print('  ' + str(i))
        else:
            print('  ' + str(i), end='   ')

    for i in range(len_inside):
        line += middle
    for i in range(len_inside):
        seperation += seperators
    
    for i in range(len_b):
        print(left + line + right)
        print(seperation)
    print(left + line + right)

display()


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

    b = [[' ', ' ', ' ', ' ', ' '], [' ', 'c', 'a', 't', 's']]

    
    left =  '+-'
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
    #for i in range(len_outside):
    #    print(left + line + right)
    #print(left + line + right)

display()
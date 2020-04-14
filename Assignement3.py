def create_board():

    x = int(input('Give length: '))
    y = int(input('Give height: '))
    lst = []
    for i in range(x):
        lst.append(' ')
    for i in range(y):
        print(lst)
  



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
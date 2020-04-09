
x = int(input('Give first: '))
y = int(input('Give second: '))


for i in range(1, x+1):
    j = 0
    while (j < i):
        print(i * j, end= ' ')
        j += 1
    print()


def primes(N):
    
    lis = []
    i, j, flag = 0, 0, 0;

    for i in range(1, N + 1, 1):

        if (i == 1 or i == 0) :
            continue
        
        flag = 1

        for j in range(2, ((i // 2 ) + 1)):
            if (i % j == 0):
                flag = 0
                break

        if (flag == 1):
            lis.append(i)

    print(lis)


N = 100
primes(N)

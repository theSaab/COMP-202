
from collections import deque

graph = {
    1: [2, 3, None],
    2: [4, None],
    3: [None],
    4: [5, 6, None],
    5: [6, None],
    6: [None]
}

llist = deque("abcde")


list = deque('abc')

list.popleft()

print(list)
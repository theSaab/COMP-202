

def mario(height):
    count = height
    num = 0
    level = (' ' * (count-1)) + '#'

    for i in range(height):
        print(level)
        count -= 1
        num += 1
        level = (' ' * count) + '#' * num

    #  return level


mario(8)

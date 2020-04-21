

"""
boo = {43 : 32, eg : 4}
heights = {7 : 192, 'fes' :90, 'fesfesf' : 3}
print(boo)
"""
"""
def count(input_list):
    count = {}

    for element in input_list:
        if element in count:
            
            count[element] += 1
        else:

            count[element] = 1

    print(count)
    return count
count({7 : 192, 'fes' : 90, 'fesfesf' : 3, 'asd' : 3})
"""
"""
dic = {'F2017' : 816, 'W2018' : 613, 'F2018' : 709, 'W2019' : 590, 'F2019' : 744}
sum = 0
years = 0

for key in dic:
    sum += dic[key]
    years += 1
avg = sum/years
print(avg)
"""
"""
dic = {}
alpha = 'abcdefghijklmnopqrstuvwxyz'
lst = ['baotato', 'apple', 'johnny', 'bruh', 'alpha', 'jlui']

for i in lst:
    if (i[0] in dic) == True:
        dic[i[0]] = dic[i[0]] + 1
        
    else:
        dic[i[0]] = 1
print(dic)
"""
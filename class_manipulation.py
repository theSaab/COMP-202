

class Student:
    name = ''

s1 = Student()
s2 = Student()
s1.name = "john"
s2.name = "prin"
s1.ID = 1842454
s2.ID = 1965325

def bigger_ID(student1, student2):
    
    ID1 = s1.ID
    ID2 = s2.ID
    
    if ID1 > ID2:
        print(ID1)
    else:
        print(ID2)
        
bigger_ID(s2, s1)
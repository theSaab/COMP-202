

def bigger_ID(student1, student2):

    ID1 = s1.ID
    ID2 = s2.ID

    if ID1 > ID2:
        print(ID1)
    else:
        print(ID2)


class Student:
    passing_grade = 60
    number_of_students = 0

    def __init__(self, name='Harry', age='23', id_num='12345'):
        self.name = name
        self.age = age
        self.id_num = id_num

    def showAge(self):
        print(self.age)

    def showName(self):
        print(self.name)

    def display_info(self):

        self.showAge()
        self.showName()
        print(self.id_num)

    def update_name(self, name):

        self.name = name


def student_return(name, age, number):
    return (Student(name, age, number))


s1 = student_return('john', 24, 23233)
s2 = student_return('Joe', 14, 24333)
s1.display_info()
s1.update_name('johnny')
s1.display_info()

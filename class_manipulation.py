

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

    def __init__(self, name='Harry', age='23', id_num='12345', courses=[]):
        self.name = name
        self.age = age
        self.id_num = id_num
        self.courses = courses
        

    def showAge(self):
        print(self.age)

    def showName(self):
        print(self.name)

    def display_info(self):

        self.showAge()
        self.showName()
        print(self.id_num)
        print(self.courses)

    def update_name(self, name):

        self.name = name

    def add_course(self, course):
        
        self.courses.append(course)

def student_return(name, age, number, courses):
    return (Student(name, age, number, courses))



s1 = student_return('john', 24, 23233, ['math', 'history', 'chem'])
s2 = student_return('Joe', 14, 24333, [])


class Movie:

    def __init__(self, name='Harry', length='23 minutes', director='him', actors=[]):
        self.name = name
        self.length = length
        self.director = director
        self.actors = actors
        
    def display_info(self):

        print(self.name)
        print(self.length)
        print(self.director)
        print(self.actors)
        
    def has_actor(self, actor):
        
        if actor in self.actors:
            print('Yes')
        else:
            print('no')
    
def movie_return(name, length, director, actors):
    return (Movie(name, length, director, actors))

m1 = movie_return('red', '24 minutes', 'john smoth', ['x', 'y', 'z'])


class Cats:

    def __init__(self, name= '', age = 0.0):
        self.name = name
        self.age = age
        
    def meow(cat):
        
        if cat.age < 1:
            print(cat.name + ' mews')
        else:
            print(cat.name + ' meow')        
            
    def birthday(cat):
        
        cat.age += 1
        print(cat.age)
        
       
c1 = Cats('john')
c2 = Cats('lilo', 7)

c2.birthday()
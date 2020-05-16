

def bigger_ID(student1, student2):

    ID1 = s1.ID
    ID2 = s2.ID

    if ID1 > ID2:
        print(ID1)
    else:
        print(ID2)


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

    def __init__(self, name='', age=0.0):
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


class Student:

    def __init__(self, name='', age='', id_num='', courses=[]):
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

    def __str__(self):

        name = str(self.name)
        id_num = str(self.id_num)
        courses = str(self.courses)

        print('Name: ' + name)
        print('ID: ' + id_num)
        print('Courses: ' + courses)


s1 = Student('john', 24, 23233, ['math', 'history', 'chem'])
s2 = Student('Joe', 14, 24333, [])


class Book:

    def __init__(self, title='',  author='', id_num=0, price=0.0, genre='N/A'):
        self.title = title
        self.author = author
        self.id_num = id_num
        self.price = price
        self.genre = genre

    def __str__(self):

        title = str(self.title)
        id_num = str(self.id_num)
        author = str(self.author)
        price = str(self.price)
        print(title, author, id_num, price, sep=', ')

    def on_sale(self):

        self.price = self.price/2
        print(self.price)

    def is_cheaper(self, book2):

        price1 = self.price
        price2 = book2.price

        if price1 > price2:
            print(False)

        else:
            print(True)

    def print_books(list):

        for element in list:

            element.__str__()

    def sale(list):

        for element in list:

            Book.on_sale(element)

    def books_by_genre(list, genre):

        titles = []
        for element in list:

            if element.genre == genre:
                titles.append(element)

            else:
                continue
        else:
            return(titles)

    def get_all_genres(list):

        genres = []
        for element in list:
            genre = element.genre

            if genre not in genres:
                genres.append(genre)

            else:
                continue
        else:
            print(genres)

    def find_cheapest(list, genre):

        titles = Book.books_by_genre(list, genre)

        price = []
        for element in titles:
            price.append(element.price)

        print(min(float(i) for i in price))


b1 = Book('bruh', 'mike lao', 1234, 3.7, 'horror')
b2 = Book('OOF', 'john kin', 5987, 4.9, 'adventure')
b3 = Book('F', 'in', 532, 59, 'love')
b4 = Book('OyOF', 'jo', 587, 4.0, 'horror')
b5 = Book('OvF', 'j kin', 6587, 5.9, 'horror')
b6 = Book('bruh', 'mike lao', 1234, 13.7, 'horror')
b7 = Book('bruh', 'mike lao', 1234, 23.7, 'horror')
b8 = Book('bruh', 'mike lao', 1234, 33.7, 'horror')
b9 = Book('bruh', 'mike lao', 1234, 53.7, 'horror')

book_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

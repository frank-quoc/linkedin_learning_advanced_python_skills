# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book: 
    def __init__(self, title): # not constructor, initializer function. Object is already created when func called
        self.title = title

# TODO: create instances of the class
b1 = Book("Harry Potter")
b2 = Book("My Antonia")

# TODO: print the class and property
print(b1)
print(b1.title)
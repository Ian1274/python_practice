"""class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printclass(self):
        try:
            print("{}'s salary is {}, and his age is {}".format(self.name, self.salary, self.age))
        except:
            print("Error! No age")

name = input()
salary = int(input())
em1 = Employee(name, salary)
print(em1.printclass())
age = int(input())
em1.age = age
print(em1.printclass())"""


"""class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printclass(self):
        try:
            print("{}'s salary is {}, and his age is {}".format(self.name, self.salary, self.age))
        except:
            print("Error! No age")

name = input()
salary = int(input())
age = int(input())
e = Employee(name, salary)
a = hasattr(e, 'age')
print(a)
if a ==True:
    print(e.printclass())
else:
    e.__setattr__('age', age)
    print(e.printclass())"""


"""class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return  f"{(self.x, self.y)}"
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

x1, y1 = map(int, input().split())
print(type(x1))
x2, y2 = map(int, input().split())
c1 = Coordinate(x1, y1)
c2 = Coordinate(x2, y2)
print(c1.__str__())
print(c2.__str__())
print(c1.__add__(c2))
print(c1)"""
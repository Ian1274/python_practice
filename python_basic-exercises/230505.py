"""print(eval("3*7"))
str_1 = input()
print(eval(str_1))"""


"""x = input().split()
print(sorted(x, key=lambda x:len(x), reverse=True))
print(type(x))"""


"""def cal(x, y):
    return x - y
print(cal(3, 5))
print(cal(5, 3))"""


"""def tuzi(n):
    if n == 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return (n - 1) + (n - 2) + 2
print(tuzi(6))"""


"""import math
def s_ball(r):
    s = 4*math.pi*(r**4)
    return round(s, 2)
print(s_ball(2))"""


"""class Student:
    def __init__(self, name, number, score, grade):
        self.name = name
        self.number = number
        self.score = score
        self.grade = grade
    def __str__(self):
        return f"{self.name}'s student number is {self.number}, " \
               f"and his grade is {self.score}. " \
               f"He submitted {len(self.grade)} assignments, " \
               f"each with a grade of {' '.join(self.grade)}"

name = "NiuNiu"
number  = "12345"
score = 90
grade = "A B C".split()
# print(grade, type(grade))
stu1 = Student(name, number, score, grade)
print(stu1)"""



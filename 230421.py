"""name = " Niuniu "
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
print(name.replace(" ", "_"))
print(name*100)
word = input('Entera word')
print(word[0:10])"""

"""offer_list = ['allen', 'tom']
for i in offer_list:
    print(f"{i}, you have passed our interview and will soon become a member of our company.")

offer_list[1]='andy'
for i in offer_list:
    print(f"{i}, welcome to join us!")"""

"""a = "yyx yyx1 yyx2 yyx3 yyx4 yyx5 yyx6"
lst = list(a.split())  # split() function: separate whitespaces characters
print(lst)"""

"""lst = [1, '2']
print(lst[0],type(lst[0]), lst[1], type(lst[1]))
lst[1] = int(lst[1])
print(lst[0],type(lst[0]), lst[1], type(lst[1]))

num = input('Enter a string of numbers: ')
lst = list(num)
for i in range(len(lst)):
    lst[i] = int(lst[i])
print(lst)"""

"""a = "yyx yyx1 yyx2 yyx3"
lst = list(a.split())
print(len(lst))
lst.append('Allen')
print(lst)
lst.insert(0, 'lucy')
print(lst)
lst.pop(0)
print(lst)
print(lst[:-3])"""

"""my_lst = ['P', 'y', 't', 'h', 'o', 'n']
a = sorted(my_lst)
print(a)
print(my_lst)
my_lst.sort(reverse=True)
print(my_lst)

num = [3, 5, 9, 0, 1, 9, 0, 3]
num.reverse()
print(num)"""


"""lst = [['Niumei', 'YOLO', 'Niu Ke Le', 'Mona'],
       ['pizza', 'fish', 'potato', 'beef'],
       [3, 6, 0, 3]]"""



"""number = [(int(c)+3) % 9 for c in input()]
print(f"{number[2]}{number[3]}{number[0]}{number[1]}")"""


"""stack = [1, 2, 3, 4, 5]
for i in range(2):
    stack.pop(-1)
    print(stack)
stack.append(9)
print(stack)"""

"""queue = [1, 2, 3, 4, 5]
for i in range(2):
    queue.pop(0)
    print(queue)
queue.append(9)
print(queue)"""


"""group_list = ['Tom', 'Allen', 'Jane', 'William', 'Tony' ]
print(group_list[0:2])
print(group_list[1:4])
print(group_list[-2:])"""

"""def add_subtract(a, b):
    return a + b, a - b

x = int(input())
y = int(input())
print(x*y)
print(x**y)"""

"""x = int(input())
y = int(input())
print(x%y, x//y)
print(f'{x/y:.2f}')"""

"""def vs(a, b):
    if a == b:
        return True
    else:
        return False
print(vs(22, 23))"""

"""a = input()
lst = [i for i in a.split()]
print(lst[0] >= lst[2])
print(lst[0] <= lst[1])"""

"""x, y = map(int, input().split())
print(type(x), type(y))
print(x and y)
print(x or y)
print(not x)
print(not y)"""

"""a = input()
b = input()
print(a == b)
print(a.lower() == b.lower())"""

"""name = input()
name1 = input()
print(name1 in name)"""

"""x, y = map(int,input().split())
print(x & y, x | y, sep="\n")"""

"""x, y, z, k = map(int, input().split())
print((x + y)*(z - k))
"""
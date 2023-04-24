"""b = int(input("enter 0 or 1:"))

if b :
    print("Enter")
else:
    print("error")"""


"""my_list = []
if my_list:
    print("my_list is not empty!")
else:
    print("my_list is empty!")"""


"""current_users = ['Niuniu', 'Niumei', 'GurR', 'LOLO']
new_users = ['GurR', 'Niu Ke Le', 'LoLo', 'Tuo Rui Chi']
for i in new_users:
    if i in current_users:
        print(f'The user name {i} has already been registered! Please change it and try again!')
    else:
        print(f'Congratulations, the user name {i} is available!')"""


"""name = input("Enter name:")
if name == 'pizaa':
    print("10yuan")
elif name == 'rice':
    print("2yuan")
else:
    print('8yuan')"""


"""score,s,cnt={'A':4,'B':3,'C':2,'D':1,'F':0},0,0
while (n:=score.get(input(),False)) is not False:
    w=int(input())
    s,cnt=s+n*w,cnt+w
print(f'{s/cnt:.2f}')"""


"""lst = [i for i in "PYthon"]
print(f'Here is the original list: \n {lst}')
print(f'The number that my_list has is:\n {len(lst)}')"""


"""users_list = ['Niuniu', 'Niumei', 'Niu Ke Le']
for i in users_list:
    print(f' Hi, {i}! Welcome to Nowcoder!')
print("Happy Programmers' Day to everyone!")"""


"""lst = [i for i in range(10, 51)]
print(lst)
print(max(lst)," ",min(lst))"""


"""age = [22, 23, 27, 28, 29, 31]
age_s = sum(age)
age_a = age_s/(len(age))
print(age_s, '\n', age_a)"""


"""lst = [i for i in range(1, 51) if i % 5 == 0]
print(lst)"""


"""my_list = []
for i in range(1, 11):
    my_list.append(2**i)
    print(my_list[-1])"""


"""list = ['apple', 'ice cream', 'watermelon', 'chips', 'hotdogs', 'hotpot']
while list != []:
    list.pop(-1)
    print(list)"""


"""users_list = ['Niuniu', 'Niumei', 'HR', 'Niu Ke Le', 'GURR', 'LOLO']
for i in users_list:
    if i == 'HR':
        print('Hi, HR! Would you like to hire someone?')
    else:
        print(f'Hi, {i}! Welcome to Nowcoder!')"""


"""lst = [3, 45, 9, 8, 12, 89, 103, 42, 54, 79]
x = int(input('Please enter a number:'))
for i in lst:
    if i - x :
        print(i)
    else:
        break"""


"""lst = [i for i in range(1, 16)]
for i in lst:
    if i != 13:
        print(i, end=' ')
    elif i == 13:
        continue"""


"""import numpy as np
matrix = np.arange(1, 10).reshape(3,3)
print(matrix)
n = int(input())
print(matrix*n)"""

"""a = "yyx"
b = "asc"
c = tuple((a, b))
print(c)
d = (a, c)
print(d)"""


"""entry_form = ('Niuniu', 'Niumei')
print(entry_form)
try:
    entry_form[1] = "Niukele"
except TypeError:
    print('The entry form cannot be modified!')"""


"""tp = ("NiuNiu", "Niumei", "Niukele", "NiuNeng", "Tom")
print(tp[0:3])"""


"""tp = ['Tom', 'Tony', 'Allen', 'Cydin', 'Lucy', 'Anna']
tp1 = tuple(tp)
print(tp1)
name = input()
if name in tp1:
    print("congratulations!")
else:
    print("what a pity")"""


"""tp = tuple(range(1, 6))
tp_a = tuple(range(6, 11))
print(tp, len(tp))
print(tp + tp_a)"""
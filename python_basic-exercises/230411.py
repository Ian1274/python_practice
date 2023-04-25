
# 编程实现：用户在键盘中输入自己的名字，例如“张三”，终端打印“你好，张三”
'''name = input('please enter your name:')
print('hello!,', f'your name is {name}.')'''

# 判断下面的代码是否写的正确，如果不正确，请修改代码，然后执行代码。
'''a = "200"
b = int(a)
print(b)'''

# 编写程序，从键盘获取用户名和密码，然后判断，如果正确就输出以下信息: "欢迎来到博学谷！"
'''ture_username = 'yyx'
ture_userpassword = '991207'
username = input('please enter your name:')
userpassword = input('please enter the password:')
if username == ture_username and userpassword == ture_userpassword:
    print('welcome to python world!')
else:
    print('username or password is wrong!')'''

# 编写代码设计简易计算器，可以进行基本的加减乘除运算。
'''nb1 = int(input('please enter a number:'))
operator = input('please enter a operator:(+ - * %)')
nb2 = int(input('please enter another number:'))
if operator == '+':
    print(f'{nb1}+{nb2}={nb1+nb2}')
elif operator == '-':
    print(f'{nb1}-{nb2}={nb1-nb2}')
elif operator == '*':
    print(f'{nb1}*{nb2}={nb1*nb2}')
elif operator == '%':
    print(f'{nb1}%{nb2}={nb1%nb2}')'''

# 考察for range的用法
'''pstr = "abcdef"
for s in pstr:
    print(s)'''

# abcd 逆打印
'''a = 'abcd'
index = len(a)-1
while index >=0 :
    print(a[index])
    index -= 1

a = a[::-1]
print(a)'''

# 把[1，2，3，4]转换为1234
'''lst = [1, 2, 3, 4]
str1 = ''
for i in lst:
    print(i, type(i))
    str1 += str(i)
    print(str1)'''

# 编程实现 把一个元素全为数字的列表中的所有偶数加1
'''import numpy as np
lengh = 10
lst = np.random.randint(0,11,lengh)
print(lst)
for i in range(lengh):
    if lst[i-1] % 2 == 0:
        lst[i-1] +=1
print(lst)
'''
# test = ("a","b","c","a","c") ，统计元祖中每个元素出现的次数把最终的结果保存到列表中，例如[('a',1),('b',3),('c',5)]

'''test = ("a","b","c","a","c")
lst = []
for i in test:
    cnt = test.count(i)
    tmp = (i, cnt)
    if tmp in lst:
        continue
    else:
        lst.append(tmp)
print(lst)'''

# 在控制台输入 3 组个人信息，每个人有姓名和年龄，将信息存入字典中，将字典存入列表。
# 遍历列表，打印每个人的信息，打印格式如下：
# 1 张三 20
# 2 李四 22
# 3 王五 23
'''user = []
i = 0
while i < 3:
    name = input('Enter name:')
    age = int(input('Enter age:'))
    user.append({'name': name, 'age': age})
    i += 1

for thnum,user in enumerate(user, start=1):
    print(f"{thnum} {user['name']} {user['age']}")
'''

# 已知字符串 test = "aAsmr3idd4bgs7Dlsf9eAF",将字符串中的数字取出，生成一个新的字符串
test = "aAsmr3idd4bgs7Dlsf9eAF"


# 现有字符串 msg = "hel@#$lo pyt \nhon ni\t hao%$" ，去掉所有不是英文字母的字符，打印结果："请理以后的结果为：hellopythonnihao"
'''msg = "hel@#$lo pyt \nhon ni\t hao%$"
result = ""
for i in msg:
    if i in 'qwertyuiopasdfghjklzxcvbnm':
        result += i
print(result)
'''
# 定义函数findall，要求返回符合要求的所有位置的起始下标，如字符串"helloworldhellopythonhelloc++hellojava"，
# 需要找出里面所有的"hello"的位置，返回的格式是一个元组，即：(0,10,21,29)
'''def findall(self,dst):
    length = len(self)
    length2 = len(dst)
    res = []
    for index in range(length):
        if self[index:index + length2] == dst:
            res.append(index)
    return tuple(res)

s = "helloworldhellopythonhelloc++hellojava"
dst = 'hello'
print(findall(s, dst))'''

# 定义一个函数 sum_test 接收一个参数 n ，在函数中计算 1 + 2 + 3 + ... + n 的值，并打印结果。
'''def sum_test(n):
    res = 0
    while n > 0:
        res += n
        n -= 1
    return res
print(sum_test(10))
'''

# 使用不定长参数定义一个函数max_min，接受的参数类型是数值，最终返回这些数中的最大值和最小值
'''def max_min(*args):
    lst = [*args]
    max_res = max(lst)
    min_res = min(lst)
    return max_res, min_res
print(max_min(1,3,4,2,4,6,7))'''

# 把一个文件中的内容，复制到另外一个文件中。
'''def copy(file1, file2):
    fr = open(file1, 'r')
    fw = open(file2, 'w')
    fw.write(fr.read())
    fr.close()
    fw.close()
    print('complete')

copy('1.txt', '2.txt')'''
# 使用os模块，把文件夹中的所有文件重命名。例如，当前test目录下所有的文件名开头添加new_这个字符串
'''import os
def rename(file_dir):
    files = os.listdir(file_dir)
    for file in files:
        filename = os.path.join(file_dir,file)
        if os.path.isfile(filename):
            new_name = os.path.join(file_dir, "new_"+file)
            os.rename(filename, new_name)
        else:
            rename(filename)

rename(R"C:\ Users\yyx89\Documents\个人资料")'''

# 定义一个水果类，然后通过水果类，创建苹果对象、橘子对象、西瓜对象并分别添加属性:颜色和价格
'''class Fruit():
    def __init__(self,fruit_type):
        self.type = fruit_type
        self.color = None
        self.price = None

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def __str__(self):
        if self.color is None or self.price is None:
            return "no setting about the color and price of fruits"
        else:
            return f"{self.type}: color is {self.color}, price is {self.price}"

# apple
apple = Fruit("apple")
apple.set_color('red')
apple.set_price(5)
print(apple)'''
# 定义一个电脑类,电脑有品牌,有价格,能放电影。分别创建2个对象"联想电脑" 和 "苹果电脑"。
# 调用放电影的动作,联想电脑播放 电影"葫芦娃"，苹果电脑播放"黑猫警长"。


# 编写一段代码以完成下面的要求：
# 定义一个Person类,类中要有初始化方法,方法中要有人的姓名和年龄属性
# 将类中的姓名是公有属性，年龄是私有属性.
# 提供获取私有属性的公有方法 get_age方法.
# 提供可以设置私有属性的方法 set_age方法，要求如果输入的年龄在 0 -- 100 之间，设置年龄，否则，提示输入不正确，.
# 重写 str 要求打印对象时，把姓名和年龄都打印出来。
class Person():
    def __init__(self, name , age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    def __str__(self):
        if 0 < self.__age < 100:
            return f"name:{self.name}, age:{self.__age}"
        else:
            return "error"
laowang = Person("laowang", 50)
print(laowang)
print(laowang.get_age())
laowang.set_age(100)
print(laowang)

# 【代码题】
# 按照如下的要求编写代码：
# - 定义 input_password 函数，提示用户输入密码
# - 如果用户输入长度 < 8，抛出异常
# - 如果用户输入长度 >=8，返回输入的密码
def input_password():
    password = input('please enter password:')
    if len(password) < 8:
        return 'error!'
    else:
        return password
input_password()
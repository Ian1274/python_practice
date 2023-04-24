"""
用户登录描述实现用户输入用户名和密码，当用户名为admin或administrator且密码为123456时，显示“登录成功”，否则显示“登录失败”，登录失败时允许重复输入三次。

def log_in(i):
    name = input("Enter name:")
    password = input("Enter password:")
    if name == "admin" or "administrator" and password == "123454":
        print("succeded login")
    else:
        print("failed login")
        if i <2 :
            i +=1
            log_in(i)
        else:
            return "game over"
i = 0
log_in(i)
"""
import random

"""
“物不知数”出自《孙子算经》。题目为今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问物几

a = 1
while a<1000:
    if a%3 == 2 and a%5 == 3 and a%7 == 2:
        print(a)
        a +=1
    else:
        a +=1
"""

"""
计算圆周率pi

n = 100000
n_c = 0
for i in range(n):
    x = random.random()
    y = random.random()
    if (x-1/2)**2 + (y-1/2)**2 < 1/4:
        n_c += 1
    else:
        continue
print(f'pi = {n_c/n*4:.10f}')
"""

"""
用户输入一个字符串，分别统计其中小写字母、大写字母、数字、空格和其他字符的个数，并在一行内输出小写字

n_str = input("随便:")
n_N = 0
n_n = 0
n = 0
n_else = 0
nstr = ""
for i in n_str:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        n_N += 1
    elif i in 'qwertyuiopasdfghjklzxcvbnm':
        n_n += 1
        nstr += i
    elif i in '0123456789':
        n += 1
    else:
        n_else += 1
print(n_N, n, n_else)
print(n_n, nstr)
"""


"""
用户登录网站经常需要输入验证码，验证码包含大小写字母和数字，随机出现。用户输入验证码时不区分大小写，只要各字符出现顺序正确即可通过验证

n = 3
while n > 0:
    password = input("enter password:")
    if str.upper(password) == "Qas2".upper():
        print("right password")
    else:
        print(f'error password, try again(left {n-1} times)')
    n -= 1
"""


"""
描述
输入一个数值，如果输入的数据为浮点数或者负数，输出”ERROR“，否则计算输入的数的阶乘并输出。
"""
'''def factorial(n):
    result = 1
    if n > 0 and isinstance(n, int):
        while n>=1 :
            result *= n
            n -=1
        return result
    else:
        return 'error'

a = factorial(4)
def f():
    n = int(input('enter a number:'))
    if isinstance(n, float) or n < 0:
        return 'error'
    else:
        return factorial(n)
b = f()
print(b)'''


"""
一个正整数，若为偶数，则把它除以2，若为大于 1 的奇数，则把它乘以3加1。经过如此有限次运算后，可以得到整数1
求经过多少次运算可得到整数1

def times():
    n = int(input('enter a positive integer:'))
    time = 0
    while n != 1:
        if n % 2 == 0:
            n=n/2
            time += 1
        elif n % 2 != 0 and n >1:
            n = 3*n + 1
            time += 1
    return f'number of operations is {time}'
print(times())"""




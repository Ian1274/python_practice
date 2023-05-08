import re

"""web = input()
res = re.match('https://www', web, re.I)
print(res.span())"""


"""phone = input()
res = re.sub('\D', '', phone)  # \D 非纯数字
print(res)

res2 = (''.join(re.findall('\d', phone)))  # \d 纯数字
print(res2)"""


msg = input()
res = re.match("[0-9)-]+", msg)
print(res.group())
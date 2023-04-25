"""operators_dict = {'<': 'less than', '==': 'equal'}
print('Here is the original dict:')
for key, value in sorted(operators_dict.items()):
    print(f'Operator {key} means {value}.')



operators_dict['>'] = 'greater than'
print(operators_dict)
print('The dict was changed to:')
for key, value in sorted(operators_dict.items()):
    print(f'Operator {key} means {value}.')"""



"""survey_list = ['Niumei','Niu Ke Le','GURR','LOLO']
result_dict = {'Niumei': 'Nowcoder', 'GURR': 'HUAWEI'}
for i in survey_list:
    if i in result_dict:
        print(f'Hi, {i}! Thank you for participating in our graduation survey!')
    else:
        print(f'Hi, {i}! Could you take part in our graduation survey?')"""



"""my_dict_1 = {'name': 'Niuniu', 'Student ID': 1}
my_dict_2 = {'name': 'Niumei', 'Student ID': 2}
my_dict_3 = {'name': 'Niu Ke Le', 'Student ID': 3}
dict_list = []
dict_list.append(my_dict_1)
dict_list.append(my_dict_2)
dict_list.append(my_dict_3)
for i in dict_list:
    key, value = i['name'], i['Student ID']
    print(f'Hi, {key}, Student ID is {value}')"""



"""cities_dict = {'Beijing': {"Capital": 'China'},
'Moscow': {"Capital": 'Russia'},
'Paris': {"Capital": 'France'}}

for key, value in sorted(cities_dict.items()):
    print(f"{key} is the capital of {value['Capital']}!")"""




"""result_dict = {'Allen': ['red', 'blue', 'yellow'],
               'Tom': ['green', 'white', 'blue'],
               'Andy': ['black', 'pink']}
for key, value in result_dict.items():
    print(f"{key}'s favorite colors is:", end='')
    for i in value:
        print(i, end=' ')
        if i == value[-1]:
            print('\n')"""



"""lst_key = ["Niuniu", "NIumei", "Niukele"]
lst_value = ["C", "C++", "Python"]
print(dict(zip(lst_key, lst_value)))"""



"""dct = {'a': ['apple', 'abandon', 'ant'],
       'b': ['banana', 'bee', 'become'],
       'c': ['cat', 'come'], 'd': ['down']}
n = input()
for i in dct[n]:
    print(i, end=' ')"""


"""dct ={'a': ['apple', 'abandon', 'ant'], 'b': ['banana', 'bee', 'become'], 'c': ['cat', 'come'], 'd': 'down'}
newletter, newword = input(1), input(2)
dct[newletter] = newword
print(dct)"""



word = input()
dct = {}
for i in word:
    dct[i] = word.count(i)
    print(dct)
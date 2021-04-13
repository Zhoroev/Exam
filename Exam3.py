def func(lst):
    lst = ['Element', 'start', *lst, 'finish']
    return lst


print(func(['hello', 5, 'John']))


def func_2(*args):
    lst = args
    slovar = {}
    num = 0
    for i in range(len(args)):
        num += 1
        slovar[lst[i]] = num
    return slovar


print(func_2('x', 5, 'John'))


def func_3(tpl):
    lst = []
    for i in tpl:
        lst.append(i)
    a = []
    list(map(lambda x: a.append(x) if x % 2 == 0 else None, lst))
    b = list(map(lambda x: x ** 2, lst))
    return a, b


a, b = func_3((1, 2, 3, 4, 5))
print(a)
print(b)

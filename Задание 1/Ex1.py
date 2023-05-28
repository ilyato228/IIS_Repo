from array import *


def left_join(ar1, ar2):
    res = []
    for i in ar1:
        if i not in ar2:
            res.append(i)
    res = array('i', res)
    return res


def get_arrays():
    list_1 = []
    list_2 = []
    len_1 = int(input('Пожалуйста, введите количество элементов первого массива: '))
    for i in range(len_1):
        list_1.append(int(input(f'Введите элемент №{i+1}: ')))
    len_2 = int(input('Пожалуйста, введите количество элементов второго массива: '))
    for i in range(len_2):
        list_2.append(int(input(f'Введите элемент №{i+1}: ')))
    return array('i', list_1), array('i', list_2)


def __main__():
    array_one, array_two = get_arrays()
    print(f'Массив, состоящий только из элементов первого массива: {[i for i in left_join(array_one, array_two)]}')


__main__()

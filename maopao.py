# -*- coding: utf-8 -*-

list1 = [2, 4, 5, 8, 2, 1, 7, 9]

def maopao(array):
    size = len(array)
    for i in range(size):
        j = size -1
        while j>i:
            if array[j] < array[j - 1]:
                array[j], array[j-1] = array[j-1], array[j]
            j -= 1


if __name__ == '__main__':
    maopao(list1)
    print list1



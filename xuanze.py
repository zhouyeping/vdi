# -*- coding: utf-8 -*-

list1 = [1, 4, 2, 4, 89, 3, 2]

def xuanze(array):
    size = len(array)
    for i in range(size):
        for j in range(i+1, size):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]


if __name__ == '__main__':
    xuanze(list1)
    print list1


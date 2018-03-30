# -*- coding: utf-8 -*-

list1 = [1, 4, 3, 5, 8, 72, 2, -2]
# 很正确.
def chapai(array):
    size = len(array)
    i = 1
    while i < size:
        j = i - 1
        tem = array[i]
        while j >= 0 and array[j] > tem:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = tem
        i += 1


if __name__ == '__main__':
    chapai(list1)
    print list1








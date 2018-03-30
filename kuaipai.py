# -*- coding: utf-8 -*-

list1 = [1, 2, 8, 2, 3, 8, 2, 0]


# 真的是太棒了呀.
def quick_sort(array, left, right):
    if left < right:
        num = array[left]
        pos = left
        i = left + 1
        while i <= right:
            if array[i] < num:
                pos += 1
                array[pos], array[i] = array[i], array[pos]
            i += 1
        array[pos], array[left] = array[left], array[pos]
        quick_sort(array, left, pos-1)
        quick_sort(array, pos + 1, right)


if __name__ == '__main__':
    quick_sort(list1, 0, len(list1) - 1)
    print list1







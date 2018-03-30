# -*- coding: utf-8 -*-

list1 = [2, 3, 1, 8, 4, 5, 1, 3]


# 终于还是解决了呀.
def merge_sort2(array, left, right):
    if left < right:
        mid = (left + right) /2
        merge_sort2(array, left, mid)
        merge_sort2(array, mid+1, right)
        res = mergeArray(array[left:mid+1], array[mid+ 1:right+1])
        for i in range(len(res)):
            array[left + i] = res[i]


def mergeArray(array1, array2):
    size1 = len(array1)
    size2 = len(array2)
    tem = [0 for i in range(size1+size2)]
    p1, p2 = 0, 0
    p = 0
    while p1 < size1 and p2 < size2:
        if array1[p1] < array2[p2]:
            tem[p] = array1[p1]
            p1 += 1
        else:
            tem[p] = array2[p2]
            p2 += 1
        p += 1
    while p1 < size1:
        tem[p] = array1[p1]
        p1 += 1
        p += 1
    while p2 < size2:
        tem[p] = array2[p2]
        p2 += 1
        p += 1
    return tem


if __name__ == '__main__':
    merge_sort2(list1, 0, len(list1)-  1)
    print list1





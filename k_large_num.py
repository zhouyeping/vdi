# -*- coding: utf-8 -*-


# succeed
def find_k_num(array, k):
    size = len(array)
    return quick_sort(array, 0, size-1, size-k)


def quick_sort(array, left, right, k):
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
        if pos == k:
            return array[pos]
        ret1 = quick_sort(array, left, pos -1, k)
        ret2 = quick_sort(array, pos + 1, right, k)
        if ret1 is not None:
            return ret1
        if ret2 is not None:
            return ret2


if __name__ == '__main__':
    list1 = [6,1,2,3, 4, 5]
    print find_k_num(list1, 1)







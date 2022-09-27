# -*- coding: utf-8 -*-
# python 二分法查找


def data_search(alist, item):
    n = len(alist)
    # 跟快速排序还是不一样的，快速排序同样是分成几个片段递归来处理，但他同时保持着原来的相对顺序
    # 二分查找不一样，分成几个片段，每个片段的下标都是从0开始，不用保持原来的相对位置
    if n > 0:
        mid = n / 2
        # 针对当n=1的情况，可以重点理解
        if item > alist[mid]:
            # 利用递归循环处理。特别注意这里return 的添加
            return data_search(alist[mid+1:],item)
        elif item < alist[mid]:
            return data_search(alist[:mid],item)
        elif item == alist[mid]:
            return True
    return False


def data_search2(alist, item):
    # 非递归版本，与递归版本最明显的区别就是，没有创建新的列表，改变的是2个游标的值
    n = len(alist)

    first = 0
    last = n-1

    while first <= last:
        mid = (first + last) / 2
        if alist[mid] > item:
            last = mid - 1
        elif alist[mid] < item:
            first = mid + 1
        else:
            return True
    return False


if __name__ == '__main__':
    alist = [6, 7, 12, 34, 48, 56, 61, 79, 89]
    print(data_search(alist, 79))

    print(data_search2(alist, 79))

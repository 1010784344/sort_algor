# -*- coding: utf-8 -*-
# python 实现选择排序


def data_sort(alist):
    n = len(alist)
    # n个数字，共要进行n-1轮，因为当只剩下最后一个数字的时候就自然而然的就是最大的，不用比对
    for j in range(n-1):
        min = j
        # 每一轮都是下标从当前加一到最后都过一遍
        for i in range(j+1,n):
            if alist[min] > alist[i]:
                # 寻找最小数值的下标
                min = i
        alist[j],alist[min] = alist[min],alist[j]


if __name__ == '__main__':
    alist = [56,48,89,12,34,6,7,79,61]
    print(alist)
    data_sort(alist)
    print(alist)
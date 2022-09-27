# -*- coding: utf-8 -*-
# python 冒泡排序


def data_sort(alist):
    n = len(alist)
    # 由图可知，每循环一轮，安排一个最大数，最后一次就只剩一个数字不用循环就最大，
    # 所以共需进行n-1轮
    for j in range(n-1):
        # 同样的，每一轮中，当排到最后，最后一个数是就是最大的，所以每轮共需循环n-1-j次
        # （有j的原因是每进行一轮，就会少一个坑）
        for i in range(n-1-j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]

if __name__ == '__main__':
    alist = [56,48,89,12,34,6,7,79,61]
    print(alist)
    data_sort(alist)
    print(alist)
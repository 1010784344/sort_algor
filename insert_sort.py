# -*- coding: utf-8 -*-
def data_sort(alist):
    # 因为有n个数字，第一个数字是不需要排序的假设是最小的，所以共需排n-1轮
    n = len(alist)
    for j in range(n-1):
        # 第一轮的无序就是从下标1开始比较的。每一轮都取无序序列中的第一个数，
        # 添加到有序序列这边(就是i)，然后再进行替换
        i = j + 1

        while i>0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
            else:
                break  

            i = i -1

if __name__ == '__main__':
    alist = [56, 48, 89, 12, 34, 6, 7, 79, 61]
    print(alist)
    data_sort(alist)
    print(alist)
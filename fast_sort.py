# -*- coding: utf-8 -*-
# pyhton 实现快速排序

def data_sort(alist,first,last):
    # 递归的终结条件
    if first >= last:
        return

    low = first
    high = last

    mid_value = alist[low]
    # 有两个游标，一个low，一个high 分别从两边开始走，当2个游标重合之时，我们就认为排好序了
    # 先把要排序的那个值放在mid_value里，当游标重合时，再把mid_value 再赋值回来
    while low < high:
        # 先从右边开始走游标满足两个条件，
        while low < high and mid_value < alist[high]:
            high = high - 1

        alist[low] = alist[high]
        # 当右边的游标走不下去再走左边的游标
        while low < high and mid_value > alist[low]:
            low = low + 1

        alist[high] = alist[low]
    #循环退出是，low == high。因为以上循环的最后一步，alist[low]已经到了赋值到high了，
    # 当前的low其实是虚位以待的
    alist[low] = mid_value

    #因为序列已经被拆分为2部分，这2部分序列分别接着套用函数进行处理（递归）
    data_sort(alist,first,low-1)
    data_sort(alist,low+1,last)




if __name__ == '__main__':
    alist = [56, 48, 89, 12, 34, 6, 7, 79, 61]
    print(alist)
    n = len(alist)
    data_sort(alist,0,n-1)
    print(alist)
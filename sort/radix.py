#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2020/6/15
# @Author: zhangxiong.net
# @Desc  :

def radix(arr):
    digit = 0
    max_digit = 1
    max_value = max(arr)
    # 找出列表中最大的位数
    while 10 ** max_digit < max_value:
        max_digit = max_digit + 1

    while digit < max_digit:
        temp = [[] for i in range(10)]
        for i in arr:
            # 求出每一个元素的个、十、百位的值
            t = int((i / 10 ** digit) % 10)
            temp[t].append(i)

        coll = []
        for bucket in temp:
            for i in bucket:
                coll.append(i)

        arr = coll
        digit = digit + 1

    return arr

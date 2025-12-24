# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 21:48:49 2025

@author: chenl

本代码将利用Python自带的最小堆数据结构,实现取出数组中最大的k个元素的功能.
"""

import heapq 

arr = [1,4,3,7,5,9,5,3,10]

res = []

k = 3

for i in range(k):
    num = arr.pop()
    heapq.heappush(res,num)
    
for item in arr:
    if item>res[0]:
        heapq.heappop(res)
        heapq.heappush(res,item)
    
print(res)
        
'''
[7, 10, 9]
'''

















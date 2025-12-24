# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 21:48:16 2025

@author: chenl

堆是一种完全二叉树(只有最下面一层没有铺满)
分为两种: (1)小顶堆:任何节点的值<=其子节点的值 (2)大顶堆:任何节点的值>=其子节点的值 
利用Python自带的heapq模块(默认实现小顶堆)和flag标注实现大顶堆
"""
import heapq

# 初始化小顶堆
'''
min_heap, flag = [], 1 # flag为1代表小顶堆 -1代表大顶堆 其实就是使用期相反数排序 入堆,出堆事再乘以相反数
'''
# 初始化最大堆
max_heap, flag = [], -1

#　元素入堆
heapq.heappush(max_heap,flag*1)
heapq.heappush(max_heap,flag*2)
heapq.heappush(max_heap,flag*3)
heapq.heappush(max_heap,flag*4)
heapq.heappush(max_heap,flag*5)

# 获取堆顶元素
peek = flag * max_heap[0]
print(peek)
print('-----')

# 获取堆大小
size = len(max_heap)
print(size)
print('-----')

#　出堆
while max_heap:
    val = flag * heapq.heappop(max_heap)
    print(val)
print('-----')


# 判断堆是否为空
is_empty = not max_heap
print(max_heap)
print(is_empty)
print('-----')

#　输入列表并建堆
min_heap = [1,3,2,5,4]
heapq.heapify(min_heap)

# 出堆
while min_heap:
    val = 1 * heapq.heappop(min_heap)
    print(val)
    

'''
5
-----
5
-----
5
4
3
2
1
-----
[]
True
-----
1
2
3
4
5
'''







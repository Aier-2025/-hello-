# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 00:33:03 2025

@author: chenl

选择排序:一种原地的时间复杂度O(n^2)的非稳定排序算法,相同元素在排序后相对顺序可能改变 
e.g. [4,2,3,4,1]第一轮排序后第一个4将排到队尾,从而改变两个4的相对顺序
每次把未排序数组中最小的元素放在前面,然后对剩下的元素继续循环.
"""

def selection_sort(nums:list[int]):
    '''选择排序'''
    n = len(nums)
    for i in range(n-1):
        # 外循环,将待排序的数组中最小元素放在最前面
        k = i # k代表最小元素索引,初始化为i
        for j in range(i+1,n):
            #　内循环．找到待排序数组中的最小元素
            if nums[j] < nums[k]:
                k = j 
        nums[i], nums[k] = nums[k], nums[i]
        
if __name__ == '__main__':
    nums = [4,2,6,1,4,2,5,7,8,0,5]
    print(nums)
    selection_sort(nums)
    print(nums)
    
'''
[4, 2, 6, 1, 4, 2, 5, 7, 8, 0, 5]
[0, 1, 2, 2, 4, 4, 5, 5, 6, 7, 8]
'''
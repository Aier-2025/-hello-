# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 00:33:38 2025

@author: chenl

插入排序:一种原地的时间复杂度O(n)的稳定排序
过程类似于整理扑克牌,一张一张地排序
"""

def insertion_sort(nums:list[int]):
    '''插入排序'''
    for i in range(1,len(nums)):# 第一张牌默认已经排好, 所以从第二张牌开始整理
        base = nums[i] # 待找到位置的牌
        j = i-1
        while j>=0 and nums[j]>base: #　从后向前找位置，如果严格比base大的牌,后移一位
            nums[j+1] = nums[j]
            j -= 1
            
        nums[j+1] = base #　找到合适位置，插入 现在的j已经不是之前的J了,退出循环前减去1了
          

if __name__ == '__main__':
    nums = [4,2,6,1,4,2,5,7,8,0,5]
    print(nums)
    insertion_sort(nums)
    print(nums)    

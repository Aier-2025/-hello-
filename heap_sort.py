# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 00:34:28 2025

@author: chenl

堆排序是一种原地操作时间复杂度O(nlogn)的非稳定排序算法

"""

def sift_down(maxheap:list[int],i:int,len:int):
    '''自顶向下"下沉:将索引为i的元素与比它大的子节点交换,直到满足终止条件'''
    while True:
        # 找到子节点
        left = 2*i+1
        right = 2*i+2
        # 停止条件:到达叶子节点,或者子节点不比它大
        # 维护 i和其子节点的最大值的索引ma, 初始化为i
        ma = i
        # 两两比较 得出其中的最大值索引
        if left < len:
            if maxheap[ma] < maxheap[left]:
                ma = left 
        if right < len:
            if maxheap[ma] < maxheap[right]:
                ma = right 
        #　如果i已经是最大值索引(包含等于),则停止循环
        if ma == i:
            return 
        #　否则将i和最大的子节点相交换
        maxheap[i], maxheap[ma] = maxheap[ma], maxheap[i]
        #　更新i的索引
        i = ma

def heap_sort(nums:list[int]):
    '''堆排序'''
    n = len(nums)
    #　除了叶子节点外的所有元素进行堆化,构建大顶堆
    for i in range((n-1)//2,-1,-1):
        sift_down(nums, i, n)
    # 对前面的元素递归进行堆化
    for i in range(n-1,0,-1):
        # 将堆顶元素和末尾元素交换
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(nums,0,i)  # sift_down(nums[:i],0,i)是错误的,因为操作的是副本，原数组未变，堆失效


if __name__ == '__main__':
    nums = [4,2,6,1,4,2,5,7,8,0,5]
    print(nums)
    heap_sort(nums)
    print(nums)    

'''
[4, 2, 6, 1, 4, 2, 5, 7, 8, 0, 5]
[0, 1, 2, 2, 4, 4, 5, 5, 6, 7, 8]
'''
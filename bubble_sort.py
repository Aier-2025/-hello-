# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 00:33:20 2025

@author: chenl

冒泡排序:一种原地的O(n)复杂度的稳定排序算法,相同元素排序后不会改变
"""

def bubble_sort(nums:list[int]):
    '''冒泡排序'''
    n = len(nums)
    flag = False # 指示变量
    for i in range(n-1,0,-1):
        # 外循环,表示要排序的前i个元素
        for j in range(i):
            if nums[j]>nums[j+1]: # 当且仅当相邻的前一个元素严格大于后一个元素时,才会执行交换动作,所以是稳定排序
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
                
        if flag == False: # 如果首轮没有发生交换动作,说明数组本就是有序的(升序),无需继续,实现最优时间复杂度O(n)
            break
        
if __name__ == '__main__':
    nums = [4,2,6,1,4,2,5,7,8,0,5]
    print(nums)
    bubble_sort(nums)
    print(nums)    

'''
[4, 2, 6, 1, 4, 2, 5, 7, 8, 0, 5]
[0, 1, 2, 2, 4, 4, 5, 5, 6, 7, 8]
'''
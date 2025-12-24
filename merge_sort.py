# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 00:34:12 2025

@author: chenl

归并排序:一种非原地时间复杂度O(nlogn)的稳定排序算法
"""

def merge_sort(nums:list[int])->list[int]:
    '''归并排序'''
    #　如果数组长度为1, 则完成排序
    if len(nums)<=1:
        return nums
    mid =len(nums) // 2
    left_ls = merge_sort(nums[:mid])
    right_ls = merge_sort(nums[mid:])
    return merge(left_ls, right_ls)

def merge(left:list[int], right:list[int]):
    '''辅助函数,合并两个有序列表'''
    n1 = len(left)
    n2 = len(right)
    res = []
    i, j = 0, 0
    while (i < n1) and (j <n2):
        if left[i]<=right[j]:  # 当两个元素相等时,优先选取左边的元素,保证了该排序算法的稳定性
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1 
    
    res.extend(left[i:])    # 注意这里合并两个列表,用的是extend方法
    res.extend(right[j:])
    return res
    


if __name__ == '__main__':
    nums = [4,2,6,1,4,2,5,7,8,0,5]
    n = len(nums)
    print(nums)
    res = merge_sort(nums)
    print(res)    

'''
[4, 2, 6, 1, 4, 2, 5, 7, 8, 0, 5]
[0, 1, 2, 2, 4, 4, 5, 5, 6, 7, 8]
'''
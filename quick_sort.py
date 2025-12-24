# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 00:33:55 2025

@author: chenl

快速排序:一种可以实现O(n logn)的原地非稳定排序算法.
"""

def quick_sort(nums:list[int],left:int,right:int):
    '''快速排序'''
    if left>=right: # 当子数组长度为1时终止递归.由于用到了递归,所以必须要有终止条件.
        return
    n = len(nums)
    pivot = partition(nums,left,right)
    quick_sort(nums,left,pivot-1)
    quick_sort(nums,pivot+1,right)
    
def partition(nums:list[int],left:int,right:int):
    '''哨兵划分'''
    i,j = left,right
    base = nums[left]
    while (i<j):
        while (i<j) and (nums[j]>=base):   # 首先移动右指针,这样确保最后和base交换的数字一定比Base更小.
            j-=1
        while (i<j) and  (nums[i]<=base):  # 要加上i<j的约束条件,最终终止时i==j,左右指针汇聚于一点
            i+=1
       
        nums[i],nums[j] = nums[j],nums[i]     # 交换左边的大数和右边小数
    nums[i],nums[left] = nums[left],nums[i]    # 交换基准和交汇点,这一步可能使得基准前面存在和它相等的值,从而不稳定
    
    return i


if __name__ == '__main__':
    nums = [4,2,6,1,4,2,5,7,8,0,5]
    n = len(nums)
    print(nums)
    quick_sort(nums,0,n-1)
    print(nums)    

'''
[4, 2, 6, 1, 4, 2, 5, 7, 8, 0, 5]
[0, 1, 2, 2, 4, 4, 5, 5, 6, 7, 8]
'''

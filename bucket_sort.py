# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 00:35:06 2025

@author: chenl


桶排序:非原地排序的时间复杂度O(n)的可能非稳定的排序算法
但是输入限定为[0,1)的浮点数,适合处理数据量较大的数据排序.
"""
import random

def bucket_sort(nums:list[int]):
    '''桶排序'''
    n = len(nums)
    k = n//2
    buckets = [[] for _ in range(k)]
    for num in nums:
        i = int(num*k)
        buckets[i].append(num)
    for bucket in buckets:
        bucket.sort()
    
    i = 0
    for bucket in buckets:
        for item in bucket:
            nums[i] = item 
            i += 1

if __name__ == '__main__':
    random.seed(42)
    nums = [random.random() for _ in range(10)]
    print(nums)
    bucket_sort(nums)
    print(nums)    
    print(nums == sorted(nums))
    
'''
[0.6394267984578837, 0.025010755222666936, 0.27502931836911926, 0.22321073814882275, 0.7364712141640124,
 0.6766994874229113, 0.8921795677048454, 0.08693883262941615, 0.4219218196852704, 0.029797219438070344]

[0.025010755222666936, 0.029797219438070344, 0.08693883262941615, 0.22321073814882275, 0.27502931836911926, 
 0.4219218196852704, 0.6394267984578837, 0.6766994874229113, 0.7364712141640124, 0.8921795677048454]

True
'''

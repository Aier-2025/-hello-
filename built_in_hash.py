# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 22:42:32 2025

@author: chenl

演示Python自带的哈希函数
"""
class ListNode:
    def __init__(self,val:int):
        self.val:int = val                  # 节点值
        self.next: ListNode | None = None   # 指向下一个节点的引用 
                                            # |表示类别可以是ListNode或None 

num = 3
hash_num = hash(num)
print(hash_num)

bol = True
hash_bol = hash(bol)
print(hash_bol)

dec = 3.1415926
hash_dec = hash(dec)
print(hash_dec)

str = 'Hello 算法'
hash_str = hash(str)
print(hash_str)

tup = (12836, '小哈')
hash_tup = hash(tup)
print(hash_tup)

obj = ListNode(0)
hash_obj = hash(obj)
print(hash_obj)

'''
3
1
326490306866391043
-7820811326509571244
1300727996259366658
144280306714
'''















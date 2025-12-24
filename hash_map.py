# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 22:40:06 2025

@author: chenl

哈希表(hash table)， 通过键（key）和值（value）, 实现高效的元素查询。
它的查询、添加、删除元素的时间复杂度都是O(1).
"""

#　初始化哈希表
hmap: dict = {}

#　添加元素
# 在哈希表中添加键值对（key, value）
hmap[12836] = '小哈'
hmap[12436] = '小4哈'
hmap[142836] = '小5哈'
hmap[15836] = '小3哈'
hmap[12046] = '小2哈'
print(hmap)

#　查询，输入键得到值
name = hmap[12046]
print(name)

# 删除操作
# 在哈希表中删除键值对
hmap.pop(15836)
print(hmap)


# 遍历哈希表
# 方式1: 遍历键值对
for k,v in hmap.items():
    print(k, '->', v)
    
# 方式2: 遍历键
for k in hmap.keys():
    print(k)
    
# 方式3: 遍历值
for v in hmap.values():
    print(v)
    















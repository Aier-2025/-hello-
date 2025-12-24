# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 22:40:31 2025

@author: chenl
本代码需要用列表构建一个哈希表
具体操作是把每个键值对通过哈希函数映射到列表中对应的"桶"里面去
"""

class Pair:
    '''把键值对封装进Pair类里面去'''
    
    def __init__(self,key:int,val:str):
        self.key = key
        self.val = val 
    
class HashTable:
    '''使用列表实现一个哈希表类'''
    
    def __init__(self):
        '''构造方法'''
        # 初始化数组,包含100个桶
        self.buckets: list[Pair | None] = [None] * 100
    
    def hash_func(self,num:int):
        '''哈希函数,用于把元素的键映射到列表索引中,寻找合适的桶'''
        return num % 100
    
    def to_Pair(self, key:int, val:str):
        '''把键值对转化为Pair对象'''
        return Pair(key, val)
    
    def put(self,key,val):
        '''插入键值对/更新键值对'''
        index = self.hash_func(key)
        pair = self.to_Pair(key, val)
        self.buckets[index] = pair
        
    def get(self,key):
        '''根据键查询值'''
        index = self.hash_func(key)
        if self.buckets[index] == None:
            return None
        return self.buckets[index].val
    
    def remove(self, key):
        '''删除键值对'''
        index = self.hash_func(key)
        self.buckets[index] = None
        
    def entry(self):
         '''遍历所有键值对'''
         result = []
         for i, e in enumerate(self.buckets):
             if e:
                 result.append(e)
         return result
     
def test_hash_table():
    
    ht = HashTable()
    
    # 1. 插入键值对
    print("1. 插入 (1, 'apple'), (2, 'banana'), (101, 'cherry')...")
    ht.put(1, "apple")
    ht.put(2, "banana")
    ht.put(101, "cherry")  # 注意：101 % 100 = 1，和 key=1 冲突！会被覆盖
    
    # 查看当前内容
    entries = ht.entry()
    print(f"   当前所有键值对: {entries}")
    print("   注意：key=1 和 key=101 哈希到同一个桶（索引1），所以只有最后插入的生效！\n")
    
    # 2. 查询
    print("2. 查询测试:")
    print(f"   get(1) = {ht.get(1)}")      # 应该是 'cherry'（被覆盖了）
    print(f"   get(2) = {ht.get(2)}")      # 'banana'
    print(f"   get(101) = {ht.get(101)}")  # 也是 'cherry'（因为桶里只有 Pair(101, 'cherry')）
    print(f"   get(999) = {ht.get(999)}")  # None\n")
    
    # 3. 更新
    print("3. 更新 key=2 的值为 'blueberry'...")
    ht.put(2, "blueberry")
    print(f"   get(2) = {ht.get(2)}\n")
    
    # 4. 删除
    print("4. 删除 key=2...")
    ht.remove(2)
    print(f"   get(2) = {ht.get(2)}")  # 应为 None
    print(f"   当前所有键值对: {ht.entry()}\n")
    
    # 5. 边界测试：重复插入、删除不存在的 key
    print("5. 边界测试:")
    ht.put(5, "grape")
    ht.put(5, "mango")  # 更新
    print(f"   重复插入 key=5: {ht.get(5)}")  # 应为 'mango'
    
    ht.remove(999)  # 删除不存在的 key
    print(f"   删除不存在的 key=999 后，get(999) = {ht.get(999)}\n")
    
    # 6. 遍历
    print("6. 最终遍历结果:")
    final_entries = ht.entry()
    for p in final_entries:
        print(f"   Key: {p.key}, val: {p.val}")
    
   

if __name__ == "__main__":
    test_hash_table()
        
'''
1. 插入 (1, 'apple'), (2, 'banana'), (101, 'cherry')...
   当前所有键值对: [<__main__.Pair object at 0x000001E2692FB110>, <__main__.Pair object at 0x000001E2692FAD50>]
   注意：key=1 和 key=101 哈希到同一个桶（索引1），所以只有最后插入的生效！

2. 查询测试:
   get(1) = cherry
   get(2) = banana
   get(101) = cherry
   get(999) = None
3. 更新 key=2 的值为 'blueberry'...
   get(2) = blueberry

4. 删除 key=2...
   get(2) = None
   当前所有键值对: [<__main__.Pair object at 0x000001E2692FB110>]

5. 边界测试:
   重复插入 key=5: mango
   删除不存在的 key=999 后，get(999) = None

6. 最终遍历结果:
   Key: 101, val: cherry
   Key: 5, val: mango
'''   
    
    






















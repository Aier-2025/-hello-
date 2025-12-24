# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 22:40:55 2025

@author: chenl

哈希冲突: 当哈希函数计算结果出现多个输入(key)对应同一个输出(index)的情况成为哈希冲突.
链式地址是解决哈希冲突的一种常用的办法.
链式地址哈希表能够通过把桶中单个元素转为链表(列表),将所有发生冲突的键值对都存放在同一个链表中.
"""

from array_hash_map import Pair

class HashMapChaining:
    '''链式地址哈希表'''
    
    def __init__(self):
        '''构造方法'''
        self.capacity = 11                                    # 哈希表容量
        self.size = 0                                         # 键值对数量
        self.load_size = 2 / 3                                # 触发扩容的负载因子阈值
        self.extend_ratio = 2                                 # 扩容倍数
        self.buckets = [[] for _ in range(self.capacity)]     # 初始化桶数组 # [[]]*self.capacity是错误写法 导致全同
        
                                                                
        
    def hash_func(self,key:int):
        '''哈希函数'''
        index = key % self.capacity
        return index
        
    
    def load_fator(self):
        '''负载因子'''
        return self.size / self.capacity
        
    def get(self,key):
        '''查询操作'''
        # 先找到对应的桶
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 然后遍历这个桶中所有元素.无需判断是否为空,空桶不会进入循环.
        for pair in bucket:
            # 如果查找到匹配的键,则输出值
            if pair.key == key:
                return pair.val
        return None
        
        
    def put(self,key:int,val:str):
        '''添加/更新操作'''
        # 判断是否需要扩容
        if self.load_fator()>=self.load_size:
            self.extend()
       
        # 计算索引,找到对应的桶
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 第一种情况,该键已存在,需要更新值
        for pair in bucket:
            if pair.key == key:
                pair.val = val
                #　更新完成，直接退出函数
                return
        # 第二种情况,该键不存在,则只需在桶中增加该键值对
        # 先把键值对转化成Pair对象
        pair = Pair(key, val)
        bucket.append(pair)
        # self.buckets[index] = bucket # 无需返回赋值,因为a=b,改变的只是引用,共享同一个内存地址,他们本质是同一个对象
        #　更新键值对数量
        self.size += 1
        
        
    def remove(self,key:int):
        '''删除操作'''
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair) # 注意: 删除的是整个键值对,而不是单单把值改成None.区分和array_hash.py的区别
                                    # list.remove(val) 是Python列表自带的按照值删除的方法
                break
        self.size -= 1
        
    def extend(self):
        '''扩容哈希表'''
        # 暂存原有哈希表
        buckets = self.buckets
        
        # 创建一个新的空哈希表, 并把self.buckets的名字分配给它
        # 注意体会其中Python语言对于对象的标签和对应内存的关系.名字只是标签而已,并不改变内存对象.
        self.capacity *=  self.extend_ratio                  # 哈希表容量改成原来的2倍
        self.buckets = [[] for _ in range(self.capacity)]    # 创建新的更长的空的桶数组
        self.size = 0                                        # 更新其中键值对个数
        
        #　把原有哈希表的对象逐个添加进新的哈希表
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key,pair.val)
        
    def print(self):
        '''打印哈希表'''
        print('[')
        for i,bucket in enumerate(self.buckets):
            res = []
            for pair in bucket:
                res.append('Line'+str(i)+':'+str(pair.key)+'->'+pair.val)
            if res:
                print(res)
        print(']')
      
    
# 主程序
if __name__ == '__main__':
    #　创建一个哈希表
    ht = HashMapChaining()
    # 添加元素
    ht.put(1,'a')
    ht.put(12,'b')
    ht.put(105,'fast')
    print('添加了三个元素后的结果')
    ht.print()
    # 修改元素
    print('修改元素后的结果:')
    ht.put(1,'b')
    ht.print()
    # 查询元素
    print('查询单个元素:')
    print(ht.get(1))
    # 删除元素
    print('删除一个元素:')
    ht.remove(105)
    ht.print()
    # 批量添加元素,检验扩容功能
    print('批量添加元素')
    for i in range(200,219):
        ht.put(i,str(i))
    ht.print()

'''
添加了三个元素后的结果
[
['Line1:1->a', 'Line1:12->b']
['Line6:105->fast']
]
修改元素后的结果:
[
['Line1:1->b', 'Line1:12->b']
['Line6:105->fast']
]
查询单个元素:
b
删除一个元素:
[
['Line1:1->b', 'Line1:12->b']
]
批量添加元素
[
['Line1:1->b']
['Line12:12->b']
['Line24:200->200']
['Line25:201->201']
['Line26:202->202']
['Line27:203->203']
['Line28:204->204']
['Line29:205->205']
['Line30:206->206']
['Line31:207->207']
['Line32:208->208']
['Line33:209->209']
['Line34:210->210']
['Line35:211->211']
['Line36:212->212']
['Line37:213->213']
['Line38:214->214']
['Line39:215->215']
['Line40:216->216']
['Line41:217->217']
['Line42:218->218']
]
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 21:16:23 2025

@author: chenl

在数组中删除首元素的时间复杂度是O(n)，这会导致出队的操作效率较低。
为了避免这个问题，我们采用环形数组（超过队尾的部分取余的方式放到数组头部去）的方式来避开这个问题。
除此之外，我还考虑使用自动扩容机制，使得该队列的长度不受数组固定容量的限制。
"""

class ArrayQueue:
    '''基于环形数组实现的队列'''
    
    def __init__(self):
        '''构造方法'''
        self._capacity = 10                 # 数组的初始容量
        self._arr = [0] * self._capacity    # 初始化数组
        self._size = 0                      # 队列的长度
        self._front = 0                     # 队首元素索引
        self._extend_ratio = 2              # 当需要扩容时，默认将列表长度扩展到原来的2倍

    def capacity(self):
        '''获取数组容量'''
        return self._capacity

    def size(self):
        '''获取队列长度'''
        return self._size
    
    def is_empty(self):
        '''判断队列是否为空'''
        return self._size == 0
    
    def check_capacity(self):
        '''根据元素数量自动扩容列表'''
        if self._size == self._capacity:
            self.extend_capacity()
        return
    
    def push(self,num:int):
        '''入队'''
        # 先判断列表容量是否已满，如果满了就扩容，确保还有剩余空间插入元素
        self.check_capacity()
        self._rear = (self._front + self._size) % self._capacity
        self._arr[self._rear] = num
        self._size += 1
        
    def peek(self):
        '''查看队首元素'''
        front_ = self._front
        return self._arr[front_]
    
    def pop(self):
        '''弹出队首元素'''
        front = self.peek()
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return front

    def extend_capacity(self):
        '''列表扩容'''
        self._arr = self._arr + [0] * self._capacity * (self._extend_ratio-1)
        self._capacity *= 2
        
    def to_list(self):
        '''输出数组'''
        return self._arr[self._front:self._rear]
    
        
if __name__ == "__main__":
    # 实例化栈
    que = ArrayQueue()
    # 依次入栈
    for i in range(100,20,-5):
        que.push(i)
    print(que.to_list())
    
    # 访问栈顶元素
    print(que.peek())
    print(que.to_list())
    
    # 出栈
    print(que.pop())
    print(que.to_list())    
    
    # 判断是否为空
    print(que.is_empty())

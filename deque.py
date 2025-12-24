# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 22:11:23 2025

@author: chenl
双向队列可以同时在两端执行入队出队的操作
我们采用Python中已经实现的deque来执行双向队列各种操作
append是从尾部入队 先入先出
pop 是从尾部出队
appendleft从头部入队
popleft从头部出队
"""

from collections import deque

#　初始化双向队列
deque = deque()

# 元素入列
deque.append(1)     # 添加至队尾
deque.append(2)
deque.append(3)
deque.appendleft(4) # 添加至队首
deque.append(5)
print(deque)

# 访问元素
# 访问队首
front = deque[0]
print(front)
# 访问队尾
rear = deque[-1]
print(rear)

# 元素出队
# 队首出队
print(deque.popleft())
print(deque)
# 队尾出队
print(deque.pop())
print(deque)

# 获取双向队列的长度
size = len(deque)
print(size)

# 判断双向队列是否为空
print(size == 0)


'''
deque([4, 1, 2, 3, 5])
4
5
4
deque([1, 2, 3, 5])
5
deque([1, 2, 3])
3
False
'''




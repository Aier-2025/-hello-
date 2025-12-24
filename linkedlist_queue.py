# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 20:36:20 2025

@author: chenl

本代码主要使用链表实现队列，并使用一系列的测试用例去验证其各项功能。
与ListNodeStack相类似，但是需要多维护一个尾节点，因为两端都开放，不像栈只有一个出口。
另外出入方式与栈不同 遵循先入先出的原则。

"""
class ListNode:
    '''
    创建一个链表类
    '''
    def __init__(self,val:int):
        self.val:int = val                  # 节点值
        self.next: ListNode | None = None   # 指向下一个节点的引用 
                                            # "|"表示类别可以是ListNode或None 

class LinkListQueue:
    '''基于链表实现的队列'''
    
    def __init__(self):
        '''构造方法'''
        self._front: ListNode | None = None
        self._rear : ListNode | None = None
        self._size : int = 0     
        
    def size(self):
        '''获取队列长度'''
        return self._size
        
    def is_empty(self):
        '''判断队列是否为空'''
        return self._size == 0
        
    def push(self,num:int):
        '''入队'''
        node = ListNode(num)
        if self.is_empty():
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1
        
    def peek(self):
        '''访问队首元素'''
        if self.is_empty():
            raise IndexError('队列为空')
        return self._front.val
        
        
    def pop(self):
        '''出队'''
        if self.is_empty():
            raise IndexError('队列为空')
        front = self._front.val
        self._front = self._front.next 
        self._size -= 1
        return front
        
    def to_list(self):
        '''转为列表用于打印'''
        res = []
        tmp = self._front
        while tmp:
            res.append(tmp.val)
            tmp = tmp.next 
        return res
        
        
if __name__ == "__main__":
    # 实例化栈
    que = LinkListQueue()
    # 依次入栈
    for i in range(1,30,3):
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

'''
[1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
1
[1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
1
[4, 7, 10, 13, 16, 19, 22, 25, 28]
False
'''
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 21:48:17 2025

@author: chenl

本代码将通过数组实现一个大顶堆
数组和堆得关系可参考ArrayBinaryTree
"""


class ArrayMaxHeap:
    '''基于数组实现大顶堆'''

    def __init__(self,nums:list):
        '''构造方法'''
        self.maxheap = nums
        # 堆化除叶节点以外的其他所有节点
        # 找到倒数第二行的最右边节点
        last_but_one_layer_tail  = self.parent(self.size())
        # 对该节点之前的节点从后向前依次下堆化
        for i in range(last_but_one_layer_tail - 1, -1, -1):
            self.sift_down(i)
        
    # 基本属性
    def size(self):
        '''列表容量'''
        return len(self.maxheap)
    
    def is_empty(self):
        return self.size() == 0
    
    def val(self,i:int):
        '''获取索引为i节点的值'''
        if i<0 or i>= self.size():
            return self.maxheap[i]
        
    def left(self,i:int):
        '''获取索引为i节点的左节点的索引'''
        return 2*i+1
    
    def right(self,i:int):
        '''获取索引为i节点的右节点的索引'''
        return 2*i+2
    
    def parent(self,i:int):
        '''获取索引为i节点的父节点的索引'''
        return (i-1)//2 
    
    # 各种操作
    def swap(self, i:int, j:int):
        '''交换索引i和j对应的元素'''
        self.maxheap[i], self.maxheap[j] = self.maxheap[j], self.maxheap[i]
        
    def peek(self):
        '''访问堆顶元素'''
        return self.maxheap[0]
        
    def push(self,num:int):
        '''元素入堆'''
        # 先把元素放置在最优叶子节点
        self.maxheap.append(num)
        # 再安排进合适的位置
        self.sift_up(self.size()-1)
        
    def sift_up(self,i:int):
        '''自底向上"上浮":将索引为i的元素与比它小的父节点交换,直到满足终止条件'''
        while True:
            # 找到父节点
            parent = self.parent(i)
            # 停止条件:到达根节点,或者父节点比它大
            if i<=0 or self.maxheap[parent]>=self.maxheap[i]:
                return
            else:
                self.swap(i,parent)
                i = parent
            
    def pop(self):
        '''元素出堆'''
        # 判空处理
        if self.is_empty():
            raise IndexError("堆为空")
        
        # 先把根节点元素和最右边叶子节点相交换,然后弹出
        self.swap(0, self.size()-1)
        peek = self.maxheap.pop()
        # 将根节点元素下沉到合适位置
        self.sift_down(0)
        
        return peek

          
    def sift_down(self,i:int):
        '''自顶向下"下沉:将索引为i的元素与比它大的子节点交换,直到满足终止条件'''
        while True:
            # 找到子节点
            left = self.left(i)
            right = self.right(i)
            # 停止条件:到达叶子节点,或者子节点不比它大
            # 维护 i和其子节点的最大值的索引ma, 初始化为i
            ma = i
            # 两两比较 得出其中的最大值索引
            if left < self.size():
                if self.maxheap[ma] < self.maxheap[left]:
                    ma = left 
            if right < self.size():
                if self.maxheap[ma] < self.maxheap[right]:
                    ma = right 
            #　如果i已经是最大值索引(包含等于),则停止循环
            if ma == i:
                return 
            #　否则将i和最大的子节点相交换
            self.swap(i,ma)
            #　更新i的索引
            i = ma
              
    def print(self):
        '''打印该大顶堆'''
        print(self.maxheap)
              
if __name__ == '__main__':
    # 实例化一个大顶堆
    arr = [1,2,3,5,6,4]
    print(arr)
    heap = ArrayMaxHeap(arr)
    heap.print()
    # 入堆
    heap.push(7)
    heap.push(5)
    heap.print()
    
    # 访问堆顶
    print(heap.peek())
    
    # 出堆
    print(heap.pop())
    heap.print()
        
'''
[1, 2, 3, 5, 6, 4]
[6, 5, 3, 1, 2, 4]
[7, 5, 6, 5, 2, 4, 3, 1]
7
7
[6, 5, 4, 5, 2, 1, 3]
'''        
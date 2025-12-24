'''
本文件将使用链表来创建一个栈类，实现其各种功能；
并通过一系列测试用例来验证其功能。
'''
class ListNode:
    '''
    创建一个链表类
    '''
    def __init__(self,val:int):
        self.val:int = val                  # 节点值
        self.next: ListNode | None = None   # 指向下一个节点的引用 
                                            # "|"表示类别可以是ListNode或None 

class LinkedListStack:
    '''
    基于链表实现的栈
    本质上就是把链表的头结点当做栈顶，并用一个变量维护该栈的长度
    '''
    
    
    def __init__(self):
        '''构造方法'''
        self._peek: ListNode | None = None
        self._size = 0
    
    def is_empty(self):
        '''判断是否为空'''
        return self._size == 0
    
    def size(self):
        '''输出栈中元素个数'''
        return self._size
        
    def push(self, num:int):
        '''入栈'''
        node = ListNode(num)
        node.next = self._peek
        self._peek = node
        self._size += 1
        
    def pop(self):
        '''出栈'''
        if self.is_empty():
            raise IndexError('栈是空的')
        peek = self._peek.val
        self._peek = self._peek.next
        self._size -= 1
        return peek
        
    def peek(self):
        '''访问栈顶元素'''
        if self.is_empty():
            raise ValueError('栈是空的')
        peek = self._peek.val
        return peek
        
    def to_list(self):
        '''转为列表打印出来'''
        res = []
        head = self._peek
        while head:
            res.append(head.val)
            head = head.next
        return res
        
if __name__ == "__main__":
    # 实例化栈
    stack = LinkedListStack()
    # 依次入栈
    for i in range(1,30,3):
        stack.push(i)
    print(stack.to_list())
    
    # 访问栈顶元素
    print(stack.peek())
    print(stack.to_list())
    
    # 出栈
    print(stack.pop())
    print(stack.to_list())    
    
    # 判断是否为空
    print(stack.is_empty())
    
    '''
    [28, 25, 22, 19, 16, 13, 10, 7, 4, 1]
    28
    [28, 25, 22, 19, 16, 13, 10, 7, 4, 1]
    28
    [25, 22, 19, 16, 13, 10, 7, 4, 1]
    False
    '''
    
    
    
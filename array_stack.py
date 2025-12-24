class ArrayStack:
    '''基于数组实现的栈'''
    
    def __init__(self):
        '''构造方法'''
        self._stack = []
        
    def size(self):
        '''获取栈的长度'''
        return len(self._stack)

    def is_empty(self):
        return self.size() == 0
    
    def push(self,item:int):
        '''入栈'''
        self._stack.append(item)
        
    def pop(self):
        '''出栈'''
        if self.is_empty():
            raise IndexError()
        return self._stack.pop()
    
    def peek(self):
        '''查看栈顶元素'''
        if self.is_empty():
            raise IndexError('栈为空')
        return self._stack[-1]
    
    def to_list(self):
        return self._stack
    
if __name__ == "__main__":
    # 实例化栈
    stack = ArrayStack()
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
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    28
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    28
    [1, 4, 7, 10, 13, 16, 19, 22, 25]
    False
    '''
    
    
    
    
    
    
    
    
    
    
    
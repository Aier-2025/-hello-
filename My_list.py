'''
列表：抽象的数据结构概念，表示有序的元素集合，支持增删查改等操作，且无需考虑容量问题。
链表天然可以视作一个列表。
数组是具有长度限制的列表。
Python自带的动态数组就是一种列表，可以实现动态扩容功能。
'''

# 先构建一个列表类
class Mylist:
    '''列表类'''
    def __init__(self):
        '''构造方法'''
        self._capacity = 10                 # 默认列表容量为10
        self._size = 0                      # 当前列表长度，即包含的元素个数
        self._arr = [0] * self._capacity    # 初始化列表
        self._extend_ratio = 2              # 当需要扩容时，默认将列表长度扩展到原来的2倍
        
    def check_index(self,index):
        '''判断输入的索引是否合法'''
        if (index<0) or (index>=self._size):
            raise IndexError('索引越界')
        return 
    
    def check_capacity(self):
        '''根据元素数量自动扩容列表'''
        if self._size == self._capacity:
            self.extend_capacity()
        return
        
    def size(self):
        '''获取当前列表长度，即当前有效元素数量'''
        return self._size
        
    def capacity(self):
        '''获取列表容量'''
        return self._capacity
        
    def get(self,index:int):
        '''访问元素'''
        # 先判断Index是否合法
        self.check_index(index)
        return self._arr[index]

    def set(self,num:int,index:int):
        '''更新已有元素'''
        # 先判断Index是否合法
        self.check_index(index)
        self._arr[index] = num

    def add(self,num:int):
        '''在尾部插入元素'''
        # 先判断列表容量是否已满，如果满了就扩容，确保还有剩余空间插入元素
        self.check_capacity()
        #　在列表尾部插入元素
        index = self._size
        self._arr[index] = num
        # 更新列表长度
        self._size += 1
        

    def insert(self,num:int,index:int):
        '''在中间插入元素'''
        # 先判断列表容量是否已满，如果满了就扩容，确保还有剩余空间插入元素
        self.check_capacity()
        # 先把index之后的数字后后移一位
        for i in range(self._size,index,-1):
            self._arr[i] = self._arr[i-1]
        # 插入num
        self._arr[index] = num
        # 更新列表长度
        self._size += 1
        
        
    def remove(self,index:int):
        '''删除元素'''
        # 先判断Index是否合法
        self.check_index(index)
        # 将index之后的数字均向前平移1位
        for i in range(index,self._size-1):
            self._arr[i] = self._arr[i+1]
        # 更新列表长度
        self._size -= 1
        
    def extend_capacity(self):
        '''列表扩容'''
        self._arr = self._arr + [0] * self._capacity * (self._extend_ratio-1)
        self._capacity *= 2
        
        
    def to_array(self):
        '''返回有效长度的列表'''
        return self._arr[:self._size]

        
# 实例化一个Mylist列表对象，并测试其各项功能
if __name__ == "__main__":
    # 主程序代码
    # 初始化列表
    mylis = Mylist()
    print(mylis.to_array())
    # 添加元素
    for i in range(14):
        mylis.add(i**2)
    print(mylis.to_array())
    # 更新列表
    mylis.set(6,2)
    print(mylis.to_array())
    # 插入元素
    mylis.insert(76,2)
    print(mylis.to_array())
    #　删除元素
    mylis.remove(8)
    print(mylis.to_array())
    # 查找元素
    print('7th:',mylis.get(7))
    print('11th:',mylis.get(11))
    '''
    []
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
    [0, 1, 6, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
    [0, 1, 76, 6, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
    [0, 1, 76, 6, 9, 16, 25, 36, 64, 81, 100, 121, 144, 169]
    7th: 36
    11th: 121
    
    '''
    
    
    
    
    
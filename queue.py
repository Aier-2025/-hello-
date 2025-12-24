'''
队列是一种遵循先入先出原则的线性数据结构
支持主要三种操作： push、pop、peek
push把元素添加在队尾
pop把队首的元素弹出，并返回该元素
peek访问队首元素
'''

from collections import deque

# 初始化队列
# 在Python中，我们一般将双向队列类deque当做队列使用
que:deque[int] = deque()
print(que)

# 元素入队
que.append(3)
que.append(5)
que.append(2)
que.append(7)
que.append(9)
print(que)

# 访问队首元素
print(que[0])
print(que)

# 队首元素出队
head = que.popleft()
print(head)
print(que)

# 获取队列的长度
size = len(que)
print(size)

# 判断队列是否为空
is_empty = (len(que) == 0)
print(is_empty)

'''
deque([])
deque([3, 5, 2, 7, 9])
3
deque([3, 5, 2, 7, 9])
3
deque([5, 2, 7, 9])
4
False
'''
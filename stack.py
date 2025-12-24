'''
栈（stack）是一种遵循先入后出逻辑的线性数据结构。
'''

#  初始化栈
stack: list[int] = []
print(stack)

# 元素入栈，push
stack.append(1)
stack.append(3)
stack.append(2)
stack.append(5)
stack.append(4)
print(stack)

# 访问栈顶元素
peek: int = stack[-1]
print(peek)

# 元素出栈
pop: int = stack.pop()
print(pop)
print(stack)

#　获取栈的长度
size = len(stack)
print(size)

# 判断是否为空
is_empty: bool = len(stack) == 0
print(is_empty)







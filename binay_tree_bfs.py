# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 14:44:23 2025

@author: chenl
层序遍历,又称广度优先搜索BFS
"""

from binary_tree import n1, TreeNode
from collections import deque

def level_order(root:TreeNode |None ) -> list[int]:
    '''层序遍历'''
    que = deque()        # 创建待访问的节点队列,先进先出
    res = []             # 结果列表
    que.append(root)     # 初始化
    while que:
        node = que.popleft() # 队首出队
        res.append(node.val) # 取出值
        if node.left:
            que.append(node.left)  # 左子节点入队
        if node.right:
            que.append(node.right) # 右子节点入队
    return res

result = level_order(n1)
print(result)
'''
<binary_tree.TreeNode object at 0x000001DFC91D2F90>
[1, 2, 3, 4, 5]
'''
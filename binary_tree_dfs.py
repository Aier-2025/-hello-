# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 14:44:44 2025

@author: chenl
深度优先搜索通常通过递归实现,
包括前序遍历(中左右) 中序遍历(左中右) 右序遍历(左右中)三类
"""

from binary_tree import n1, TreeNode

def pre_order(root:TreeNode | None):
    '''前序遍历'''
    res = []
    # 辅助函数
    def dfs(root):
        if  root is None:
            return 
        res.append(root.val)
        dfs(root.left)
        dfs(root.right)
        
    dfs(root)
    return res
    
def in_order(root:TreeNode | None):
    '''中序遍历'''
    res = []
    # 辅助函数
    def dfs(root):
       if  root is None:
           return 
       dfs(root.left)
       res.append(root.val)
       dfs(root.right)
    dfs(root)
    return res
  
    
    
def post_order(root:TreeNode | None):
    '''后序遍历'''
    res = []
    # 辅助函数
    def dfs(root):
        if  root is None:
            return 
        dfs(root.left)
        dfs(root.right)
        res.append(root.val)
    dfs(root)
    return res

res = pre_order(n1)
print('前序遍历:',res)
res = in_order(n1)
print('中序遍历:',res)
res = post_order(n1)
print('后序遍历:',res)    

'''
前序遍历: [1, 2, 4, 5, 3]
中序遍历: [4, 2, 5, 1, 3]
后序遍历: [4, 5, 2, 3, 1]
'''
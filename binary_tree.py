# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 14:43:57 2025

@author: chenl
"""

class TreeNode:
    '''二叉树节点类'''
    
    def __init__(self,val:int):
        self.val: int = val                # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None # 右子节点引用
# 初始化二叉树
# 初始化节点
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
#　构建节点之间的引用(指针)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
  
if __name__ == '__main__':      
      
    #　在n1和n2之间插入p
    p = TreeNode(0)
    n1.left = p
    p.left = n2
    
    # 删除p
    n1.left = n2











































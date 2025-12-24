# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 14:45:48 2025

@author: chenl

二叉搜索树满足如下两个条件:
(1)对于根节点,左子树的所有节点的值 < 根节点的值 < 右子树的所有节点的值
(2)任意节点的左右子树也均是二叉搜索树,满足(1)
二叉搜索树类BinarySearchTree类的查找 插入 删除效率都为O(logn)
中序遍历能够以O(n)的效率得到一个升序数组.
"""
from binary_tree import TreeNode

class BinarySearchree:
    '''二叉搜索树类'''
    
    def __init__(self,root:TreeNode | None):
        '''构造方法'''
        self._root = root
    
    def search(self,num:int)->bool:
        '''查找节点'''
        cur = self._root
        # 循环查找,越过叶节点后跳出
        while cur is not None:
            # 目标节点在cur的右子树中
            if cur.val < num:
                cur = cur.right
            elif cur.val > num:
                cur = cur.left
            else:
                return True

        return None
    
    def insert(self,val:int):
        '''插入节点'''
        # 如果根节点为空,直接令根节点为val
        node = TreeNode(val)
        if self._root is None:
            self._root = node
            return 
        
        # 维护cur和pre两个变量 用于比较和确定插入位置
        cur, pre = self._root, None
        # 跳过叶节点 直至找到合适的插入位置
        while cur:
            if cur.val == val:          # 由于二叉搜索树不允许有重复值,当val已经存在时,无法插入
                print(val,'已存在,无法插入')
                return 
            pre = cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        # 执行插入操作
        if pre.val > val:
            pre.left = node
        else:
            pre.right = node
            
    def remove(self,num:int):
        '''删除节点'''
        # 如果头结点为空,直接提前退出
        if not self._root:
            return
        
        # 维护cur和pre两个变量 用于比较和确定插入位置
        cur, pre = self._root, None
        # 跳过叶节点 直至找到合适的插入位置
        while cur:
            if cur.val == num:          # 查找到需要删除的节点,退出循环
                break 
            pre = cur                   # 注意该语句的位置,要确保pre是cur的父节点,否则就会出错
            if cur.val > num:
                cur = cur.left
            else:
                cur = cur.right
        # 如果没有满足要求的节点,则退出
        if not cur:
            return 

        # 如果要删除的节点只有0或1个叶子节点,将pre和其叶子节点相接即可
        if  (not cur.left) or (not cur.right):
            child = cur.left or cur.right
            #　考虑要删除的节点不是根节点的情况
            if cur != self._root:  
                if pre.left == cur:
                    pre.left = child 
                else:
                    pre.right = child 
            # 如果要删除的节点是根节点,直接把根节点重新赋值
            else:
                self._root = child
                
        # 如果要删除的节点右2个叶子节点
        else:
            #　找到右子树的最大叶子节点，删除后将其值赋给cur
            tmp = cur.right
            while tmp.left: # 注意:这里是while
                tmp = tmp.left 
            # 递归删除tmp
            self.remove(tmp.val)
            #　重新赋值
            cur.val = tmp.val
        

    def in_order(self):
        '''中序遍历'''            
        res = []
        # 辅助函数
        def dfs(root):
           if  root is None:
               return 
           dfs(root.left)
           res.append(root.val)
           dfs(root.right)
        dfs(self._root)
        return res
    
    def print(self):
        '''打印中序遍历结果'''
        res = self.in_order()
        print(res)
    

    
if __name__ == '__main__':
    # 创建二叉搜索树
    # 创建节点
    n1 = TreeNode(40)
    n2 = TreeNode(20)
    n3 = TreeNode(60)
    n4 = TreeNode(10)
    n5 = TreeNode(30)
    n6 = TreeNode(50)
    n7 = TreeNode(70)
    # 创建指针
    n1.left = n2
    n1.right = n3
    n2.left = n4 
    n2.right = n5
    n3.left = n6
    n3.right = n7 
    
    # 实例化
    bst = BinarySearchree(n1)
    
    #　打印初始排列
    bst.print()
    
    # 查找
    print(bst.search(50))
    print(bst.search(80))
    print(bst.search(20))
    
    # 插入
    bst.insert(19)
    bst.insert(99)
    bst.insert(60)
    bst.print()
    
    # 删除
    bst.remove(40)
    bst.print()
    bst.remove(20)
    bst.print()

'''
[10, 20, 30, 40, 50, 60, 70]
True
None
True
60 已存在,无法插入
[10, 19, 20, 30, 40, 50, 60, 70, 99]
[10, 19, 20, 30, 50, 60, 70, 99]
[10, 19, 30, 50, 60, 70, 99]
'''




    

























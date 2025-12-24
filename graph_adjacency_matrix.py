# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 21:49:42 2025

@author: chenl

本代码将基于邻近矩阵实现一个图的数据结构，并能实现增删查改的功能
输入为各个节点的值和两两成对的连接关系
输出为除对角线外连接项均为1 无连接0的邻近矩阵
"""

class GraghAdjMat:
    '''基于邻近表实现的无向图类'''
    
    def __init__(self, verticles: list[int], edges:list[list[int]]):
        '''构造方法'''
        self.verticles = verticles
        n = self.size()
        self.edges = [[0 for _ in range(n)] for _ in range(n)]
        for v1, v2 in edges:
            self.add_edge(v1, v2)
    
    def size(self):
        '''获取顶点数量'''
        return len(self.verticles)
        
    def add_vertex(self,val:int):
        '''添加顶点'''
        n = self.size()
        self.verticles.append(val)
        self.edges.append([0]*n)
        for edge in self.edges:
            edge.append(0)
            
    def add_edge(self, val1:int, val2:int): # 如果输入的是索引 则无需前两行,获取O(1)查询效率
        '''添加边'''
        i = self.verticles.index(val1)  
        j = self.verticles.index(val2)
        if i<0 or j<0 or i>=self.size() or j>=self.size() or i==j:
            raise IndexError('索引错误')
        self.edges[i][j] = 1
        self.edges[j][i] = 1
        
    def remove_vertex(self, val:int): # 如果输入的是索引 则无需第一行,获取O(1)查询效率
        '''删除顶点'''
        index = self.verticles.index(val)
        if index<0 or index>=self.size():
            raise IndexError('索引错误')
        self.verticles.pop(index)
        self.edges.pop(index)
        for e in self.edges:
            e.pop(index)
        
        
    def remove_edge(self, val1:int,val2:int): # 如果输入的是索引 则无需前两行,获取O(1)查询效率
        '''删除边'''
        i = self.verticles.index(val1)
        j = self.verticles.index(val2)
        if i<0 or j<0 or i>=self.size() or j>=self.size() or i==j:
            raise IndexError('索引错误')
        self.edges[i][j] = 0
        self.edges[j][i] = 0
        
    def print(self):
        '''打印邻近矩阵'''
        print('邻近矩阵:')
        print(' '*3+' '.join(str(self.verticles)[1:-1].split(',')))
        for i, es in enumerate(self.edges):
            print(self.verticles[i],str(es))
        
        
if __name__ == '__main__':
    #　实例化一个无向图
    vs = [1,2,3,4]
    es = [[1,2],[1,4],[2,3]]
    gragh = GraghAdjMat(vs, es)
    gragh.print()
    
    # 添加顶点
    gragh.add_vertex(6)
    
    # 添加边
    gragh.add_edge(2,6)
    
    # 打印邻近矩阵
    gragh.print()
    
    # 删除顶点
    gragh.remove_vertex(3)
    
    # 打印
    gragh.print()
    
    # 删除边
    gragh.remove_edge(2, 6)
    
    # 打印
    gragh.print()
    
    # 获取顶点数量
    print('节点个数:',gragh.size())
    
'''
邻近矩阵:
   1  2  3  4
1 [0, 1, 0, 1]
2 [1, 0, 1, 0]
3 [0, 1, 0, 0]
4 [1, 0, 0, 0]
邻近矩阵:
   1  2  3  4  6
1 [0, 1, 0, 1, 0]
2 [1, 0, 1, 0, 1]
3 [0, 1, 0, 0, 0]
4 [1, 0, 0, 0, 0]
6 [0, 1, 0, 0, 0]
邻近矩阵:
   1  2  4  6
1 [0, 1, 1, 0]
2 [1, 0, 0, 1]
4 [1, 0, 0, 0]
6 [0, 1, 0, 0]
邻近矩阵:
   1  2  4  6
1 [0, 1, 1, 0]
2 [1, 0, 0, 0]
4 [1, 0, 0, 0]
6 [0, 0, 0, 0]
节点个数: 4

'''
        
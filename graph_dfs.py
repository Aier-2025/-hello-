# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 21:51:31 2025

@author: chenl

本代码将实现对无向图的深度优先搜索,
这种"走到尽头再返回"的算法范式通常基于递归来实现.
我们依然需要借助一个哈希表visited来记录已经被访问的节点,以避免重复访问节点
"""

from graph_adjacency_list import GraphAdjList, Vertex, vals_to_vets

def dfs(graph:GraphAdjList, visited: set, vet:Vertex,res:list[int]):
    '''深度优先遍历辅助函数'''
    res.append(vet.val)
    visited.add(vet)
    for child in graph.adj_list[vet]:
        if child in visited:
            continue
        dfs(graph,visited,child,res)
    
    
    
def graph_dfs(graph: GraphAdjList, start_vet:GraphAdjList)->list[Vertex]:
    '''深度优先遍历'''
    res = []
    visited = set()
    dfs(graph,visited,start_vet,res)
    return res




if __name__ == '__main__':
    # 初始化无向图
    v = vals_to_vets([1, 3, 2, 5, 4])
    edges = [
        [v[0], v[1]],
        [v[0], v[3]],
        [v[1], v[2]],
        [v[2], v[3]],
        [v[2], v[4]],
    ]
    graph = GraphAdjList(edges,v)
    print("\n初始化后，图为")
    graph.print()
    
    # bfs
    result = graph_dfs(graph, v[0])
    print('BFS结果:\n',result)





























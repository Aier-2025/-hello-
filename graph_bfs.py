# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 21:51:17 2025

@author: chenl
本代码将实现对无向图的广度优先遍历bfs
除了visited之外,和二叉树的bfs完全一样
"""

from collections import deque
from graph_adjacency_list import GraphAdjList, Vertex, vals_to_vets

def graph_bfs(graph: GraphAdjList, start_vet: Vertex)->list[Vertex]:
    '''广度优先遍历'''
    #　构建队列,先进先出,存储待访问的节点
    que = deque([start_vet])
    # res 保存结果
    res = []
    # 集合visited记录已经访问过的节点,避免重复
    visited = set([start_vet])
    while que:
        v = que.popleft()
        res.append(v.val)
        for child in graph.adj_list[v]:
            if child in visited:
                continue
            que.append(child)
            visited.add(child)
        
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
    result = graph_bfs(graph, v[0])
    print('BFS结果:\n',result)

'''
初始化后，图为
邻接表 =
1: [3, 5],
3: [1, 2],
2: [3, 5, 4],
5: [1, 2],
4: [2],
BFS结果:
 [1, 3, 5, 2, 4]
'''













































































# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 21:50:43 2025

@author: chenl
本代码将通过邻近表(而非矩阵)实现无向图
邻近表是以节点为键,以与之相连的节点都以链表(动态数组)的形式作为值 ,的哈希表
注意, 原作者在构造方法部分存在bug, 会漏掉孤立节点 我对其进行了修正.
在邻接表中使用 Vertex 类来表示顶点，这样做的原因是：如果与邻接矩阵一样，用列表索引来区分不同顶点，那么假设要删除索引为 
的顶点，则需遍历整个邻接表，将所有大于索引全部减，效率很低。而如果每个顶点都是唯一的 Vertex 实例，删除某一顶点之后就无须
改动其他顶点了。
"""
class Vertex:
    """顶点类"""

    def __init__(self, val: int):
        self.val = val


def vals_to_vets(vals: list[int]) -> list["Vertex"]:
    """输入值列表 vals ，返回顶点列表 vets"""
    return [Vertex(val) for val in vals]

class GraphAdjList:
    """基于邻接表实现的无向图类"""

    def __init__(self, edges: list[list[Vertex]], vertices: list[Vertex] = None): # 输入参数增加了节点序列vertics
        self.adj_list = {}
        
        # 先添加所有顶点（包括孤立点）
        if vertices:
            for v in vertices:
                self.add_vertex(v)
        
        # 再添加边
        for edge in edges:
            self.add_edge(edge[0], edge[1])
            
    def size(self) -> int:
        """获取顶点数量"""
        return len(self.adj_list)

    def add_edge(self, vet1: Vertex, vet2: Vertex):
        """添加边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError()
        # 添加边 vet1 - vet2
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)

    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        """删除边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError()
        # 删除边 vet1 - vet2
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)

    def add_vertex(self, vet: Vertex):
        """添加顶点"""
        if vet in self.adj_list:
            return
        # 在邻接表中添加一个新链表
        self.adj_list[vet] = []

    def remove_vertex(self, vet: Vertex):
        """删除顶点"""
        if vet not in self.adj_list:
            raise ValueError()
        # 在邻接表中删除顶点 vet 对应的链表
        self.adj_list.pop(vet)
        # 遍历其他顶点的链表，删除所有包含 vet 的边
        for vertex in self.adj_list:
            if vet in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vet)

    def print(self):
        """打印邻接表"""
        print("邻接表 =")
        for vertex in self.adj_list:
            tmp = [v.val for v in self.adj_list[vertex]]
            print(f"{vertex.val}: {tmp},")


"""Driver Code"""
if __name__ == "__main__":
    # 初始化无向图
    v = vals_to_vets([1, 3, 2, 5, 4])
    edges = [
        [v[0], v[1]],
        [v[0], v[3]],
        [v[1], v[2]],
        [v[2], v[3]],
    ]
    graph = GraphAdjList(edges,v)
    print("\n初始化后，图为")
    graph.print()

    # 添加边
    # 顶点 1, 2 即 v[0], v[2]
    graph.add_edge(v[0], v[4])
    print("\n添加边 1-2 后，图为")
    graph.print()

    # 删除边
    # 顶点 1, 3 即 v[0], v[1]
    graph.remove_edge(v[0], v[1])
    print("\n删除边 1-3 后，图为")
    graph.print()

    # 添加顶点
    v5 = Vertex(6)
    graph.add_vertex(v5)
    print("\n添加顶点 6 后，图为")
    graph.print()

    # 删除顶点
    # 顶点 3 即 v[1]
    graph.remove_vertex(v[1])
    print("\n删除顶点 3 后，图为")
    graph.print()
    
'''
初始化后，图为
邻接表 =
1: [3, 5],
3: [1, 2],
2: [3, 5],
5: [1, 2],
4: [],

添加边 1-2 后，图为
邻接表 =
1: [3, 5, 4],
3: [1, 2],
2: [3, 5],
5: [1, 2],
4: [1],

删除边 1-3 后，图为
邻接表 =
1: [5, 4],
3: [2],
2: [3, 5],
5: [1, 2],
4: [1],

添加顶点 6 后，图为
邻接表 =
1: [5, 4],
3: [2],
2: [3, 5],
5: [1, 2],
4: [1],
6: [],

删除顶点 3 后，图为
邻接表 =
1: [5, 4],
2: [5],
5: [1, 2],
4: [1],
6: [],
'''
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 生成一个接连矩阵
# 自己创建一个符合蜂巢结构的矩阵
adj_matrix = np.array(
         [[0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
          [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
          [1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
          [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
          [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 1, 1, 0, 1, 0]])

# print(adj_matrix.T == adj_matrix)

# 将接连矩阵转换成 NetworkX 图
G = nx.Graph(adj_matrix)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
print(plt.show())

# 计算最短路径和最长路径
shortest_paths = nx.shortest_path(G)
# 在无向图中，最长路径的长度可以通过计算图的直径来得到。图的直径是指图中任意两个节点之间的最短路径中最长的一条路径。
longest_paths = nx.diameter(G)

# 输出最短路径和最长路径
for i in shortest_paths:
    for j in shortest_paths[i]:
        print(f"Shortest distance between {i} and {j}: {len(shortest_paths[i][j]) - 1}")

print(f"Longest path: {longest_paths}")


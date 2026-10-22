'''
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
对于给定的由 
n
n 个顶点、
m
m 条边构成的有向无权图（不一定连通）。依次输出以顶点 
s
s 为起点、到全部顶点的最短路径长度。
输入描述：
第一行输入三个整数 
n
,
m
,
s
(
1
≦
n
,
m
≦
2
×
1
0
5
;
 
1
≦
s
≦
n
)
n,m,s(1≦n,m≦2×10 
5
 ; 1≦s≦n)，表示顶点数量、边数量、起点编号。
此后 
m
m 行，第 
i
i 行输入两个整数 
u
i
u 
i
​
  和 
v
i
(
1
≦
u
i
,
v
i
≦
n
;
 
u
i
≠
v
i
)
v 
i
​
 (1≦u 
i
​
 ,v 
i
​
 ≦n; u 
i
​
  

​
 =v 
i
​
 )，表示图上第 
i
i 条边从顶点 
u
i
u 
i
​
  连向顶点 
v
i
v 
i
​
 。
图可能不连通、可能存在重边。不存在自环。
输出描述：
在一行上输出 
n
n 个整数，依次代表到各个顶点的最短路径。特别的，若不存在路径，则输出 
−
1
−1。
示例1
输入：
4 7 2
1 3
1 4
2 1
4 1
2 4
4 3
4 3
复制
输出：
1 0 2 1
复制
说明：

示例2
输入：
3 2 1
1 2
2 1
复制
输出：
0 1 -1
'''

# =========================
# 调试
# =========================
from io import StringIO
import sys

sys.stdin = StringIO("""3 2 1
1 2
2 1
""")

# =========================
# 解题代码
# =========================

def solve():
    import sys
    input = sys.stdin.readline

    # 多个数
    n, m, s = map(int, input().split()) # 顶点数，边数，起点（start）
    # n条边。建图：
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    '''
    算法思路：单源最短路，无权图，使用BFS。
    输出：到每个点的最短路径长度（n个数）。不联通，输出-1
    '''

    # 算法实现：BFS
    from collections import deque
    dist = [-1] * (n+1) # 距离数组，初始化为-1
    dist[s] = 0 # 起点距离为0
    queue = deque([s]) # BFS队列
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == -1: # 未访问过
                dist[v] = dist[u] + 1 # 更新距离
                queue.append(v) # 入队
    print(' '.join(map(str, dist[1:]))) # 输出距离数组，去掉0索引


# =========================
# 主程序入口
# =========================

solve()